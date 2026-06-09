# Evaluation Cases

Use these cases when testing or updating the skill. They are not normally loaded during student-facing work.

## Case 1: Materials Only, No Time Given

User gives an exam notice and two chapter PDFs, but no request text.

Pass criteria:
- Does not invent a 3-day or 7-day plan.
- Extracts explicit exam signals first.
- Produces a rescue skeleton with 3-8 units.
- Produces a 3-5 item task board when examples/exercises/pages are visible.
- Gives one first 30-90 minute task.
- Asks for exam time, format, and target only after giving a useful first pass.

## Case 2: Student Says "I Do Not Understand"

User says they cannot understand a formula-heavy topic.

Pass criteria:
- Starts with plain-language purpose.
- Decodes symbols before formula shortcuts.
- Shows a micro-example.
- Assigns one small practice task.
- Does not dump a full chapter summary.

## Case 3: Scan-First PDF

User provides a mostly scanned PDF.

Pass criteria:
- Runs or references `pdf_probe.py` first.
- Reports readable status and confidence.
- Produces a provisional map from visible evidence.
- Requests 1-3 high-value supplements.
- Does not start full OCR unless Deep Scan Mode is confirmed.

## Case 4: Wrong Answer Repair

User submits a partial solution.

Pass criteria:
- Identifies the first broken step.
- Gives a repair table with step, issue, fix.
- Assigns a near-transfer drill.
- Avoids re-teaching the whole chapter.

## Case 5: User Explicitly Wants A Plan

User gives exam time and asks for a schedule.

Pass criteria:
- Uses Sprint Planning Mode.
- Includes a short rescue warm-up before long study blocks if the student is weak.
- Keeps the plan tied to topic priority and visible material evidence.
- Includes review and self-test loops, not just reading blocks.

## Case 6: Generated Practice

User asks for self-test questions.

Pass criteria:
- Questions match the subject playbook.
- Each question is answerable from the taught template or visible materials.
- No unexplained symbols appear in the question.
- Answer key and pitfalls are held back if the user asks to drill first.
- If answers are provided, they are checked for ambiguity and scope.

## Case 7: Probability Materials Only Golden Case

Use `tests/golden/probability-materials-only/` and `examples/probability-rescue-first-pass.md` when validating the real Chapter 6/7 probability rescue workflow.

Pass criteria:
- Uses the exam notice as the strongest source signal.
- Treats the two PDFs as mixed-readable rather than fully extracted.
- Does not invent a schedule when study time is unknown.
- Starts with symbol decoding and question-type templates, especially method of moments and maximum likelihood estimation.
- Gives a concrete 30-90 minute first task tied to visible exercises.
- Includes exact task cards for visible evidence such as Chapter 7 page 27 exercise 7-1 question 5 and Chapter 6 visible comprehensive-training/sample-statistic exercises when available.

## Case 8: Materials Feel Useless Without Task-Level Guidance

User gives an exam notice and partial chapter PDFs, then says the first output is not useful because it only gives topic-level advice.

Pass criteria:
- Acknowledges the gap without defending the previous answer.
- Rewrites the answer around a task board, not a bigger summary.
- Names exact pages, exercises, screenshots, or generated fallback drills.
- Explains what cannot be task-grounded from the current material and requests only the smallest missing supplement.
- Avoids broad statements such as "review the chapter" unless attached to a concrete task.
