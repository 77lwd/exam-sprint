# Golden Expected Output: probability-materials-only

The exact wording may vary, but a passing answer should preserve this structure, source grounding, and zero-baseline readability.

## What I Can See

- Materials: one exam notice plus Chapter 6 and Chapter 7 PPT PDFs.
- Evidence strength: medium. The exam notice is strong, but both PDFs are `mixed`, so the answer should not claim complete extraction.
- Exam signals: textbook examples and after-class exercises are central; original textbook questions are about 50%; Comprehensive Training A can appear; Comprehensive Training B is excluded.
- Question format: single choice, multiple choice, and calculation. Calculation questions total 39 points.
- Chapter 6/7 deletion rule: skip empirical distribution function, two-population conclusions, and statistics outside mean, variance, and moments unless the teacher later says otherwise.

## Rescue Units

| Unit | Priority | Why It Matters | First Action | Practice Source | Skip For Now |
|---|---|---|---|---|---|
| Sample, population, and statistic | Must rescue | Choice questions can ask whether an expression is a statistic. | Decode `X`, `Xi`, `n`, unknown parameter, and check whether the expression contains an unknown parameter. | Chapter 6 section 6.1-6.2 visible examples and exercises. | Long theory of descriptive statistics. |
| Sample mean, variance, and moments | Must rescue | These are explicitly kept by the exam notice. | Write `Xbar = sum Xi / n`, then choose corrected or uncorrected variance according to wording. | Chapter 6 exercises 6-2 and Comprehensive Training A visible pages. | Median, mode, range, coefficient of variation unless confirmed in scope. |
| Sample joint distribution | High yield | Repeated Chapter 6 exercise type for simple random samples. | First write: independent and same distribution, so multiply each probability or density. | Chapter 6 examples for Poisson/exponential and exercises 6-1. | Empirical distribution function, because the notice deletes it. |
| Method of moments | Must rescue | Chapter 7 uses it repeatedly and it is learnable fast. | Set theoretical mean or moment equal to sample mean or sample moment, then solve the parameter. | Chapter 7 exercises 7-1 and Comprehensive Training A. | Abstract estimator theory before doing examples. |
| Maximum likelihood estimation | Must rescue | It appears in examples and exercises and is calculation-heavy. | Build `L(theta)` as a product, take `ln L` if useful, differentiate or use boundary constraints. | Chapter 7 examples 6-8, exercises 7-1, Comprehensive Training A. | Proof-heavy derivations beyond the exercise template. |
| Unbiasedness, efficiency, consistency | High yield for choices | These are likely choice/multiple-choice definitions. | Decode each as expectation equals target, smaller variance among unbiased estimators, convergence as sample size grows. | Chapter 7 section 7.2 and exercises 7-2. | Full theorem proofs unless the user asks. |

## Start Here: Parameter Estimation

### What This Topic Is Testing

The examiner gives a distribution with an unknown number and sample data. Your job is to turn the sample into an estimate of that unknown number.

### Symbol Decoder

| Symbol In Material | Plain Meaning | What You Do With It |
|---|---|---|
| `X` | The random variable for one observation from the population. | Read its distribution first, such as Bernoulli, exponential, normal, or uniform. |
| `Xi` | The i-th observed item before numbers are plugged in. | Treat `X1, X2, ..., Xn` as independent copies of `X` unless told otherwise. |
| `xi` | The actual observed value of `Xi`. | Plug these numbers into products, sums, and averages. |
| `n` | Sample size. | Count how many observations there are. |
| `Xbar` | Sample average: add all observations and divide by `n`. | Use it for mean, moment estimates, and many final answers. |
| `theta` | The unknown parameter the problem wants you to estimate. | Solve for it; do not treat it as a known number. |
| `hat theta` | Your estimate of `theta`. | This is the final estimator or estimate. |
| `L(theta)` | Likelihood: how plausible the observed sample is under each `theta`. | Make it as large as possible for MLE. |
| `MLE` | Maximum likelihood estimation. | Choose the parameter value that makes the observed data most plausible. |

### Question-Type Recognition

If the problem says “矩估计”, use method of moments. If it says “极大似然估计” or “最大似然估计”, use MLE. If it asks which estimator is better, move to unbiasedness, efficiency, or consistency.

### Do-This Template

Method of moments:
1. Write the theoretical mean or moment from the distribution.
2. Write the matching sample moment, usually `Xbar`.
3. Set them equal.
4. Solve for the unknown parameter.

Maximum likelihood:
1. Write the probability or density for one observation.
2. Multiply all observations to get `L(theta)`.
3. If it is easier, take `ln L(theta)`.
4. Differentiate and solve, or check boundary conditions.
5. Put a hat on the solved parameter.

### Micro-Example From The Visible Materials

Problem type: `X ~ U[0, theta]`; estimate `theta`.

- Plain meaning: each observed value must lie between 0 and the unknown upper limit `theta`.
- Method of moments: the theoretical mean of `U[0, theta]` is `theta / 2`. Set `theta / 2 = Xbar`, so `hat theta = 2 Xbar`.
- MLE: all sample values must fit under `theta`, so `theta` must be at least the largest observed value. The likelihood is largest when `theta` is as small as legally possible, so `hat theta = max(X1, ..., Xn)`.

### Now Practice: First 60-75 Minutes

1. Spend 10 minutes copying the symbol decoder above onto paper and rewriting each symbol in your own words.
2. Spend 25 minutes on Chapter 7: do exercise 7-1 question 1 or the `U[0, theta]` Comprehensive Training A question if available. For each, force yourself to write both method-of-moments and MLE first lines.
3. Spend 20 minutes on Chapter 6: do one “is this a statistic?” question and one sample mean/sample variance question.
4. Spend 10 minutes checking only the first broken step: wrong formula, wrong symbol meaning, or wrong scope.

## Questions To Ask After The Useful First Pass

- When is the exam, or how many study hours remain?
- Is the final closed-book, open-book, machine-based, or unknown?
- Is the goal passing, stable score, or high score?
