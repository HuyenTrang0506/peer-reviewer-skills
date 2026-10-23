# From course outline to reviewer methodology

This repository translates the supplied reviewer-training screenshots and inspected public guidance into two standalone skills: journal reviewing and conference reviewing. The screenshots establish training topics; they do not document how an individual reviewer actually performed a review. The method below is a proposed synthesis of guidance and methodological reasoning, not an observational study of reviewers.

## Analysis of the supplied material

| Course content | Operational implication |
| --- | --- |
| Purpose, publishing context, editorial process | Establish the assignment and limits of reviewer authority. |
| Review models; internal versus external review | Determine identity/confidentiality rules; distinguish editorial triage from scientific assessment. |
| Author, editor, and reviewer roles | Authors supply and revise; reviewers advise; editors decide. |
| Constructive, critical, objective author comments | Require evidence, reasoning, and actionable requests. |
| Article types, ethics, methods, design, results, data presentation, references | Adapt appraisal to study design and discipline. |
| Title, abstract, introduction, discussion, summary | Check coherence with actual evidence and contribution. |
| Confidential editor comments | Separate recommendation and genuinely confidential matters from author feedback. |
| Accept, reject, minor revision, major revision | Justify advice through consequences and remediability of findings. |

The initial screenshots supplied Sections 1 and 3. Additional slides now explicitly identify Elsevier Researcher Academy and cover publishing functions, journal process, reviewer qualities, and NISO/STM terminology. The course date, author, full content, and missing Section 2 remain unverified. No missing section is reconstructed as fact. Publishing history and recruitment are useful context but need not dominate operational instructions.

The slide's placement of language/grammar and general impressions under editor comments should not become a blanket rule: ordinary scientific and clarity criticisms belong where authors can respond. Its mention of a commercial language service is not a reason to require that service.

## The missing reasoning layer

A report outline says where comments go. A reviewing method explains how to decide whether a concern is real, important, and repairable.

**Assignment → manuscript map → claim/evidence appraisal → issue triage → constructive report → human verification.**

Reading need not follow the printed section order. A useful first pass establishes the question and claims; another examines methods and results together; a final pass tests consistency and interpretation. Reviewers may loop back as their understanding changes. The PLOS guidance recognizes different reviewing methods; Wong et al. (2025) recommend a complete broad reading followed by a detailed reading. Our passes implement that flexibly, not as a shortcut to reviewing excerpts while claiming full coverage; see [source notes](journal-peer-reviewer/references/sources.md).

For each potential concern, answer:

1. What exactly does the manuscript say, and where?
2. What evidence or methodological criterion creates the concern?
3. Is this an observed problem, insufficient reporting, or an unresolved question?
4. Which conclusion or reader judgment would change if it were addressed?
5. What is the smallest adequate author response?

An unreported allocation method supports a request for clarification. It does not establish that allocation was nonrandom. An analysis demonstrably treating repeated observations from one subject as independent raises a different concern about inference. The skill must preserve that distinction.

## Working artifacts

| Artifact | Purpose | Included in author report? |
| --- | --- | --- |
| Assignment record | Scope, policy, conflicts, competence, materials, versions | Relevant scope limits only |
| Manuscript map | Neutral question, design, claims, strengths | Concise summary |
| Claim/evidence map | Trace central conclusions to actual support | Referenced when useful |
| Issue ledger | Evidence, uncertainty, consequence, remedy, priority | Selected findings rewritten as comments |
| Author report | Scientific feedback and proportionate requests | Yes |
| Editor note | Recommendation, rationale, confidential matters | No; follow venue routing |

These are working aids, not a numerical quality score. A complete checklist does not establish validity; an incomplete checklist alone does not establish invalidity.

## Essential distinctions

- **Reporting versus conduct:** “not reported” does not mean “not done.”
- **Validity versus novelty:** reliable evidence may be confirmatory; novelty alone cannot repair a flawed inference. Venue criteria differ.
- **Observed flaw versus uncertainty:** distinguish demonstrated problems from questions needing clarification or specialist assessment.
- **Essential revision versus future research:** ask for work necessary to support current claims; label extensions as optional.
- **Statistical significance versus evidential value:** assess estimates, uncertainty, design, and precision rather than a threshold alone.
- **Recommendation versus decision:** the reviewer advises; the editor determines the outcome.
- **Inspection versus reproduction:** reading code is not running it, and running it does not validate the whole study.
- **Scientific criticism versus integrity allegation:** explain scientific concerns to authors; route evidence-based integrity concerns privately without accusation.

## Skill architecture

```text
journal-peer-reviewer/
├── SKILL.md                         Journal entry point
├── agents/openai.yaml               Discovery metadata
├── references/journal-workflow.md   Journal procedure and decision channels
├── references/worked-example.md     Journal review and re-review example
├── assets/review-report.md          Author/editor report
└── references/ and assets/          Shared appraisal, standards, enrichment, diagnostics
conference-peer-reviewer/
├── SKILL.md                         Conference/year/track entry point
├── agents/openai.yaml               Discovery metadata
├── references/conference-workflow.md
├── references/worked-example.md     Conference review and rebuttal example
├── assets/review-report.md          Rubric, confidence, response/discussion update
└── references/ and assets/          Local copies of shared resources
scripts/sync_shared_resources.py     Maintain identical shared resources
tests/test_shared_resources.py       Sync invariants
COMMIT_PLAN.md                      User-run incremental commit commands
```

Each skill is self-contained and can be installed alone; there are no sibling-file dependencies. Shared references are authored in `journal-peer-reviewer/` and copied into the conference package by the explicit allowlist in `scripts/sync_shared_resources.py`. Edit common resources there, then run `python3 scripts/sync_shared_resources.py --write`; `--check` detects drift without writing. Venue-specific entry points, workflows, report templates, metadata, and examples are never synchronized. The script supports packaging consistency, not scientific judgment.

## Journal and conference are separate contracts

| Aspect | Journal skill | Conference skill |
| --- | --- | --- |
| Context | Journal, article type, scope, round, decision policy | Conference edition/year, track, submission type, stage, exact form |
| Main output | Author report plus editor-facing advice | Venue-form review with rubric/overall/confidence fields if requested |
| Revision | Actual response and revised manuscript against stable IDs | Author response, permitted evidence/revisions, and score/reason updates within policy |
| Recommendation | Actual journal categories; usually editor channel | Actual track scale/category and readership; no invented major-revision option |
| Interaction | Editor and other parties as allowed | Author/peer/AC/PC discussion only as permitted for the stage |

These are routing distinctions, not rigid claims that all journals or conferences share one process. OpenReview alone does not determine the destination. Journal-linked conference tracks require their specific rules. ICLR 2026 and NeurIPS 2025 provide inspected examples, not universal conference standards.

## Terminology and domain knowledge

[ANSI/NISO Z39.106-2023](journal-peer-reviewer/references/peer-review-standards.md) defines identity transparency, reviewer interaction, published review information, and post-publication commenting. Its 2023 scope is external journal-article review; scientific criteria and acceptance governance are excluded. The conference skill uses those dimensions descriptively, without claiming NISO prescribes conference procedure. The standard's STM origins are verified through NISO; the STM web endpoint itself was inaccessible.

The skills proactively [enrich domain knowledge](journal-peer-reviewer/references/domain-enrichment.md) when a specific gap matters. They inspect relevant local resources, search generic public terms, download suitable public skill text as task-local references, preserve provenance/license, and verify consequential advice against primary methodological sources. Downloading reference material does not authorize executing it or exporting confidential content. This adds knowledge without claiming professional competence or silently imposing another skill's tools and behavior.

## Readiness and limits

The repository contains two standalone skills, common claim-specific appraisal guides, separate complete fictional workflows, and twelve diagnostic excerpts in six matched pairs with a separate key and evaluation protocol. Venue-routing scenarios supplement the core diagnostics. Public implementations, the PMC article, standards, conference-policy examples, and their access limitations are recorded in source notes.

It has not reviewed an actual manuscript, been validated against editor ratings, or demonstrated improvement in reviewer performance. The diagnostic evaluation is prepared but not run; author-written cases are not independent expert gold. Future evaluation must examine both detection and restraint using unseen authorized material, not just count how many criticisms a model emits.

Adapt the workflow to the actual discipline and venue. It is not a claim that all real reviewers use one empirically established procedure.
