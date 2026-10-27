# Fictional conference review and rebuttal update

This is a wholly fictional track, form, excerpt, and response. The example demonstrates process; it is not an actual conference policy, a computed result, or evidence of system performance.

## Assignment and form

The owner authorizes a mock pre-submission AI review for **Methods Meeting 2026, full-paper track**. The fictional policy permits clarifications and analyses of existing data during rebuttal but no revised PDF. The review/recommendation is visible to authors; process notes go to the AC. Overall categories are **accept / borderline / reject**, with no numerical scale and no major-revision category. Confidence categories are **limited / moderate / high**. Scope is new-patient validation; novelty and numerical reproduction are excluded.

## Submission v1

**Methods §3:** “We split 600 images from 100 patients randomly at image level; each patient appears in both training and test sets.”

**Results §4:** “AUC is 0.94 on this split.”

**Discussion §5:** “This establishes performance on entirely new patients.”

## Private finding and challenge

**C1:** Methods §3 and Discussion §5 demonstrate a mismatch between the evaluation split and the generalization claim. This is an observed problem central to the contribution. Could the held-out images nevertheless establish the stated target? No: the explicitly shared patient identities prevent that evaluation from being evidence on entirely new patients. It does not establish the direction or magnitude of any corrected score.

## Working draft — initial author-facing review

The paper reports an image classifier evaluated using images from 100 patients. The splitting procedure is described clearly, making the validation target assessable. The main concern is that this target differs from the new-patient claim.

**C1 — Methods §3; Discussion §5.** Every patient contributes images to training and test sets, while the conclusion claims generalization to patients absent from training. The reported AUC therefore does not establish that claim. Please clarify whether patient-disjoint evaluation of the existing data is available, or narrow the interpretation to the supported target. I cannot infer the corrected score from this excerpt. A new hospital study is not necessary merely to resolve this patient-overlap issue.

**Decision-relevant question:** Is an evaluation with no patient shared between fitting/tuning/testing available, with preprocessing fitted on training data only? Its procedure and results could change my assessment. If not, explain how narrowing the claim affects the stated contribution.

**Optional suggestion:** Broader external-site evaluation would be valuable future work if deployment across sites is intended; it is not a condition for resolving C1 in this track.

**Overall: reject at this stage.** C1 undermines the central validation claim as submitted. This is provisional reviewer advice under the fictional categories, not a journal major-revision decision.

**Confidence: moderate.** The split mismatch is explicit; the numerical results, novelty, and other manuscript content were not independently assessed. This is a focused mock review, not full-paper coverage.

## Permitted rebuttal

**Response C1, paragraphs 1–3:** “We used the existing cohort to conduct a patient-disjoint split, fitting preprocessing on training data and selecting settings on a separate validation group. AUC on held-out patients was 0.81. Our earlier statement described the original experiment incorrectly. We will revise Discussion §5 to restrict generalization to new patients from this one site.”

No revised PDF, raw predictions, uncertainty interval, or executable analysis is supplied. The fictional track allows considering the response analysis; it does not allow silently replacing the PDF with a new preprint.

## Working draft — update

**C1: partly resolved.** Response C1 ¶1–3 reports a split that addresses patient overlap and appropriately limits the site claim. I have not reproduced the AUC. The response does not yet provide enough detail about independent test-patient counts and uncertainty to assess the revised empirical support, and the main PDF retains the prior claim. The latter is a promised correction, not an inspected manuscript change.

**Updated overall: borderline; confidence: moderate.** The permitted response supplies relevant new evidence, so my initial rejection rationale has weakened. The remaining question is the adequacy of the patient-level evaluation, not whether the AUC remains 0.94. I ask the AC to assess whether the response evidence and promised textual correction meet this track's decision rules; I do not invent a conditional-acceptance policy or demand a significant improvement. No new-site experiment is added as a requirement.

This update illustrates a reasoned change, not a rule that a lower AUC deserves acceptance or that all rebuttal claims should be trusted. Actual ratings require the full assigned submission and its real rubric.
