import pandas as pd
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Sample data
reference_data = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 6, 7, 8, 9]
})

current_data = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 6, 7, 8, 9]
})
# Define column mapping
column_mapping = ColumnMapping(
    numerical_features=['feature1', 'feature2']
)

# Create a data drift report
report = Report(metrics=[
    DataDriftPreset()
])

# Calculate the report
report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)

# Save the report to an HTML file
report.save_html("data_drift_reporttest.html")
