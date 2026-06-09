# Probability Rescue First Pass

This is a representative first-pass answer for a user who provides the probability exam notice plus Chapter 6 and Chapter 7 PPT PDFs, but gives no remaining study time.

## What I Can See

I can already use these materials for a first rescue pass, but I should not pretend I fully extracted every PPT page. The exam notice is strong evidence; the two PDFs are mixed-readable, so this first pass is grounded in visible text plus the notice.

- Exam structure: 15 single-choice questions, 4 multiple-choice questions, and 4 calculation questions worth 39 points total.
- Strong exam signal: textbook examples and after-class exercises are central; about half of the final uses original textbook questions.
- Chapter 6/7 rule: only PPT-covered examples and exercises are tested.
- Delete for now: empirical distribution function, two-population conclusions, and statistics outside mean/variance/moments unless the teacher later re-emphasizes them.

## Rescue Units

| Unit | Priority | What It Tests | First Thing To Write |
|---|---|---|---|
| Sample, population, statistic | Must rescue | Decide whether a formula is a statistic. | “A statistic can only use the sample; it cannot contain an unknown parameter.” |
| Mean, variance, moments | Must rescue | Compute allowed sample statistics. | `Xbar` means add all observations and divide by sample size. |
| Sample joint distribution | High yield | Turn independent same-distribution samples into a product. | “Because the sample is simple random, multiply each probability/density.” |
| Method of moments | Must rescue | Estimate an unknown parameter from moments. | “Set theoretical mean/moment = sample mean/moment.” |
| Maximum likelihood estimation | Must rescue | Pick the parameter that makes the sample most plausible. | “Write the likelihood `L(theta)` as a product.” |
| Unbiased/effective/consistent | High yield | Choice and multiple-choice concepts. | “Unbiased means the estimator’s expectation equals the target.” |

## Start Here: Estimating A Parameter

This is probably the fastest Chapter 7 score gain because the template repeats across Bernoulli, exponential, normal, uniform, and discrete distribution exercises.

### Symbol Decoder

| Symbol | Plain Meaning | Exam Action |
|---|---|---|
| `X` | One random observation from the population. | Read its distribution first. |
| `Xi` | The i-th observation before numbers are plugged in. | Treat `X1, X2, ..., Xn` as independent copies when the problem says simple random sample. |
| `n` | Number of observations. | Count sample size. |
| `Xbar` | Sample average. | Add all observed values, then divide by `n`. |
| `theta` | Unknown parameter. | This is what you are solving for. |
| `hat theta` | Estimate of `theta`. | This is your final estimator. |
| `L(theta)` | Likelihood: how plausible the observed sample is under each `theta`. | Make it as large as possible. |
| `MLE` | Maximum likelihood estimation. | Choose the parameter that makes the sample most plausible. |

### Two Templates

Method of moments:
1. Find the theoretical mean or moment from the distribution.
2. Write the matching sample version, usually `Xbar`.
3. Set them equal.
4. Solve for the unknown parameter.

Maximum likelihood:
1. Write the probability or density for one observation.
2. Multiply all observations to form `L(theta)`.
3. Take `ln L(theta)` if the product is hard.
4. Differentiate and solve, or check the allowed range/boundary.
5. Write the answer with a hat.

### Micro-Example: Uniform Distribution On `[0, theta]`

What the problem is asking: the upper endpoint `theta` is unknown, and the sample values tell us how large it must be.

Method of moments:
- The mean of `U[0, theta]` is `theta / 2`.
- Set `theta / 2 = Xbar`.
- So `hat theta = 2 Xbar`.

Maximum likelihood:
- Every observed value must be between 0 and `theta`.
- So `theta` must be at least the biggest observed value.
- The likelihood is largest when `theta` is the smallest legal value.
- So `hat theta = max(X1, X2, ..., Xn)`.

## Now Do This First

For the next 60-75 minutes:

1. Copy the symbol decoder and rewrite each symbol in Chinese plain language.
2. Do one Chapter 7 method-of-moments question and force the first line: “theoretical moment = sample moment.”
3. Do one Chapter 7 MLE question and force the first line: “`L(parameter) = product of probabilities/densities`.”
4. Do one Chapter 6 statistic-identification question: cross out any expression containing an unknown parameter.
5. Stop and check only the first broken step, not the whole chapter.

I still need three things to make the next pass sharper: how many hours remain, whether the exam is closed-book/open-book, and whether your goal is passing, stable score, or high score.
