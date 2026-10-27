# From course outline to reviewer methodology

This repository translates the supplied reviewer-training screenshots and inspected public guidance into two standalone reviewer skills: journal reviewing and conference reviewing. A small companion skill handles professional language for review comments and office documents. The screenshots establish training topics; they do not document how an individual reviewer actually performed a review. The method below is a proposed synthesis of guidance and methodological reasoning, not an observational study of reviewers.

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

The initial screenshots supplied Sections 1 and 3. Additional slides now explicitly identify Elsevier Researcher Academy and cover publishing functions, journal process, reviewer qualities, and NISO/STM terminology. The course date, author, full content, and complete Section 2 remain unverified. No missing section is reconstructed as fact. Publishing history and recruitment are useful context but need not dominate operational instructions.

The slide's placement of language/grammar and general impressions under editor comments should not become a blanket rule: ordinary scientific and clarity criticisms belong where authors can respond. Its mention of a commercial language service is not a reason to require that service.

## The missing reasoning layer

A report outline says where comments go. A reviewing method explains how to decide whether a concern is real, important, and repairable.

**Assignment → manuscript map → claim/evidence appraisal → issue triage → constructive report → human verification.**

Reading need not follow the printed section order. A useful first pass establishes the question and claims; another examines methods and results together; a final pass tests consistency and interpretation. Reviewers may loop back as their understanding changes. The PLOS guidance recognizes different reviewing methods; Wong et al. (2025) recommend a complete broad reading followed by a detailed reading. Our passes implement that flexibly, not as a shortcut to reviewing excerpts while claiming full coverage; see [source notes](journal-peer-reviewer/references/appendices/sources.md).

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

### Rule architecture

Both entry points separate rule classes before presenting the staged workflow.
The shared [rulebook](journal-peer-reviewer/references/01-foundations/rulebook.md) gives stable
IDs, applicability triggers, obligations, and recovery actions:

- **H1–H8: hard rules.** Authorization, evidence integrity, coverage honesty,
  role boundaries, fair critique, proportionate requirements, reasoned assessment,
  and honest human handoff are required when their triggers apply.
- **V1–V4: venue-conditional requirements.** Criteria/form, materials, audiences
  and interaction, assistance and retention become binding through actual
  applicable policy. Unknown policy limits the dependent action rather than
  producing an invented rubric or stopping unrelated public guidance.
- **S1–S5: soft defaults.** Reading passes, working-note layout, report structure,
  search budget, and limited copyediting can adapt to the assignment. Only
  changes materially affecting coverage or interpretation need explanation.

This is a local operational classification, not terminology prescribed by NISO
or STM. For example, whole-paper coverage is required before claiming a full
review (H3), supplement obligations depend on the assignment (V2), and reading
order remains flexible (S1). Constructive critique does not prohibit a negative
recommendation; it requires evidence and professional, answerable reasons (H5/H7).
Necessary references can include a reviewer's work; coercive or irrelevant
self-citation is prohibited (H5). Additional experiments require a reason tied to
retained claims or applicable criteria, with bounded alternatives considered
(H6); future-research suggestions remain optional (S5).

Procedural references supply implementation guidance rather than extra absolute
requirements. The workbook records applicable rules, policy provenance, affected
actions, and material adaptations without requiring a style-deviation audit.

```text
common/                                Canonical reusable chapters, rules, forms and cases
journal-peer-reviewer/                  Standalone journal handbook
conference-peer-reviewer/               Standalone conference handbook
  SKILL.md                             Entry point, rule classes, essential gates
  agents/openai.yaml                   Discovery metadata
  references/
    CONTENTS.md                        Venue-specific contents and reading routes
    01-foundations/                    Chapters 1–3: rules, standards, assignment
    02-appraisal/                      Chapters 4–7: method, sections, domains, enrichment
    03-reporting/                      Chapters 8–9: adjudication and report writing
    04-review-rounds/                   Chapter 10: venue-specific worked follow-up
    appendices/                        Sources, evaluation protocol and answer key
  assets/                              Forms and development datasets
professional-office-language/          Small standalone wording skill (LANG rules)
scripts/sync_shared_resources.py        Export common resources into skill packages
tests/test_shared_resources.py          Sync invariants
COMMIT_PLAN.md                          Suggested message and user-run commit steps
```

Each skill is self-contained and can be installed alone; there are no sibling-file dependencies. Shared references are authored in `common/` and exported into both reviewer packages by the explicit allowlist in `scripts/sync_shared_resources.py`. The same LANG reference is also exported into the office-language skill. Edit common resources there, then run `python3 scripts/sync_shared_resources.py --write`; `--check` detects drift without writing. Venue-specific entry points, contents pages, workflows, report templates, metadata, and examples are never synchronized. These exported copies are packaging artifacts: maintain one source in `common/`,
while each installed skill remains self-contained without sibling dependencies.
The script reads all canonical inputs before writing, detects drift in either
reviewer package or the language export, and leaves venue-specific files alone.
It supports packaging consistency, not scientific judgment.

The book organization is functional: Chapter 5 adds article-type and
section-by-section appraisal; Chapter 9 turns adjudicated findings into a report.
The new supplied checklist/structure slides support these topics, with caveats:
novelty depends on article type and venue, checklist coverage is not validity,
and major/minor priority depends on scientific consequence rather than a slide's
example label. Overview, strengths, and comment ordering are presentation defaults;
venue-specific forms still govern outputs. See the local contents pages for all
chapter links. Evaluation appendices remain separate from ordinary review.

### Small reusable rule modules

FIG, READ, LANG, INT and REV modules provide granular IDs, explicit rule classes,
applicability, and recovery. Display rules cover actual visual inspection,
quantities/units, legends/colorbars, uncertainty and independent units,
text/display correspondence, readability, overplotting and bounded integrity
concerns. READ separates scientific ambiguity from imperfect but understandable
language; LANG preserves facts and intent while improving professional wording.
INT separates observed overlap from allegations and automatic-rejection shortcuts.
REV distinguishes narrative, systematic, scoping and meta-analytic synthesis,
checks faithful source representation and consensus versus author interpretation,
and assesses contribution against audience and venue. It does not transfer a
primary-research experiment checklist to every review or waive assessment of
methods/statistics for a literature synthesis. The review format also governs the expected referencing rigor and editorial
stance: a perspective, focused trends update and systematic synthesis have
different evidence/coverage obligations. Actual format limits guide proportionate
remedies without excusing inaccurate claims. An opening summary is optional unless
the form requires one. Co-review permission and availability for re-review are
recorded separately from scientific judgment; inability to return does not change
the need for another check. These modules do not impose every domain-specific
check on every paper.

The office-language skill uses LANG without requiring either reviewer package.
It drafts and edits wording; it does not verify scientific findings, modify a
submission by default, contact recipients or prescribe paid language services.
The same language reference is generated into all three packages from one source.

The added training material also motivates checking methods/results in both
directions, abstract/main-text consistency and discussion/claim alignment.
Minor versus major revision remains venue-specific: not needing re-review is
only a heuristic, not a universal definition. Required versus optional action is
separate from issue priority, and confidentiality/readership follows real policy.

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

[ANSI/NISO Z39.106-2023](journal-peer-reviewer/references/01-foundations/peer-review-standards.md) defines identity transparency, reviewer interaction, published review information, and post-publication commenting. Its 2023 scope is external journal-article review; scientific criteria and acceptance governance are excluded. The conference skill uses those dimensions descriptively, without claiming NISO prescribes conference procedure. The standard's STM origins are verified through NISO; the STM web endpoint itself was inaccessible.

The skills proactively [enrich domain knowledge](journal-peer-reviewer/references/02-appraisal/domain-enrichment.md) when a specific gap matters. They inspect relevant local resources, search generic public terms, download suitable public skill text as task-local references, preserve provenance/license, and verify consequential advice against primary methodological sources. Downloading reference material does not authorize executing it or exporting confidential content. This adds knowledge without claiming professional competence or silently imposing another skill's tools and behavior.

## Readiness and limits

The repository contains two standalone reviewer skills, a small professional-language skill, common claim-specific appraisal guides, separate complete fictional workflows, and twelve diagnostic excerpts in six matched pairs with a separate key and evaluation protocol. Venue-routing scenarios supplement the core diagnostics. Public implementations, the PMC article, standards, conference-policy examples, and their access limitations are recorded in source notes.

It has not reviewed an actual manuscript, been validated against editor ratings, or demonstrated improvement in reviewer performance. The diagnostic evaluation is prepared but not run; author-written cases are not independent expert gold. Future evaluation must examine both detection and restraint using unseen authorized material, not just count how many criticisms a model emits.

Adapt the workflow to the actual discipline and venue. It is not a claim that all real reviewers use one empirically established procedure.
