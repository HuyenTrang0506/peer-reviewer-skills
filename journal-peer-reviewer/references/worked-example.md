# Worked example: evidence to report and re-review

Everything below is fictional training material. Numbers illustrate the workflow and were not calculated from a dataset. This example provides no empirical evidence of the skill's performance.

## Supplied assignment and manuscript v1

The fictional owner authorizes a pre-submission review with AI assistance. Requested scope: analytical validity and claim wording; novelty, raw-data reproduction, and specialist assay validation are excluded. The mock venue asks for an author report and a private recommendation using accept/minor/major/reject categories.

**Title:** “Compound Q increases marker X in donor-derived cells.”

**Methods §2:** “Cells from eight donors were divided into vehicle and Q conditions. Each donor supplied three wells per condition. All 24 wells per condition were treated as independent observations in an unpaired test. The endpoint was marker X fluorescence at 24 hours.”

**Results §3:** “Across donors, mean fluorescence was 100 units for vehicle and 104 for Q. The well-level test gave p = 0.01.”

**Figure 1 legend:** “Mean fluorescence by condition. n = 24 wells per condition; error bars indicate SD.” The vertical axis says “Marker X,” without the unit.

**Discussion §4:** “These data establish an increase in marker X after Q treatment in this donor-derived cell system.”

**Data statement:** “Donor and well identifiers were retained; raw measurements are available to the authors for reanalysis.” No raw data are supplied for this review. No claim about a molecular mechanism or clinical benefit is made.

## Private evidence records

| ID | Anchor | Observation/type | Consequence | Priority/remedy |
| --- | --- | --- | --- | --- |
| M1 | Methods §2; Results §3; Discussion §4 | Observed analytical mismatch: nested wells treated as independent and paired donor structure ignored | The reported test does not establish the claimed increase with an appropriate uncertainty assessment | Major: donor-aware analysis, estimates/intervals, and reconciled claims |
| m1 | Figure 1 axis; Results §3 | Reporting gap: axis omits fluorescence unit | Local interpretability | Minor: specify the same unit on the axis |

**Challenge M1:** Could a paired or hierarchical analysis already account for donors? Methods §2 explicitly says otherwise, and no alternate analysis is supplied. Retain the concern. This does not establish that Q has no effect or that a corrected analysis must be nonsignificant.

**Scope restraint:** Do not invent a missing mechanism experiment, demand a clinical trial, or declare the compound novel. Those are outside the supplied claim or assessment. A public raw-data release is not necessary to ask authors to perform a justified reanalysis.

## Working draft for human verification — authors

The study examines the effect of Q on marker X in cells from eight donors using a within-donor comparison. The use of matched conditions and retention of donor/well identifiers provide a useful basis for analysis. The principal issue is that the reported test treats technical wells as independent despite the donor structure. This needs resolution before the stated increase can be assessed.

**M1 — Methods §2, Results §3, Discussion §4.** Each donor contributes three wells to each condition, but the analysis treats all 24 wells per condition as independent in an unpaired test. This does not account for within-donor dependence or the matched comparison, so the reported p-value may misrepresent uncertainty. Please analyze the treatment comparison using a justified donor-aware approach, such as paired donor summaries or an appropriate hierarchical model, and report the effect estimate and interval. Update the figure, results, and conclusion consistently. The present evidence does not tell us what the corrected result will be; a bounded or inconclusive conclusion may be adequate without new experiments.

**m1 — Figure 1 vertical axis.** Please specify the fluorescence unit used in Results §3 so the figure can be interpreted on its own.

This focused assessment does not evaluate novelty, reproduce calculations from raw data, or independently validate the assay.

## Working draft for human verification — editor

**Recommendation: major revision.** The central inference requires a donor-aware analysis and reconciliation of the claim, as explained in M1. Identifiers reportedly remain available, making a remedy within the existing study plausible. This recommendation does not assume a particular reanalysis outcome. Scope excludes novelty, raw-data reproduction, and specialist assay validation. AI assistance is disclosed as permitted by this fictional assignment. No integrity allegation is supported by the supplied material.

## Response and revised manuscript v2

**Response M1:** “We averaged the three technical wells within each donor/condition and analyzed the eight paired donor differences. The revised estimate is +4 units with a 95% interval from −1 to +9 units. We updated the figure and changed the conclusion to an imprecise estimate.”

**Methods §2 v2:** Now describes the paired donor-summary analysis, with eight donors as independent units.

**Results §3 v2 and Figure 1 v2:** Report the estimate and interval above, distinguish donor and well counts, and label the axis “Marker X fluorescence (units).”

**Discussion §4 v2:** “The estimate favors higher marker X under Q, but uncertainty includes a small decrease and a larger increase; these data do not establish the direction with precision.”

## Re-review

| ID | Transition | Verified material | Reason |
| --- | --- | --- | --- |
| M1 | Open → resolved at reporting/analysis-specification level | Methods §2, Results §3, Figure 1, Discussion §4 v2 | The described analysis respects the donor structure, and interpretation reflects the reported interval. Raw-data numerical reproduction remains unperformed. |
| m1 | Open → resolved | Figure 1 v2 | The axis includes the unit. |

**Author follow-up:** The revised analytical description and bounded interpretation address M1, and the figure label addresses m1. I have not reproduced the numerical analysis; resolution here concerns the documented method and consistency of the revised reporting.

**Editor follow-up:** Within the requested focused scope, no further required changes are identified; recommend accept under the mock categories. This is not a judgment on the excluded novelty/assay questions. Do not demand a significant result or additional donors merely because the corrected interval is inconclusive.
