# Rubric: probability-materials-only

Use this rubric to judge outputs for `tests/golden/probability-materials-only`.

## Critical Pass Criteria

An output fails if any critical item is missing.

- **Mode choice**: Uses Rescue Teaching Mode or equivalent behavior. It must not begin with a multi-day schedule because exam time is unknown.
- **Material grounding**: Mentions the exam notice signals: original textbook questions are about 50%, Comprehensive Training A may be tested, Comprehensive Training B is excluded, and Chapter 6/7 only test PPT-covered examples and exercises.
- **Scope control**: Marks empirical distribution function, two-population conclusions, and statistics outside mean/variance/moments as skipped or low priority unless later confirmed.
- **Mixed-PDF caution**: Reports that the two PDFs are only partially text-readable or otherwise avoids claiming full extraction.
- **Symbol decoding before formulas**: Explains at least `X`, `Xi`, `n`, `Xbar`, `theta`, `hat theta`, `L(theta)`, and MLE in plain language before relying on them.
- **Concrete first action**: Gives the first line or first decision for at least one Chapter 7 estimation question type.
- **Practice task**: Gives a concrete 30-90 minute first task tied to visible Chapter 6/7 exercises or clearly named generated mini drills.
- **Minimal questions**: Asks only for exam time/study hours, exam format, and target outcome after giving useful content.

## Strong Output Criteria

A strong output should satisfy most of these.

- Separates units into must rescue, high yield, if time remains, and skip for now.
- Uses a compact rescue-unit table or equivalent visual structure without hiding unexplained symbols.
- Covers both method of moments and maximum likelihood estimation.
- Includes one micro-example from visible materials, preferably `U[0, theta]`, Bernoulli, exponential, normal, or a discrete parameter table.
- Includes Chapter 6 basics: population/sample, simple random sample, statistic-vs-not-statistic, sample mean, variance, and moments.
- Includes Chapter 7 estimator-quality basics: unbiasedness, efficiency, and consistency as choice-question concepts.
- Makes uncertainty explicit with a simple confidence label.

## Common Failure Labels

- `overplan`: starts with a 3-day, 7-day, or hourly plan without knowing remaining time.
- `symbol_gap`: uses `Xbar`, `theta`, `MLE`, likelihood, or sample statistic without plain-language decoding.
- `scope_gap`: treats deleted topics as main priorities or predicts unobserved topics as certain.
- `practice_gap`: gives advice but no exact first practice target.
- `start_gap`: student still does not know what to write first on an estimation problem.
- `visual_gap`: table or diagram is dense with unexplained notation.
- `answer_suspect`: an estimator formula, variance formula, or MLE boundary argument is mathematically wrong.

## Review Procedure

1. Read the output once as a zero-baseline student.
2. Mark every unexplained symbol that appears before the decoder.
3. Check whether the first actionable task can be started without asking another question.
4. Check whether every high-yield claim points back to the exam notice or visible PDF evidence.
5. If a critical item fails, patch the output before accepting the case.
