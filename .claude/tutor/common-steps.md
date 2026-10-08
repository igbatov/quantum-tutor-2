# Common steps for the /explain-* setups

Every setup is run by the main session as orchestrator. You never write the explanation yourself; subagents do. Subagents don't see this conversation, so everything they need goes into the run folder or the delegation message. Read only verdict lines and summaries from their files, not whole reviews, to keep your context small.

## A. Set up the run

1. Run id: `YYYYMMDD-HHMMSS-short-slug` (2–4 words from the topic). `mkdir -p work/<id>`.
2. Classify the learner's message: `new-question`, `follow-up`, `check-answer` (answering the previous "Check yourself" question), `another-angle`, `simpler`, `deeper`.
3. Write `work/<id>/request.md`:

   ```markdown
   # Request
   ## Learner's message (verbatim)
   ...
   ## Mode
   new-question | follow-up | check-answer | another-angle | simpler | deeper
   ## Setup
   explain | multi | parallel | debate | teachback
   ## Level override
   none | conceptual | intermediate | technical   (only if the learner asked)
   ## Context from this conversation
   - Previous run: work/<previous-id>/final*.md (or "none")
   - Previous check question: "..." (or "none")
   - Anything else the learner said that matters (course, notation, goals)
   ```

   For `another-angle`, `simpler`, `deeper` and `check-answer` the previous run's path is required.

## B. Judge candidates (when a setup produced several)

Delegate to **student**, `mode: judge`, naming the candidate files. It writes `judgement.md` with `WINNER`, `MARGIN` and `FINALISTS`. Read those three lines and the "Notes for the learner" section. The finalists are what you continue with; a single finalist means the student was sure, several mean it wasn't and the learner will choose.

## C. Review, verify and revise each finalist

For every finalist `<letter>`, in the same turn so they run in parallel:

- **physics-critic**, `mode: review`, file `candidate-<letter>.md` → `review-physics-<letter>.md`
- **math-verifier**, file `candidate-<letter>.md` → `verify-<letter>.md`, `checks/`, `figures/`

Never skip the verifier when a candidate contains an equation, a number, or a figure request. (The student judge already assessed clarity, so its "Notes for revision" replace a separate clarity review here. In the baseline `/explain` setup, which has no judge, run **student** `mode: review` as well.)

Decide per finalist with `grep -E "^VERDICT|^- \[(critical|major)\]|FAIL" work/<id>/review-*-<letter>*.md work/<id>/verify-<letter>*.md`:

- All `ship`, no critical/major, no `FAIL`, no unfulfilled figure request → copy the candidate to `final-<letter>.md` unchanged.
- Otherwise → **qm-explainer**, `mode: revise`, naming the candidate and the output `final-<letter>.md`. Several finalists revise in parallel.

Re-check at most once: if a finalist's round one had a `critical` item or a `FAIL`, run physics-critic and math-verifier again on `final-<letter>.md` (`-2` files). Still failing → one more revise, then stop and tell the learner in one sentence what stayed uncertain. Never more than two revisions per finalist.

## D. Render and present

1. `python3 scripts/render.py work/<id>/final-<letter>.md` for each finalist (writes `answer-<letter>.html`).
2. One finalist: show `final-<letter>.md` in full, unchanged, then:

   ```
   Checked: <n> physics fixes, <n> clarity fixes, <passed>/<total> computational checks passed.
   Setup: <name>. Figures: work/<id>/figures/... Rendered: work/<id>/answer-<letter>.html
   ```

3. Several finalists: say in one sentence that the student agent couldn't pick a clear winner, so the learner chooses. Then show each finalist in full under a heading `## Explanation <letter>: <strategy name>` followed by the student's one-line note for it. Add the Checked block once, with per-finalist counts, and the rendered paths. Then ask the learner which explanation they prefer; use the AskUserQuestion tool when it is available. When they answer, write `work/<id>/choice.md` with `CHOSE: <letter> (<strategy>)` and `OVER: <letters (strategies)>`, plus any reason they gave.

Don't paste reviews, judgement or scripts unless the learner asks.

## E. Update the learner model

Delegate to **learner-modeler** with the run folder and the chosen or only final file. With several finalists, do this after the learner has chosen, so `choice.md` exists. Its result isn't needed before you reply.

## F. Failure handling

- If a subagent fails, continue with the rest and say in the Checked block which step was skipped.
- Missing `python3` or packages: tell the learner to run `pip install -r requirements.txt`; continue without verification and say so.
- If the learner wrote `quick:` before the question, skip the pipeline and answer directly using the quantum-explainer skill.
