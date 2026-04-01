import numpy as np
import math
from data_reader import read_fasta
from utils import save_as_bed


def viterbi_decode(sequence, states, start_p, trans_p, emiss_p, global_offset=0):
    """
    Performs Viterbi decoding to identify CpG islands in a genomic sequence.

    This implementation uses log-space transformations to ensure numerical stability
    over long genomic sequences (such as Human Chromosome 22) and includes a
    neutral coasting logic to handle assembly gaps ('N' characters).

    Args:
        sequence (str): The DNA sequence string (A, C, G, T, N).
        states (list): List of hidden states [0, 1] where 0=Background, 1=Island.
        start_p (list): Log-probabilities for the initial state distribution.
        trans_p (dict): Nested dictionary of log-transition probabilities.
        emiss_p (dict): Nested dictionary of log-emission probabilities.
        global_offset (int): Offset to align local indices with genomic coordinates.

    Returns:
        list: A list of tuples (start, end) representing detected CpG islands.
    """
    L = len(sequence)
    S = len(states)

    # Initialization
    # V[state, index] stores the maximum log-probability of reaching a state
    # B[state, index] stores the backpointer to the most likely previous state
    V = np.full((S, L), -np.inf)
    B = np.zeros((S, L), dtype=int)

    for s in range(S):
        # Initial score = Start Probability + Emission Probability of the first base
        V[s, 0] = start_p[s] + emiss_p[s].get(sequence[0], math.log(0.25))

    # Main Recursive Loop (The Trellis)
    for i in range(1, L):
        current_obs = sequence[i]

        # Assembly Gap Handling ('N')
        # If an 'N' is encountered, we maintain the previous log-score and
        # coast through the gap to preserve genomic coordinate alignment.
        if current_obs not in ['A', 'C', 'G', 'T']:
            for s in range(S):
                V[s, i] = V[s, i - 1] + math.log(0.25)
                B[s, i] = s
            continue

        for s in range(S):
            # Calculate (Previous Score + Transition to Current State) for all possible origins
            scores = [V[prev_s, i - 1] + trans_p[prev_s][s] for prev_s in range(S)]

            # Store the maximum path score and the index of the state that produced it
            V[s, i] = max(scores) + emiss_p[s].get(current_obs, math.log(0.25))
            B[s, i] = np.argmax(scores)

    # Path Reconstruction (Backtracking)
    # Identify the best ending state and follow the backpointers (B) from right to left
    best_final_state = np.argmax(V[:, L - 1])
    path = np.zeros(L, dtype=int)
    path[L - 1] = best_final_state

    for i in range(L - 2, -1, -1):
        # Looks at the backpointer for the state we just found at index i+1
        path[i] = B[path[i + 1], i + 1]

    # Post-Processing & Biological Filtering
    # Identifies contiguous segments of State 1 and applies a 200bp length threshold.
    islands = []
    current_start = None

    for idx, state in enumerate(path):
        if state == 1 and current_start is None:
            current_start = idx
        elif state == 0 and current_start is not None:
            length = idx - current_start
            # Threshold to only keep islands >= 200bp
            if length >= 200:
                islands.append((current_start + global_offset, idx + global_offset))
            current_start = None

    # Ensure islands that reach the end of the sequence are recorded
    if current_start is not None:
        length = L - current_start
        if length >= 200:
            islands.append((current_start + global_offset, L + global_offset))

    return islands


if __name__ == "__main__":
    """
    Execution block for Prototype Validation.
    Uses calibrated probabilities to test sensitivity on synthetic and local FASTA data.
    """
    # Model calibration: States 0 (Background) and 1 (CpG Island)
    states = [0, 1]
    start_p = [math.log(0.5), math.log(0.5)]

    # Transition matrix: Adjusted to favor state persistence (stickiness)
    trans_p = {
        0: {0: math.log(0.95), 1: math.log(0.05)},
        1: {0: math.log(0.05), 1: math.log(0.95)}
    }

    # Emission matrix: Weighted heavily for G/C content in the Island state
    emiss_p = {
        0: {'A': math.log(0.25), 'C': math.log(0.25), 'G': math.log(0.25), 'T': math.log(0.25)},
        1: {'A': math.log(0.01), 'C': math.log(0.49), 'G': math.log(0.49), 'T': math.log(0.01)}
    }

    # Prototype Execution
    file_path = "data/prototype_genome.fa"
    print(f"--- Loading data from {file_path} ---")

    try:
        sequence = read_fasta(file_path)
        print(f"Successfully loaded {len(sequence)} base pairs.")

        print("Running Viterbi decoding")
        results = viterbi_decode(sequence, states, start_p, trans_p, emiss_p)

        if results:
            print(f"Success! Found {len(results)} island(s).")
            print(f"Genomic Coordinates: {results}")

            # Save to the root directory for browser compatibility 
            save_as_bed(results, "predictions.bed")
        else:
            print("No islands detected. Check if sequence is >200bp or if GC-content is sufficient.")

    except FileNotFoundError:
        print(f"Error: {file_path} not found. Verify the file path relative to the root directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
