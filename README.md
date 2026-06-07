# Exam Sprint

期末突击复习助手，一个面向大学生的 Codex skill。它帮助学生把课件 PDF、课堂笔记、往年题、作业、老师划重点等零散资料，整理成可以立刻执行的期末突击复习路线、考点优先级、速记清单和自测陪练。

## What It Does

Exam Sprint 关注真实期末场景：资料不完整、时间紧、课件很多、重点不清楚。它不会假设用户已经准备好完整信息，而是先基于已有资料建立复习地图，再按考试收益排序。

核心能力：

- 处理一堆课件 PDF 或零散资料
- 识别课程结构和章节模块
- 判断课程的复习类型组合
- 按考试概率、分值、提分效率和资料证据排序考点
- 生成 24 小时、3 天或 7 天突击复习计划
- 输出一页纸速记、公式/定义/流程清单
- 生成自测题并根据错误进行回补
- 生成考前 20 分钟速记页

## Use Cases

适合这些提问：

```text
用 exam-sprint 帮我根据这些课件做期末突击复习计划。
```

```text
我把课件 PDF 都传给你了，先帮我判断哪些最重要。
```

```text
明天考计算机组成原理，我只剩 8 小时，帮我保命。
```

```text
根据这些资料给我生成一页纸速记和 10 道自测题。
```

## Design

这个 skill 使用三个核心框架：

1. 课程类型框架  
   不按专业分类，而按考试得分方式分类。支持计算推导型、概念理解型、记忆背诵型、技能实践型、语言表达型、开放综合型，并允许混合比例。

2. 优先级规则  
   不按章节顺序平均复习，而按考试概率、分值、提分效率、基础依赖和资料证据进行排序。

3. PDF Dump Workflow  
   面向“一堆课件 PDF”的真实场景，先盘点资料、提取课程骨架、判断课程类型、排序考点，再生成复习材料。

## Installation

把本仓库放入 Codex skills 目录即可：

```powershell
mkdir $env:USERPROFILE\.codex\skills
git clone https://github.com/YOUR_USERNAME/exam-sprint.git $env:USERPROFILE\.codex\skills\exam-sprint
```

如果你已经有这个目录，也可以手动复制：

```text
exam-sprint/
  SKILL.md
  agents/
    openai.yaml
  references/
    course-types.md
    priority-rules.md
    pdf-dump-workflow.md
```

安装后重启 Codex 或开启新对话，让 skill metadata 重新加载。

## Project Structure

```text
exam-sprint/
  SKILL.md
  agents/
    openai.yaml
  references/
    course-types.md
    priority-rules.md
    pdf-dump-workflow.md
```

## Notes

Exam Sprint 优先使用用户提供的课件、笔记、题库和老师重点。内置 references 只提供复习方法论，不会替代具体课程资料，也不会承诺考试分数。

## License

No license has been selected yet. Add a LICENSE file before publishing if you want others to reuse or modify this project.
