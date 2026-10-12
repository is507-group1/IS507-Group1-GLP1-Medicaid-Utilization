
# GLP-1 Utilization & Health Needs Across U.S. States
**IS 507: Data, Statistical Models, and Information | Fall 2026 | Group 1**

## Overview

This project examines Medicaid GLP-1 prescription patterns across U.S. states in relation to obesity and diabetes prevalence. We aim to identify states with lower-than-predicted prescription rates and investigate whether these gaps narrowed during 2025.

## Research Question

**Are U.S. states with Medicaid GLP-1 prescription rates below the levels predicted by their obesity and diabetes prevalence catching up during 2025?**

Here, *catching up* refers to a reduction in the gap between actual and model-predicted prescription rates from Q1 to Q4 of 2025. These gaps do not directly measure unmet medical needs or barriers to access.

## Datasets

| Dataset | Purpose |
|---|---|
| [CMS Medicaid State Drug Utilization Data](https://data.medicaid.gov/dataset/158a1baa-5506-400a-8ec3-97756f0b0536) | Identify GLP-1 prescriptions and aggregate counts by state and quarter |
| [CDC BRFSS 2025](https://www.cdc.gov/brfss/annual_data/annual_2025.html) | Estimate state-level obesity and diabetes prevalence |
| [CMS Medicaid Enrollment](https://data.medicaid.gov/dataset/6165f45b-ca93-5bb5-9d06-db29c692a360) | Calculate quarterly Medicaid GLP-1 prescription rates using enrollment data |

## Methodology

1. **Data Preparation:** Identify GLP-1 medications, address missing and suppressed records, and integrate prescription, enrollment, and health prevalence data.
2. **Multiple Linear Regression:** Predict state-level Medicaid GLP-1 prescription rates using obesity prevalence, diabetes prevalence, and quarter.
3. **Gap and Trend Analysis:** Identify states with negative prediction gaps in Q1 and examine changes through Q4.
4. **Model Evaluation:** Use state-grouped cross-validation and Mean Squared Error (MSE) to evaluate predictive performance.
5. **Baseline Comparison:** Compare regression performance against the quarterly average prescription rate across training states.

## Project Files

- [Midterm Report (PDF)](Midterm_Report/%28Group%201%29%20GLP-1%20Utilization%20%26%20Health%20Needs%20Across%20U.S.%20States.pdf)
- [Analysis Code]

## Institution

University of Illinois Urbana-Champaign | Fall 2026
  
