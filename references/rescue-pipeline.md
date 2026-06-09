# Rescue Pipeline

Use this pipeline when the user provides course materials, an exam notice, screenshots, past papers, or messy notes and does not already know what to do.

The pipeline adapts a production-style "extract -> skeleton -> create -> review -> revise" flow into a fast exam rescue loop. Keep the first pass small enough to help immediately.

## Pipeline

1. **Probe and Inventory**
   - List available files, readable status, page or slide counts when available, and obvious gaps.
   - For PDFs, use `scripts/pdf_probe.py` before ad hoc extraction.
   - Pull explicit exam scope, deleted topics, teacher highlights, question types, point values, and original-question signals first.

2. **Build a Rescue Skeleton**
   - Produce 3-8 rescue units, not a full chapter summary.
   - Each rescue unit should contain:
     - `unit`: short topic or question family name.
     - `why_it_matters`: likely score source or prerequisite value.
     - `student_gap`: what a weak student probably does not understand.
     - `symbols`: symbols, acronyms, or terms that must be decoded.
     - `first_action`: the first line or first decision the student should write.
     - `practice_source`: exact exercise/page/file if visible; otherwise a small generated drill.
     - `skip_or_defer`: what not to study now.
     - `confidence`: high, medium, or low.
   - Source-ground the skeleton with visible file names, page numbers, slide titles, exercise numbers, or detected text when possible.

3. **Choose the Subject Playbook**
   - Use `references/course-types.md` to classify the scoring type.
   - Then load `references/subject-playbooks.md` for the matching rescue style.
   - Let the playbook control default artifacts and practice format.

4. **Create the First Rescue Pack**
   - Use `references/rescue-output-patterns.md`.
   - Include symbol decoding before formula tables.
   - Include one micro-example or a partially solved example.
   - Include a first 30-90 minute task if exam time is unknown.

5. **Self-Review Before Final**
   - Use `references/self-review-rubric.md`.
   - Fix critical failures before replying: unexplained symbols, no first action, no practice task, unsupported claims, or invented study time.

6. **Iterate**
   - If the student attempts questions, switch to answer checking and mistake repair.
   - If the student gives remaining time, add Sprint Planning Mode after the rescue pack.
   - If the student asks for complete extraction, switch to Deep Scan Mode.

## Output Contract

For a first pass from materials, prefer this shape:

```text
Material Signal
Rescue Skeleton
First Topic To Learn
Symbol Decoder
How To Recognize This Question
Do-This Template
Micro-Example
Now Practice
Common Traps
Missing Info Needed
```

Keep the response compact. A usable first rescue pack beats a comprehensive but unreadable review.
