# Exam Sprint

Version: 1.1

Exam Sprint 是一个面向大学期末突击复习的 Codex skill。它把课件 PDF、课堂笔记、往年题、作业、老师划重点和零散截图整理成可执行的复习路线、考点优先级、速记清单和自测陪练。

## What It Does

- 盘点课程材料并识别课程模块。
- 按考试得分方式分类课程，例如计算推导、概念理解、记忆背诵、实践技能、语言表达和开放综合。
- 按考试可能性、分值、提分效率、前置价值和材料证据排序考点。
- 输出 24 小时、3 天、7 天或自定义周期的冲刺计划。
- 生成一页速记、公式/定义/流程清单、自测题和错题修复路线。
- 在扫描版 PDF 场景下优先快速诊断，避免默认长时间卡在 OCR 或文件恢复上。

## Version 1.1 Highlights

- 新增 Sprint Mode 和 Deep Scan Mode。
- 新增扫描版 PDF 的快速处理规则。
- 新增 `scripts/pdf_probe.py`，用于快速判断 PDF 是可读文本、混合版、扫描优先还是不可读。
- 新增 provisional 材料地图输出策略，证据不足时先给可用战况板，再请求 1-3 个高价值补料。
- 新增可选 probe 缓存，方便反复测试同一份 PDF。

See [CHANGELOG.md](CHANGELOG.md) for release notes.

## Installation

Clone this repository into your Codex skills directory:

```powershell
mkdir $env:USERPROFILE\.codex\skills -Force
git clone https://github.com/77lwd/exam-sprint.git $env:USERPROFILE\.codex\skills\exam-sprint
```

If the directory already exists, update it with:

```powershell
cd $env:USERPROFILE\.codex\skills\exam-sprint
git pull
```

Restart Codex or start a new conversation so skill metadata is reloaded.

## Project Structure

```text
exam-sprint/
  SKILL.md
  VERSION
  CHANGELOG.md
  agents/
    openai.yaml
  references/
    course-types.md
    priority-rules.md
    pdf-dump-workflow.md
  scripts/
    pdf_probe.py
```

## Notes

Exam Sprint 优先使用用户提供的课程材料。内置 references 只提供复习方法论，不替代具体课程资料，也不承诺考试分数。
