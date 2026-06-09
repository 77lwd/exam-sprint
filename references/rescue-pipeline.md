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

3. **Build a Task Board**
   - Convert the strongest rescue units into 3-5 concrete task cards.
   - Prefer exact tasks from the user's materials: file name, page number, exercise number, visible example, worksheet item, screenshot, or answer-key item.
   - If only chapter titles are visible, create fallback mini drills but label them as fallback rather than source questions.
   - Each task card should contain:
     - `source`: where the student opens the material.
     - `why_now`: why this is the next best score move.
     - `question_type`: what kind of exam task it trains.
     - `first_line`: the first line, first formula, or first decision to write.
     - `stop_point`: where the student should stop before checking.
     - `self_check`: one concrete check for whether the attempt is on track.
     - `next_if_stuck`: what to send back, such as a photo of the first line or a screenshot of the page.
   - Do not let a material-first answer end with only "review Chapter X" or "practice topic Y" when task-level evidence exists.

4. **Choose the Subject Playbook**
   - Use `references/course-types.md` to classify the scoring type.
   - Then load `references/subject-playbooks.md` for the matching rescue style.
   - Let the playbook control default artifacts and practice format.

5. **Create the First Rescue Pack**
   - Use `references/rescue-output-patterns.md`.
   - Include symbol decoding before formula tables.
   - Include one micro-example or a partially solved example.
   - Include a first 30-90 minute task if exam time is unknown.
   - Put the Task Board near the top so the student can act before reading all explanations.

6. **Self-Review Before Final**
   - Use `references/self-review-rubric.md`.
   - Fix critical failures before replying: unexplained symbols, no first action, no task board when materials contain exercises/examples, unsupported claims, or invented study time.

7. **Iterate**
   - If the student attempts questions, switch to answer checking and mistake repair.
   - If the student gives remaining time, add Sprint Planning Mode after the rescue pack.
   - If the student asks for complete extraction, switch to Deep Scan Mode.

## Output Contract

For a first pass from materials, prefer this shape:

```text
Material Signal
Rescue Skeleton
Task Board
First Topic To Learn
Symbol Decoder
How To Recognize This Question
Do-This Template
Micro-Example
Now Practice
Common Traps
Missing Info Needed
```

Keep the response compact. A usable first rescue pack beats a comprehensive but unreadable review. A task board the student can open and start is better than a polished chapter summary.
