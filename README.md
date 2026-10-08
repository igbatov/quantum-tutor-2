# Quantum tutor for Claude Code

A team of Claude Code subagents that explain quantum mechanics. Several candidate explanations are written along different routes, a student agent modelled on you judges them, and the finalists are reviewed by a physicist, checked by running real code, and revised. When the student agent can't pick a clear winner, you see all finalists and choose. Your choices are remembered and shape later explanations.

## The team

| Agent | Model | Role |
|---|---|---|
| qm-explainer | `fable`, effort max | Plans strategies, writes candidates, critiques rivals, revises |
| student | `opus` | Plays you: reviews clarity, judges candidates, sits probe exams |
| physics-critic | `opus` | Accuracy review; writes and grades probe exams |
| math-verifier | `opus` | Turns every equation and number into a sympy/numpy check; draws figures |
| learner-modeler | `haiku` | Keeps `learner/profile.md` and `learner/history.md` |

All setups share this team and the procedure in `.claude/tutor/common-steps.md`. If your plan or organization doesn't allow a model or effort level, Claude Code substitutes; edit the `model:` and `effort:` lines in `.claude/agents/` to suit your budget.

## The setups

Each is a slash command. They differ in how candidates are produced and how the winner is chosen.

| Setup | Candidates | Selection | Writer runs | When to use |
|---|---|---|---|---|
| `/explain` | 1 draft | none | 1 | Baseline; cheapest |
| `/explain-multi` | 3, one writer plans ≥6 routes and writes the 3 most different | student judge | 1 | Good default on a budget; candidates can share blind spots |
| `/explain-parallel` (default) | 3, planned once, written by 3 independent writers | student judge | 4 | Most diverse candidates for the cost |
| `/explain-debate` | 2, each critiques the other, both revise | student judge | 6 | Subtle or contested topics: measurement, Bell, interpretations |
| `/explain-teachback` | 3 independent | probe exam: a student agent reads only one candidate, answers a physicist's exam, best score wins | 4 (+5 exam runs) | When you want selection by what the explanation lets you *do*, not how it reads |
| `/explain-bakeoff` | runs several setups | you | many | Comparing the setups themselves |

In every setup except `/explain`, the judge (or the exam) keeps every candidate it can't clearly beat the best with, so you may be shown two or three finalists and asked to pick. The pick is recorded in `learner/profile.md`; after a few consistent picks the planner favours your preferred style.

## Setup

```bash
pip install -r requirements.txt
cd quantum-tutor
claude
```

Accept the workspace trust prompt so the project's agents and settings load. `.claude/settings.json` pre-approves `python3` and `mkdir`. Answers write several files per run; a permission mode that auto-accepts edits avoids approving each one.

## Use

- Ask a question normally (goes to `/explain-parallel`), or name a setup: `/explain-debate why can't entangled particles send messages?`
- Answer the **Check yourself** question at the end of each answer; it's graded and the notes update.
- Say "another angle", "simpler" or "more math" for a different version of the last answer.
- Start with `quick:` for a fast single-pass answer with no team.
- `/progress` shows what the tutor knows about you, including which explanation styles you've preferred.
- Edit `learner/profile.md` by hand any time (goals, course, notation, preferences). Your edits win.
- To change the default setup, edit the first bullet of `CLAUDE.md`.

## Cost and time

`/explain-parallel` makes roughly 8–12 subagent calls per question (one plan, three drafts, one judge, then review, verification and revision per finalist). Expect several minutes and far more usage than a chat reply. `/explain-debate` and `/explain-teachback` cost more; `/explain-bakeoff` runs everything. Use `quick:` or `/explain` for simple questions.

## Files

```
CLAUDE.md                          project instructions for the main session
.claude/tutor/common-steps.md      procedure shared by all setups
.claude/skills/explain*/           the six setups
.claude/skills/progress/           /progress
.claude/skills/quantum-explainer/  explanation standard, preloaded into the explainer and physics critic
.claude/agents/                    the five subagents
.claude/settings.json              permission allow rules
learner/                           the tutor's notes about you
scripts/render.py                  Markdown + LaTeX to HTML (final-A.md -> answer-A.html)
work/                              one folder per answer (git-ignored):
                                   request.md, strategies.md, candidate-*.md, judgement.md,
                                   review-*.md, verify-*.md, checks/, figures/, exam*.md,
                                   final-*.md, answer-*.html, choice.md
```
