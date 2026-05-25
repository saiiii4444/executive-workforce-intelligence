# Executive Workforce Intelligence & Talent Optimization

A workforce analytics project built with Python, SQL, and Power BI to analyze employee performance, attrition, satisfaction, burnout risk, and promotion readiness.

The project turns raw HR and recruitment data into cleaned datasets, useful metrics, and an interactive dashboard for workforce decision-making.

---

## Project Objective

HR teams often deal with scattered employee and recruitment data. This project focuses on organizing that data and answering practical workforce questions:

- Which departments have higher attrition?
- Are high-performing employees at risk of burnout?
- Which roles show stronger promotion readiness?
- How is satisfaction distributed across the workforce?
- What patterns can support better hiring and workforce planning?

---

## Tools Used

- Python
- SQL
- Power BI
- Pandas
- NumPy
- Scikit-learn

---

## Data Sources

The project uses publicly available HR and recruitment datasets, including:

- IBM HR Attrition Dataset
- HRDataset_v14
- Recruitment training dataset
- Recruitment test dataset

The data includes employee demographics, departments, job roles, salary, performance, satisfaction, engagement, absences, overtime, tenure, and recruitment-related information.

---

## Project Workflow

```text
Raw HR Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
SQL Analysis
    ↓
Power BI Dashboard
    ↓
Workforce Insights
Data Preparation

The data preparation was done in Python.

Main steps included:

Removed duplicate records
Standardized column names and category values
Handled missing values
Converted performance ratings into numerical values
Cleaned recruitment fields such as experience, education level, company size, and training hours
Exported cleaned datasets for dashboarding

The cleaned files are saved in the data_cleaned/ folder.

Feature Engineering

I created three main workforce indicators to support the analysis.

Talent Score

A combined score based on employee performance, engagement, satisfaction, project contribution, and attendance behavior.

Burnout Risk

A proxy indicator based on absences, lateness, and engagement levels.

Promotion Readiness

A score designed to identify employees who may be ready for internal growth or promotion opportunities.

These indicators are not meant to replace real HR decisions. They are analytical features created to explore workforce patterns.

Dashboard Overview

The Power BI dashboard includes the following views:

Workforce Snapshot

Shows key indicators such as total employees, average salary, employee satisfaction, talent score, burnout risk, and promotion readiness.

Department Overview

Compares departments by headcount, salary, and satisfaction.

Talent vs Burnout

Highlights departments where strong talent may also be showing signs of burnout risk.

Promotion Readiness by Role

Shows which job roles have higher average promotion readiness.

High Potential Employee Mapping

Compares salary, talent score, and promotion readiness to identify useful workforce patterns.

Satisfaction Distribution

Shows how employee satisfaction is distributed across the workforce.

Key Metrics

The dashboard tracks:

Total Employees
Average Salary
Attrition Rate
Employee Satisfaction
Average Talent Score
Average Burnout Risk
Average Promotion Readiness
Recruitment Efficiency

Additional analysis includes absenteeism, tenure, salary-performance relationship, and recruitment conversion patterns.

Repository Structureexecutive-workforce-intelligence/
│
├── README.md
│
├── scripts/
│   ├── data_preprocessing.py
│   └── department_summary.sql
│
├── data_raw/
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   ├── HR-Employee-Attrition.csv
│   ├── HRDataset_v14.csv
│   ├── aug_train.csv
│   ├── aug_test.csv
│   └── sample_submission.csv
│
├── data_cleaned/
│   ├── employee_attrition_clean.csv
│   ├── employee_talent_features.csv
│   └── recruitment_clean.csv
│
├── images/
│   └── dashboard.png
│
└── dashboard.pbix
SQL Analysis

The repository includes SQL queries for quick workforce summaries, including:

Headcount by department
Average salary by department
Satisfaction trends
Talent and burnout comparison
Promotion readiness by role
SELECT
    Department,
    COUNT(*) AS total_employees,
    ROUND(AVG(Salary), 2) AS avg_salary,
    ROUND(AVG(Talent_Score), 2) AS avg_talent_score,
    ROUND(AVG(Burnout_Risk), 2) AS avg_burnout_risk
FROM employee_talent_features
GROUP BY Department
ORDER BY total_employees DESC;
Main Learnings

This project helped me practice:

Cleaning messy HR datasets
Creating useful analytical features
Writing SQL queries for business analysis
Designing KPIs for workforce reporting
Building a Power BI dashboard from cleaned data
Turning raw data into clear business insights
Future Improvements

Planned improvements:

Build an attrition prediction model
Add workforce forecasting
Improve Power BI dashboard design
Add more SQL analysis files
Include a proper data dictionary
Deploy the dashboard or publish it online
