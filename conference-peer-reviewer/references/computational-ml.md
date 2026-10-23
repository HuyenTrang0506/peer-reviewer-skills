# Computational and machine-learning appraisal

Use when a central claim depends on computation, prediction, simulation, or model comparison. The relevant validation unit depends on the intended use, not the file format.

## Generalization target and leakage

Identify what must be new at deployment: participants, sites, time periods, documents, molecular scaffolds, environments, or another unit. Trace training, preprocessing, feature selection, hyperparameter tuning, model selection, and final testing against that target.

A random image split with the same patients in both sets cannot establish new-patient generalization without addressing patient dependence. Repeated use of the test set for tuning compromises its role as a final holdout. Check duplicate/near-duplicate records and preprocessing fitted on evaluation data when relevant. Do not accuse leakage simply because a split description is missing: ask for the relevant boundaries and procedure.

Patient-disjoint testing addresses patient overlap but does not establish cross-hospital generalization. Temporal testing addresses one type of shift but does not establish all deployment conditions. Match the requested evaluation to the stated claim.

## Comparisons and uncertainty

Compare baselines using compatible data, splits, preprocessing, tuning budgets, and metrics, or explain documented differences. Include strong relevant comparators without requiring every recent model. Verify external citations before calling a comparator obsolete or declaring novelty.

Inspect class imbalance, threshold selection, calibration when predictions are probabilities, uncertainty at the appropriate independent unit, and practical magnitude. Repeated seeds quantify some training variability; they do not replace independent participants or sites. Do not demand accuracy alone for an imbalanced or decision-sensitive application.

## Reproduction and simulation

Record data access, restrictions, versions, preprocessing, configuration, seeds, environment, and commands actually inspected or run. A repository link alone does not establish reproducibility. A successful rerun of one table does not validate data provenance or every claim.

For simulation, inspect model assumptions, parameter ranges, boundary conditions, numerical convergence/stability, and empirical or analytical checks relevant to the claim. Do not impose supervised-learning split requirements on a mathematical proof or simulation where they do not apply.

## Proportionate findings

| Observation | Consequence and minimum remedy |
| --- | --- |
| Demonstrated patient overlap with a new-patient headline claim | The reported test does not establish that target; request patient-disjoint re-evaluation or narrow the claim. Do not predict the unobserved corrected score. |
| Split unit unreported | Ask for split construction and separation of fitting/tuning/testing; phrase leakage as an unresolved question. |
| External-site testing absent, claim limited to one site's new patients | State the applicability boundary; external validation can be optional rather than a publication condition. |
| Model chosen using test scores | Request a fresh appropriate holdout or a clearly bounded exploratory interpretation. |
| Restricted data with a justified access process | Assess the documented route and reproducibility limits; do not demand an unauthorized public release. |
