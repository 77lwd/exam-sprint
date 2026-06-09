# Golden Case: probability-materials-only

## User Situation

The user provides only course materials and no remaining study time, no exam date, no explicit target score, and no precise request. The skill should default to Rescue Teaching Mode and produce a first usable rescue artifact before asking questions.

## User Prompt

```text
帮我看这三份概率期末材料：
- 2026年工科概率期末考试说明 (1).docx
- 第六章新.pdf
- 第七章.pdf
```

## Source Materials

- `2026年工科概率期末考试说明 (1).docx`
- `第六章新.pdf`
- `第七章.pdf`

## Extracted Material Evidence

### Exam Notice

- Chapter 6 and Chapter 7 scope: only examples and exercises covered in the PPT are tested.
- Deleted from Chapter 6 and Chapter 7: statistics other than mean, variance, and moments; empirical distribution function; two-population conclusions.
- Final exam mainly uses textbook examples and after-class exercises, plus Comprehensive Training A.
- Comprehensive Training B is not tested.
- Original textbook questions are about 50% of the final exam.
- Question types: 15 single-choice questions, 3 points each; 4 multiple-choice questions, 4 points each; 4 calculation questions totaling 39 points.

### PDF Probe Evidence

- `第六章新.pdf`: 83 pages, `mixed`, medium confidence. Readable samples include Chapter 6 titles, simple random sample, sample joint distribution, sample statistic, sample mean, variance, standard deviation, moments, and exercises from 6-1 and 6-2.
- `第七章.pdf`: 53 pages, `mixed`, medium confidence. Readable samples include Chapter 7 titles, point estimation, method of moments, maximum likelihood estimation, unbiasedness, efficiency, consistency, and exercises from 7-1, 7-2, and Comprehensive Training A.

### Visible High-Yield Exercise Signals

- Chapter 6 visible exercises include identifying population/sample, writing sample joint distributions, judging whether an expression is a statistic, computing sample mean and sample variance, and comparing allowed statistics.
- Chapter 7 visible exercises include Bernoulli, exponential, normal, uniform, and discrete-parameter estimation questions using method of moments and maximum likelihood estimation.
- Chapter 7 Comprehensive Training A includes a direct comparison of method-of-moments and MLE for `U[0, theta]`.

## Expected Mode

Use Rescue Teaching Mode. Do not create a 3-day, 7-day, or 24-hour plan because remaining time is unknown.
