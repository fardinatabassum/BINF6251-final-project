## Project Title
Probabilistic Identification of CpG Islands in the Human Genome using Hidden Markov Models
## Research Question
The research question for my final project is, can a first-order Hidden Markov Model be used to accurately identify CpG island boundaries in human promoter regions by differentiating between island and background genomic states?

CpG Islands are important epigenetic regulators located near the transcription start sites in most genes in humans. The methylation state in these islands controls gene expression by acting as an on/off switch. Hypermethylation of CpG islands is linked to various cancers and developmental disorders. Having a way to identify these islands can provide us with valuable insights to understand these regions and how they control responses to the environment. This can then help us understand how diseases like cancer progress.

## Algorithm and Algorithm Class
The algorithm class that I will be using is Hidden Markov Models (HMM). The specific algorithm I plan to implement will be the Viterbi algorithm to decode the most likely hidden state path from the observed nucleotide sequence. I chose this algorithm because HMMs can model the relationship between observable sequence data and unobserved biological states. The nucleotide sequence is visible, and the functional identity of a CpG island versus the background is a hidden property that must be calculated. By using the Viterbi algorithm, we can use the Markov Property to account for the specific transition frequencies that window-based counting methods can overlook. This probabilistic approach allows for a more accurate identification of genomic boundaries.
   
## Data Plan
I will be using the human genomic sequence data, specifically focusing on Chromosome 22. I chose chromosome 22 because it is one of the smaller chromosomes, which allows for the HMM to run faster, making testing easier and computationally less intensive. However, chromosome 22 also has high gene density, which means it has a high density of promoter regions and, consequently, CpG islands. To validate my model, I will also be using the CpG Islands track from the UCSC Table Browser that identifies the known start and end coordinates of CpG islands on this chromosome.
  
### Sources: 
* UCSC Genome Browser
* CpG Islands track from the UCSC Table Browser
* Synthetic FASTA file for initial logic testing

### Data type(s):
- FASTA file for raw genomic sequences of chromosome 22
- BED file genomic coordinates of CpG islands to calculate sensitivity and specificity

Licensing or access considerations: Public domain is being used, so no special licenses or permissions are required for access

### Prototype data:
This data will be a small synthetic DNA sequence. This sequence will be mostly background, containing low GC content with a region in the middle containing a high frequency of C and G nucleotides. This allows me to control and know where the hidden state is, thus allowing me to verify the HMM logic. I can check for the transition and emission probabilities to see if they correctly identify the transition from background to island before I move to a much larger dataset of the actual Chromosome 22. The prototype relates to the realistic dataset as a controlled benchmark. It mimics the statistical properties of human genomic DNA, such as CG suppression in the background and high density in the islands.

## Success Criteria
1. Define what “success” looks like for your project:
2. Expected outputs.
3. At least one way you will check whether your result is reasonable (e.g., comparison to a standard tool, known small example, known motif, or simulated ground truth).
   
## 5. Pitfall Scan
1. Identify at least three
    1. Data-related issues (e.g., noisy or biased data, missing annotations).
    2. Algorithmic issues (e.g., runtime or memory blowup, numerical stability, sensitivity to parameters).
    3. Evaluation issues (e.g., no ground truth, risk of overfitting, misleading metrics).
2. For each pitfall:
    1. Describe why it is a realistic concern in your chosen context.
    2. Outline a strategy for detecting and mitigating it (even if only partially).
       
## Planned Repository Structure (Initial Sketch)
```
/ BINF6251-final-project
├── data/
│   ├── hg38_chr22.fa            # Chromosome 22 FASTA from UCSC
│   ├── ucsc_cpg_islands.bed     # CpG island BED file
│   └── prototype_genome.fa      # Synthetic sequence
├── hmm.py                       # HMM and Viterbi implementation
├── data_readers.py              # FASTA/BED parsing and cleaning
├── evaluate.py                  # Comparison logic and validation
├── .gitignore                   # Excludes large data files
├── LICENSE                      # Project licensing
├── PROPOSAL.md                  # Project proposal
└── README.md                    # Project overview
```

## Generative AI Disclosure (If Used)
Claude was used to understand the different algorithms and biological contexts. 
