# Figure and table appraisal

Use for displays supporting claims within the review scope. Rule classes inherit
the [rulebook](../01-foundations/rulebook.md); these IDs specify how H2/H3/H5/H6
and V1/V2 apply. This is an appraisal guide, not a requirement that every paper
contain every plot element. Apply each check only to the relevant display type.

## Evidence boundaries — hard rules

| ID | Trigger | Obligation and response |
| --- | --- | --- |
| FIG-H1 Actual inspection | Making a visual claim about a figure, panel, or table | Inspect the supplied display at a usable size. Text extraction or a caption alone does not verify marks, readability, image quality, or manipulation. If rendering/access is unavailable, limit comments to inspected text and mark the visual check unavailable. |
| FIG-H2 Interpretable encoding | Interpreting a plotted quantity, symbol, or color | Establish what marks encode from axes, legend, caption and relevant text. Identify quantities, units where meaningful, category/symbol mappings, scale transformations and colorbar meaning. If unclear, ask for the missing mapping; do not invent units or insist on a colorbar for categorical colors. Dimensionless measures should be identifiable as such. |
| FIG-H3 Honest uncertainty and counts | Inferring precision, sample size, or independence | Check what n counts, denominators, independent units, and the definition of error bars/bands when displayed. Do not assume bars are 95% CIs or plotted points are independent replicates. Request clarification or adequate uncertainty only where needed for the claim/design; do not impose one interval or statistic universally. |
| FIG-H4 Claim/display consistency | Reporting a mismatch or misleading display | Compare the exact text, panel/table values, labels, direction, scale and denominators. Describe the discrepancy and consequence, including rounding or different subsets as possible explanations. Do not call an unreadable panel a fabricated result. |
| FIG-H5 Bounded integrity concerns | A suspicious duplication, alteration, or anomaly is observed | Record inspected panels and the precise observation, confidence and access limits. Route a factual concern through the designated restricted channel. Visual resemblance alone is not proof of misconduct; do not claim forensic analysis that was not performed. |
| FIG-H6 Proportionate remedy | Retaining a display-related criticism | Tie priority to the central inference or ability to assess it. Prefer labels, a clearer rendering, caption detail, or another adequate presentation over new experiments where sufficient. A missing unit can be major or minor; decoration preferences do not become acceptance conditions. |

## Venue and design requirements

| ID | Class and trigger | Apply or withhold |
| --- | --- | --- |
| FIG-V1 Technical specifications | V: verified venue instructions on resolution, file format, accessibility, panel size or image adjustments | Cite the actual requirement and affected item. Do not invent universal DPI, font size, palette, axis-origin or journal production rules. Separate production compliance from scientific validity. |
| FIG-V2 Permitted materials | V: review stage controls supplements, original images or interactive artifacts | Inspect only authorized materials and record actual versions. Inaccessible source data limits verification; it does not establish a defect. |

## Presentation checks — soft defaults

| ID | Starting check | When to adapt |
| --- | --- | --- |
| FIG-S1 Readability | Look for readable labels, legends, colorbars, captions and meaningful contrasts at the intended viewing size. | Ask for resizing only when the inspected rendering obstructs interpretation; a low-resolution preview may not represent the submitted original. |
| FIG-S2 Information density | Check whether overplotting, excessive panels or decorative colors obscure a claimed trend. | Suggest transparency, aggregation, faceting or an alternative display as options, retaining the scientific information. A dense point cloud is not automatically poor science. |
| FIG-S3 Accessibility | Prefer redundant encodings, distinguishable colors and clear ordering. | Apply actual accessibility mandates through FIG-V1; otherwise present changes according to their effect on comprehension, not personal taste. |
| FIG-S4 Standalone explanation | Prefer captions defining symbols, sample units, abbreviations and uncertainty sufficiently for interpretation. | Definitions elsewhere can suffice under the venue's format. Locate missing information across authorized material before calling it absent. |
| FIG-S5 Scale and selection | Examine axis ranges, logarithms, omitted categories, image scale bars, normalization and representative-image selection as applicable. | Nonzero axes and transformations are not inherently wrong. Explain a specific distortion or interpretive gap rather than enforce a plotting convention unrelated to the display. |

## Output

Record display/panel ID, version/viewing limit, rule ID, inspected observation,
claim consequence, priority, and smallest adequate remedy in the issue ledger.
Use “not checked” when a check was not performed. Keep ordinary scientific
display concerns available to authors; only sensitive integrity/process details
use the restricted route. These rules do not establish image-forensics expertise.
