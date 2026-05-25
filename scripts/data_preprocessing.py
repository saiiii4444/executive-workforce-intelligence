"""
Data preprocessing script for the Executive Workforce Intelligence project.

This script reads the raw HR dataset, performs basic cleaning, maps
performance labels to a numeric scale and engineers composite scores for
talent, burnout and promotion readiness.  The cleaned and enriched
dataset is written to the ``data_cleaned`` folder.

Usage::

    python data_preprocessing.py

Note that this script expects the raw data to be located in
``../data_raw/HRDataset_v14.csv`` relative to the script location and
will write the output to ``../data_cleaned/employee_talent_features.csv``.

You can adjust the input and output paths by editing the constants
defined near the top of the file.
"""

import os
import pandas as pd
from pathlib import Path


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

# Path to the raw HR data (CSV).  Adjust as necessary.  The default assumes
# the dataset lives one directory above this script in ``data_raw``.
RAW_HR_DATA = Path(__file__).resolve().parents[1] / "data_raw" / "HRDataset_v14.csv"

# Path to the output directory.  The cleaned file will be saved here.
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data_cleaned"

# Name of the cleaned dataset
OUTPUT_FILE = OUTPUT_DIR / "employee_talent_features.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load the raw HR dataset from the given path.

    Raises:
        FileNotFoundError: if the file does not exist.

    Returns:
        pandas.DataFrame: the loaded data.
    """
    if not path.exists():
        raise FileNotFoundError(f"Raw data not found at {path}")
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw HR data and engineer new metrics.

    Steps performed:

    - Drop unused columns that are not needed for the dashboard.
    - Fill missing numeric values with the median of the column.
    - Fill missing categorical values with ``'Unknown'``.
    - Map performance codes or labels to a numeric scale when present.
    - Create composite scores for talent, burnout and promotion readiness.

    Args:
        df (pandas.DataFrame): Raw input data.

    Returns:
        pandas.DataFrame: Cleaned and enriched data ready for analysis.
    """
    # Copy to avoid modifying the original frame
    data = df.copy()

    # Keep only columns relevant to workforce analytics.  Use get to avoid
    # KeyError if a column is missing.  Additional columns can be added here.
    columns_to_keep = [
        "Employee_Name", "EmployeeNumber", "Department", "Position",
        "Salary", "EngagementSurvey", "EmpSatisfaction",
        "SpecialProjectsCount", "Absences", "DaysLateLast30",
        "PerformanceScore", "RecruitmentSource"
    ]
    data = data[[col for col in columns_to_keep if col in data.columns]]

    # Fill missing categorical values with 'Unknown'
    categorical_cols = [c for c in data.columns if data[c].dtype == object]
    for col in categorical_cols:
        data[col] = data[col].fillna("Unknown")

    # Fill missing numeric values with median
    numeric_cols = [c for c in data.columns if pd.api.types.is_numeric_dtype(data[c])]
    for col in numeric_cols:
        data[col] = data[col].fillna(data[col].median())

    # Map performance labels to numeric scores.  If the source data already
    # provides numeric performance codes, this mapping will not change it.
    # Common labels from public HR datasets include: 'Exceeds', 'Fully Meets',
    # 'Needs Improvement', 'PIP'.  Feel free to adjust the mapping for your data.
    performance_mapping = {
        "Exceeds": 5,
        "Fully Meets": 4,
        "Needs Improvement": 2,
        "PIP": 1,
        # Additional mappings can be added here
    }
    if "PerformanceScore" in data.columns:
        # Use map for strings; if numeric codes are present they'll fall through
        data["PerformanceScore_Numeric"] = data["PerformanceScore"].map(performance_mapping)
        # If mapping produced NaN (because values were numeric), fill with existing
        data["PerformanceScore_Numeric"] = data["PerformanceScore_Numeric"].fillna(data["PerformanceScore"])
    else:
        # If the column doesn't exist, create a neutral score
        data["PerformanceScore_Numeric"] = 3

    # Ensure numeric types for metric columns
    for col in [
        "EngagementSurvey", "EmpSatisfaction", "SpecialProjectsCount",
        "Absences", "DaysLateLast30", "Salary", "PerformanceScore_Numeric"
    ]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce").fillna(data[col].median())

    # Engineer Talent Score
    data["Talent_Score"] = (
        data.get("PerformanceScore_Numeric", 0) * 0.35
        + data.get("EngagementSurvey", 0) * 0.25
        + data.get("EmpSatisfaction", 0) * 0.20
        + data.get("SpecialProjectsCount", 0) * 0.10
        - data.get("Absences", 0) * 0.10
    )

    # Engineer Burnout Risk Score
    data["Burnout_Risk"] = (
        data.get("Absences", 0) * 0.30
        + data.get("DaysLateLast30", 0) * 0.40
        - data.get("EngagementSurvey", 0) * 0.30
    )

    # Engineer Promotion Readiness
    data["Promotion_Readiness"] = (
        data.get("PerformanceScore_Numeric", 0) * 0.40
        + data.get("SpecialProjectsCount", 0) * 0.30
        + data.get("EngagementSurvey", 0) * 0.30
    )

    return data



def main() -> None:
    """Main entry point for the script."""
    # Load raw data
    df_raw = load_data(RAW_HR_DATA)

    # Clean and engineer features
    df_clean = clean_data(df_raw)

    # Ensure the output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save cleaned data
    df_clean.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
