# Executive Workforce Intelligence & Talent Optimisation

## Overview
This project delivers an end-to-end HR analytics solution: cleaning and enriching raw HR data, engineering composite metrics, and presenting key insights in a Power BI dashboard. It helps managers understand employee performance, satisfaction, burnout risk and promotion readiness across departments and job roles.

## Data
The analysis uses three public HR datasets (IBM HR Attrition, HRDataset_v14 and a recruitment dataset). Only HRDataset_v14 is used for the current dashboard; the others are included for completeness.

## Processing
The script `scripts/data_preprocessing.py` loads the HRDataset, cleans missing values, maps text performance ratings to a 1–5 scale and creates three composite metrics:
- **Talent Score**: weighted combination of performance, engagement, satisfaction, project work and absences.
- **Burnout Risk**: emphasises absences and lateness, reduced by engagement.
- **Promotion Readiness**: based on performance, projects and engagement.

The cleaned dataset is saved to `data_cleaned/employee_talent_features.csv`.

## Dashboard
The Power BI report (see `images/dashboard.png`) summarises workforce health. It includes:
- KPI cards for average talent, burnout, promotion readiness, salary and employee satisfaction.
- Charts showing headcount by department, talent vs burnout, promotion readiness by role, satisfaction distribution and high-potential employees by salary and talent score.
- Slicers to filter by department or job role.

## Repository structure
- `data_raw/`: original CSV files.
- `data_cleaned/`: processed dataset.
- `scripts/`: data_preprocessing script and example SQL.
- `images/dashboard.png`: screenshot of the dashboard.
- `README.md`: this document.

## Using this project
Run `python scripts/data_preprocessing.py` to regenerate the cleaned dataset. Open the Power BI report and point it at `data_cleaned/employee_talent_features.csv` to refresh visuals.
