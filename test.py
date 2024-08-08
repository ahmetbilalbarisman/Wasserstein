import pandas as pd
import numpy as np
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Set random seed for reproducibility
np.random.seed(42)

# Generate reference data
reference_data = pd.DataFrame({
    'feature1': np.random.normal(loc=0, scale=1, size=1000),
    'feature2': np.random.normal(loc=5, scale=2, size=1000),
    'feature3': np.random.exponential(scale=1, size=1000),
    'feature4': np.random.uniform(low=0, high=10, size=1000),
    'feature5': [1, 2, 3, 4, 5]
})

# Generate current data with some drift
current_data = pd.DataFrame({
    'feature1': np.random.normal(loc=0.5, scale=1.5, size=1000),
    'feature2': np.random.normal(loc=6, scale=2.5, size=1000),
    'feature3': np.random.exponential(scale=1.2, size=1000),
    'feature4': np.random.uniform(low=1, high=11, size=1000),
    'feature5': [1, 2, 3, 4, 5]
})

# Define column mapping
column_mapping = ColumnMapping(
    numerical_features=['feature1', 'feature2', 'feature3', 'feature4']
)

# Create a data drift report
report = Report(metrics=[
    DataDriftPreset()
])

# Calculate the report
report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)

# Save the report to an HTML file
report.save_html("complex_data_drift_report.html")
