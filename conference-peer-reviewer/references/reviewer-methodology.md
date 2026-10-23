# Reviewer methodology

## 1. Establish scope

Record venue, article type, review round/model, requested questions, deadline where relevant, conflicts, expertise, authorization, AI/tool permission, confidentiality, and retention rules. Single, double, and triple anonymized review and open practices vary between venues: record who sees identities and whether reports are published rather than assume a universal implementation.

Use [the standards reference](peer-review-standards.md) for precise terminology and [domain enrichment](domain-enrichment.md) for an identified expertise gap. A reference search can support a review but cannot confer professional expertise or resolve a conflict of interest. Decline or request specialist review if the central assignment cannot be completed competently and on time; the assistant does not send that message without authorization.

Submission commonly passes administrative checks and editorial triage before external review. Do not assume these verified the science, ethics, references, or data. Inventory manuscript/supplement versions, protocols/registrations, availability statements, instructions, and prior reports/response letters. Record missing materials and limits of a focused review.

## 2. First pass: understand before judging

Read the abstract, question, study overview, main results/figures, and conclusions in a useful order. Capture the research question, contribution, design, population/system, sample, independent unit, comparator, outcomes, timing, central claims, and supported strengths. Identify evidence needed to evaluate each claim.

Write a neutral summary the authors would recognize. Defer the publication recommendation. Do not declare novelty without an adequate literature check; say when that check is outside scope.

## 3. Second pass: test the inference

Read methods and results together. Follow each central claim from question to design, measurement, analysis, result, and interpretation.

| Area | Questions that can change the assessment |
| --- | --- |
| Design | Can it answer the question? Is the independent unit correct? Are controls, comparators, and temporal order appropriate? |
| Sampling/allocation | What population is represented? Could selection, confounding, masking, clustering, or attrition affect the claim? |
| Measurement | Are outcomes and instruments appropriate? Are timing, denominators, and measurement errors clear? |
| Analysis | Does it respect dependence, missingness, assumptions, multiplicity, and prespecification? Are estimates and uncertainty interpretable? |
| Results | Are analyses traceable to methods? Are exclusions, null results, harms, and deviations reported as applicable? |
| Interpretation | Are causal, mechanistic, diagnostic, predictive, or generalization claims supported? Are alternatives considered? |
| Transparency | Are protocol, data, code, software, materials, and restrictions sufficiently described? |
| Ethics | Are applicable approval, consent, welfare, privacy, funding, sponsor role, and conflicts reported? |

Assess sample-size rationale and achieved precision; do not demand retrospective observed power. A small study can be informative with bounded conclusions. Request specialist review when a pivotal method exceeds competence.

### Route by study type

| Study | Priority checks | Reporting guidance to locate and verify |
| --- | --- | --- |
| Randomized trial | Allocation/concealment, masking, estimand, attrition, harms | CONSORT and extensions |
| Observational | Selection, confounding, time-related bias, causal limits | STROBE and extensions |
| Systematic review/meta-analysis | Search, eligibility, selection, risk of bias, synthesis, heterogeneity | PRISMA and extensions |
| Diagnostic accuracy | Patient spectrum, reference standard, thresholds, blinding | STARD and extensions |
| Prediction | Leakage, validation, overfitting, calibration, discrimination | Applicable TRIPOD guidance, including AI guidance where relevant |
| Qualitative | Methodological coherence, sampling rationale, reflexivity, evidentiary grounding | SRQR or COREQ as applicable |
| Animal | Experimental unit, randomization, masking, exclusions, welfare | ARRIVE |
| Computational/ML | Split independence, leakage, baseline/tuning fairness, uncertainty, provenance | Venue/domain guidance; health standards only where applicable |
| Theory/mathematics | Assumptions, proof/argument, boundary cases, prior results | Discipline and venue conventions |

This is a routing aid, not an exhaustive checklist or assurance that any edition is current. Verify the current base guideline, extensions, and venue requirements. Do not impose health-specific standards on unrelated fields. Reporting coverage does not establish validity or replace risk-of-bias appraisal.

## 4. Third pass: reconcile the paper

Check title/abstract against actual outcomes, effect sizes, uncertainty, and limitations. Does the introduction motivate the question and represent relevant prior work fairly? Does the discussion distinguish findings from speculation and avoid extending conclusions beyond the sample/design?

For figures/tables, inspect units, axes, scales, denominators, uncertainty definitions, legends, and text agreement. A visual anomaly is a question, not proof of manipulation. Check whether pivotal citations support the associated claims; distinguish reference consistency from external source verification. Do not compel self-citation.

Check whether the venue requires, permits, or limits supplement review. Inspect available authorized relevant supplements before asserting that information is absent from the submission. If unable to inspect them, state that limit. Record what was checked rather than imply comprehensive verification. A venue may not require reading every supplement; do not turn this evidence check into an invented universal obligation.

## 5. Triage by consequence and remedy

Classify the finding first:

- **Observed problem:** identifiable contradiction, analysis error, or unsupported inference.
- **Reporting gap:** information needed for appraisal is absent from reviewed material.
- **Unresolved question:** evidence or competence is insufficient to conclude.
- **Optional improvement:** useful but unnecessary for current central claims.

Then assign priority:

- **Major:** resolution could change a central inference, its uncertainty, ethical acceptability, or ability to evaluate the work. A missing explanation can be major without proving flawed conduct.
- **Minor:** localized correction/clarification with limited effect on the main conclusion.
- **Optional:** suggestion explicitly distinguished from publication requirements.

Priority and remediability are separate. A major issue may be fixed by explanation or reanalysis. A design limitation may require claim narrowing or may prevent the central contribution altogether. Never choose a recommendation by counting major comments.

Maintain a private ledger; merge duplicate manifestations of one problem. Remove unsupported concerns. Express unresolved matters as bounded questions rather than facts.

## 6. Convert findings into comments

Use **location → observation/evidence → scientific consequence → requested action**. Give an adequate lower-burden alternative where possible.

Fictional example: “Methods §2.4 and Figure 3: the methods describe three wells per donor, while the legend reports n = 30 without identifying the independent unit. If wells from one donor were treated as independent, uncertainty may be understated. Please identify donor and well counts and explain how dependence was handled; if necessary, reanalyze with an appropriate donor-level or multilevel approach and update the intervals.”

This is a reporting question and a conditional analysis concern, not a finding that pseudoreplication occurred. A direct finding would require inspecting the analytical specification or code.

Avoid “the statistics are wrong,” “perform more experiments,” or “improve the English” without evidence and purpose. Narrowing a causal claim to an association may suffice. New experiments should be necessary for a retained central claim and proportionate to scope, rather than a request to conduct the reviewer's preferred study.

## 7. Draft and recommend

Start with a neutral summary and supported strengths. Prioritize major issues, then localized corrections. Follow the venue's form rather than impose an exact layout.

The selected venue skill controls report structure, rubric, recommendation categories, channels, and opportunities for revision. Do not carry a journal revision category into a conference form that does not offer it. For journals, typical categories, subject to venue definitions, are:

- **Accept:** no substantive required changes identified within scope.
- **Minor revision:** limited changes unlikely to alter central interpretation.
- **Major revision:** substantial but plausibly addressable issues; explain what must be resolved.
- **Reject:** central problems cannot reasonably be remedied within the submitted study, or an applicable venue criterion is unmet; explain why.

Missing expertise/materials may require a provisional assessment or specialist request. Reviewer advice is not the editor's decision. Confidential notes may include recommendation, fit, conflicts, competence, disclosures, and evidence-based integrity/process concerns. Ordinary scientific reasons also belong in author comments.

## 8. Re-review revisions

Use stable comment IDs. Locate each response and actual manuscript change; mark resolved, partly resolved, unresolved, or no longer applicable, with reasons. A reasoned disagreement can resolve a comment without the authors performing the originally requested action.

Check consequential new problems introduced by changes. Avoid a new wish list or unjustified moving of acceptance criteria. Explain newly discovered central issues transparently. Update the recommendation from remaining evidence, not author agreeableness.

## 9. Verify the handoff

Confirm traceable locations, bounded claims, proportional requests, priority, tone, disclosure, channel separation, and scope limits. The human verifies scientific judgment and the final report. A format check does not establish review quality.
