Global Workforce Intelligence & Talent Optimization
Overview

Global Workforce Intelligence & Talent Optimization is a comprehensive HR analytics project designed to transform raw employee and recruitment data into actionable insights. The goal is to help HR leaders understand workforce dynamics, identify high‑potential talent, mitigate burnout risks, and optimize recruitment and promotion strategies. The project uses Python for data preparation and feature engineering, SQL for ad‑hoc queries, and Power BI for interactive dashboards.

Data Sources

The analysis integrates multiple publicly available HR datasets to simulate the kind of information a large organisation might collect:

IBM HR Attrition Dataset (1470 rows, 35 columns): Contains demographics, job role, performance, overtime, satisfaction, engagement, tenure, and whether an employee left (Attrition).
HRDataset_v14 (311 rows, 36 columns): Provides employee names, departments, positions, salary, performance scores, engagement surveys, satisfaction, special projects count, absences, lateness, and recruitment source.
aug_train (Recruitment dataset – 19,158 rows, 14 columns): Includes candidate demographics, education level, company size/type, experience, training hours, and whether the candidate moved to a new job. We use it to model recruitment channel effectiveness.
aug_test (Separate test set used only for demonstration).
HR-Employee-Attrition.csv: A duplicate of the IBM dataset included for completeness.
Data Preparation & Feature Engineering

All data manipulation is performed in scripts/data_preprocessing.py. Key steps include:

Cleaning: Remove duplicates, standardise date formats, fix inconsistent labels, and impute missing values (mode for categorical fields and median for numerical fields).
Performance Mapping: Convert qualitative performance ratings (Exceeds, Fully Meets, Needs Improvement, PIP) into numeric scores (5, 4, 2, 1) to support quantitative analysis.
Talent Score: A weighted composite indicator of employee potential:
35% PerformanceScore (numeric)
25% EngagementSurvey
20% EmployeeSatisfaction
10% SpecialProjectsCount
–10% Absences
Burnout Risk: Proxy measure of overwork and disengagement:
30% Absences
40% DaysLateLast30
–30% EngagementSurvey
Promotion Readiness: Estimate of suitability for advancement:
40% PerformanceScore
30% SpecialProjectsCount
30% EngagementSurvey
Recruitment Cleaning: Fill missing company size/type, education level and gender as “Unknown,” convert experience from string ranges to numeric, and normalise training hours.
Export: Save the cleaned HR data (employee_talent_features.csv), cleaned attrition data (employee_attrition_clean.csv), and cleaned recruitment data (recruitment_clean.csv) into data_cleaned/.
Key Performance Indicators (KPIs)

The dashboard tracks and computes the following KPIs. Each KPI is defined below to help interviewers understand the reasoning:

KPI	Definition	Calculation
Total Employees	Number of unique employees in the company.	COUNT(DISTINCT EmployeeNumber)
Average Salary	Mean of current annual salaries across employees.	AVG(Salary)
Average Talent Score	Overall workforce potential. Higher = stronger talent pipeline.	AVG(Talent_Score)
Average Burnout Risk	Average risk of burnout. Higher = greater risk.	AVG(Burnout_Risk)
Average Promotion Readiness	Average score indicating employees ready for promotion.	AVG(Promotion_Readiness)
Employee Satisfaction	Average of engagement/satisfaction survey results.	AVG(EmpSatisfaction)
Attrition Rate	Proportion of employees who left in a given period.	(Employees Who Left) / (Total Employees)
Recruitment Efficiency	Combines offer acceptance rate, time to hire, and candidate quality.	Custom formula in SQL/Power BI
Onboarding Completion Rate	% of new hires completing required onboarding tasks.	Completed Onboarding / Total New Hires

Other metrics tracked in supporting SQL queries include absenteeism rate, average tenure, recruitment conversion rate, training completion rate, and salary vs. performance correlation.

Dashboard Design

The Power BI dashboard is designed with executives and HR managers in mind. It contains six sections:

Top KPIs: Display workforce size, talent health, burnout risk, promotion readiness, average salary, and satisfaction at a glance using cards and gauges.
Department Overview: Visualises headcount by department, average salary by department, and satisfaction distribution to compare teams.
Talent vs Burnout: A clustered column chart compares average talent score and burnout risk for each department, highlighting units where high performers may be at risk of burnout.
Promotion Readiness by Role: Horizontal bar chart ranks job positions by their average promotion readiness, helping leadership identify where succession pipelines are strong or weak.
High Potential Employee Mapping: Scatter plot comparing salary against talent score with bubble size proportional to promotion readiness. Colour-coded by department, this chart reveals underpaid high talent individuals and overcompensated low performers.
Employee Satisfaction Distribution: 100% stacked bar chart showing distribution of satisfaction/engagement scores across the workforce.

The dashboard also includes interactive filters for department, position, and gender, enabling drill-down analysis.

Repository Structure
executive-workforce-intelligence/
├── README.md                  # Project documentation
├── scripts/
│   ├── data_preprocessing.py  # Python script for cleaning and feature engineering
│   ├── department_summary.sql # Example SQL queries (e.g. headcount by department)
├── data_raw/                  # Original datasets (to be uploaded)
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   ├── HR-Employee-Attrition.csv
│   ├── HRDataset_v14.csv
│   ├── aug_train.csv
│   ├── aug_test.csv
│   └── sample_submission.csv
├── data_cleaned/              # Outputs generated by data_preprocessing.py
│   ├── employee_attrition_clean.csv
│   ├── employee_talent_features.csv
│   └── recruitment_clean.csv
└── images/
    └── dashboard.png          # Export of the final Power BI dashboard
How to Run
Clone the repository and create a virtual environment.
Install dependencies using pip install -r requirements.txt if provided, or manually install pandas, numpy, and scikit-learn for data processing.

Run the preprocessing script from the root directory:

python scripts/data_preprocessing.py

This will clean the raw data and export the feature‑engineered tables to data_cleaned/.

Open Power BI Desktop, import the CSV files from data_cleaned/, and recreate the dashboard following the design described above. Alternatively, use the provided dashboard.pbix file if included.
Execute department_summary.sql against the employee_talent_features table in your favourite SQL tool to produce departmental summaries.
Interview Preparation Notes
HR Analytics Concepts: Be prepared to explain terms like attrition, employee engagement, performance ratings, high‑potential talent, and workforce planning.
Metric Design: Understand how each engineered KPI aligns with strategic HR objectives—for example, why we penalise absenteeism in the talent score, or why engagement scores are subtracted in burnout risk.
Business Impact: Discuss how the insights could inform real HR decisions, such as focusing retention efforts on high‑talent departments with high burnout or prioritising promotions for roles with strong readiness.
Limitations: Address ethical and practical considerations when using employee data, including privacy, potential bias in performance evaluations, and the importance of validating model assumptions.
Next Steps: Mention future enhancements like predictive modelling of attrition using logistic regression or machine learning (e.g., random forest), deploying dashboards to the cloud for real‑time monitoring, or integrating additional data sources like training records or exit interview feedback.
