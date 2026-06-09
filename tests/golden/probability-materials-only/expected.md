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

## Task Board: Open These First

| Order | Source | What To Do | Why This Comes First | First Line / First Decision | Stop Point | Self-Check |
|---|---|---|---|---|---|---|
| 1 | `第七章.pdf`, page 27, exercise 7-1 question 5 | Do only the setup for both method of moments and MLE. | This visible exercise asks for both estimates from one distribution table, so it trains the highest-yield Chapter 7 calculation pattern. | First read the table as `P(X=0)=theta^2`, `P(X=1)=2theta(1-theta)`, `P(X=2)=theta^2`, `P(X=3)=1-2theta`; then count how many sample values are 0, 1, 2, and 3. | Stop after writing the sample mean and the likelihood product by counts. | The probabilities in the likelihood should use exponents equal to the observed counts, not just appear once. |
| 2 | `第六章新.pdf`, page 42, comprehensive training question 4 | Compute the population mean/variance and the sampling distribution of the sample mean for sample size 2. | This visible task trains mean, variance, and sample mean distribution, which are explicitly kept by the exam notice. | First list all possible samples of size 2 according to the sampling rule; then write the sample mean for each. | Stop after the list of possible sample means and their probabilities. | The average of the sample-mean distribution should match the population mean. |
| 3 | `第六章新.pdf`, visible Chapter 6 exercises 6-1/6-2 or fallback if the exact page is unreadable | Do one statistic-vs-not-statistic check. | Choice questions can ask whether an expression is a statistic, and this is fast to rescue. | First decision: does the expression contain an unknown population parameter? If yes, mark it as not a statistic. | Stop after classifying 3 expressions. | A statistic can use sample data and known constants, but not an unknown parameter. |

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

1. Spend 10 minutes copying only the symbols needed for Task 1: `X`, `xi`, `n`, `theta`, `L(theta)`, and `MLE`.
2. Spend 25 minutes on `第七章.pdf` page 27, exercise 7-1 question 5. Do not try to finish everything at once; first write the counts and likelihood product.
3. Spend 25 minutes on `第六章新.pdf` page 42, comprehensive training question 4. Stop after listing sample means and probabilities.
4. Spend 10 minutes checking only the first broken step: wrong probability from the table, wrong count exponent, missing sample mean, or unknown parameter used inside a statistic.

## Questions To Ask After The Useful First Pass

- When is the exam, or how many study hours remain?
- Is the final closed-book, open-book, machine-based, or unknown?
- Is the goal passing, stable score, or high score?
