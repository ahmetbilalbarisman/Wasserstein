import pandas as pd
import numpy as np
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metrics import ColumnDriftMetric, DatasetDriftMetric

np.random.seed(42)

reference_data = pd.DataFrame({
    'feature1': np.random.normal(loc=0, scale=1, size=1000),
    'feature2': np.random.normal(loc=5, scale=2, size=1000),
    'feature3': np.random.exponential(scale=1, size=1000),
    'feature4': np.random.uniform(low=0, high=10, size=1000),
})

current_data = pd.DataFrame({
    'feature1': np.random.normal(loc=0.5, scale=1.5, size=1000),
    'feature2': np.random.normal(loc=6, scale=2.5, size=1000),
    'feature3': np.random.exponential(scale=1.2, size=1000),
    'feature4': np.random.uniform(low=1, high=11, size=1000),
})

column_mapping = ColumnMapping(
    numerical_features=['feature1', 'feature2', 'feature3', 'feature4'],
)

# Create a custom report with the Wasserstein test for feature1
report = Report(metrics=[
    DataDriftPreset(
        num_stattest='jensenshannon',  # wasserstein ayarlanabilir
        num_stattest_threshold=0.2,  
    ),
    ColumnDriftMetric(column_name='feature1', stattest='jensenshannon', stattest_threshold=0.2), # wasserstein ayarlanabilir
    DatasetDriftMetric(drift_share=0.7)  # Set condition for dataset drift (70% of columns should show drift)
])

report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)

report.save_html("custom_data_drift_report.html")
