import pandas as pd
from google.cloud import bigquery
import os

# Define the path to CSV file
csv_file_path = "/Users/0x000008/Documents/automated-data-loading/Electric_Vehicle_Population_Data.csv"

# Load the CSV data into a Pandas DataFrame
dataframe = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame to verify the data
print("Loaded CSV data:")
print(dataframe.head())

# Set the environment variable to the path of JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/0x000008/Documents/automated-data-loading/automated-data-loading-52c063a5e147.json"

# Initialize a BigQuery client
client = bigquery.Client()

# Specify the dataset and table names
dataset_name = 'auto_data'
table_name = 'sample_data'

# Specify the BigQuery dataset and table
table_id = f'{client.project}.{dataset_name}.{table_name}'

# Modify column names for consistency and compliance with BigQuery rules
dataframe.columns = dataframe.columns.str.replace(' ', '_').str.replace('-', '_').str.replace('__', '_').str.replace('(', '').str.replace(')', '')
dataframe.columns = dataframe.columns.str[:300]  # Limit to 300 characters

# Convert specific columns to string data type
columns_to_convert = ['Electric_Vehicle_Type', 'Electric_Range', 'Base_MSRP', 'Legislative_District', 'DOL_Vehicle_ID', '2020_Census_Tract']
for col in columns_to_convert:
    dataframe[col] = dataframe[col].astype(str)

# Convert other numeric columns to string
numeric_columns = dataframe.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_columns:
    dataframe[col] = dataframe[col].astype(str)

# Update the schema to match the DataFrame columns
bq_schema = [
    bigquery.SchemaField(name, 'STRING') for name in dataframe.columns
]

# Load the data into BigQuery
job_config = bigquery.LoadJobConfig(
    schema=bq_schema,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

# Write the DataFrame to a BigQuery table
job = client.load_table_from_dataframe(dataframe, table_id, job_config=job_config)
job.result()  # Wait for the job to complete

print("Data successfully loaded into BigQuery table.")
