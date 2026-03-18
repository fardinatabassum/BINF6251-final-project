## Recap of Project (Short)
* Summary of:
    * The research question.
    * The chosen algorithm and algorithm class.
    * The type of data you plan to use.
* This should be concise enough that a reader can understand the rest of the document without opening `PROPOSAL.md`.

## 2. Inputs, Outputs, and Assumptions

* Precisely define:
    * The expected input(s) to your algorithm (including data types and formats).
    * The expected output(s) (what you return or produce).
* State key assumptions (e.g., “All sequences are uppercase A/C/G/T,” “Graph is simple and directed,” “Emission probabilities are normalized”).\
## 3. Detailed Pseudocode
* Provide pseudocode that:
  * Has clear function signatures or step headings.
  * Explicitly describes main loops, conditionals, and data structures.
  * Handles at least one non-trivial edge case (e.g., empty input, unexpected characters, disconnected graph).
* Use code-style formatting (indented blocks, consistent naming) so that another student could implement it in Python or another language.
## 4. Complexity and Bottlenecks
* Analyze the time and space complexity of your algorithm in terms of relevant parameters (e.g., sequence length, number of reads, number of states).
* Identify the most expensive parts of the algorithm and discuss:
  * When performance might become a problem.
  * Any ideas you have for mitigating performance issues (e.g., pruning, indexing, approximate methods)?

## 5. Validation and Testing Plan
* Describe how you plan to test your implementation:
    * At least one small, hand-crafted example where you know or can reason about the correct answer.
    * At least one synthetic or real dataset for stress testing.
* Explain:
  * What results do you expect from these tests?
  * What would constitute evidence that the algorithm is behaving incorrectly?
* Outline the kinds of automated tests you will implement (e.g., unit tests for subfunctions, end-to-end tests, property/invariant checks).
## 6. Updated Pitfall and Risk Log
* Revisit the pitfalls from Part 1:
  * Which ones still seem relevant?
  * Which new pitfalls have emerged as you wrote the pseudocode?
* For each risk, add a brief note on how your design (or upcoming implementation) will address it.

## 7. Generative AI Disclosure (If Used)
* If you used generative AI to help with pseudocode or explanations:
  * Add an appendix titled `Generative AI Usage`.
  * Include tool/version, full prompts, how it influenced your pseudocode, and why you chose to use it.
