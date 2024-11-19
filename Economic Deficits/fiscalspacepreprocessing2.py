import pandas as pd
import os

# Path to the Variable List and the directory containing CSV files
variable_list_path = 'Economic Deficits/Datasets/Variable_List.csv'
csv_dir = 'Economic Deficits/Datasets'

# Read the Variable List
variable_df = pd.read_csv(variable_list_path)


variable_dict = dict(zip(variable_df['Variable Name'], variable_df['Series Name']))

# Iterate through all CSV files in the directory
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv') and filename != 'Variable_List.csv':
        file_path = os.path.join(csv_dir, filename)
        
        # Get the variable name (without .csv extension)
        variable_name = os.path.splitext(filename)[0]
        
        # Get the corresponding series name
        series_name = variable_dict.get(variable_name, "Unknown Series")
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Add the series name as the first row
        df.loc[-1] = [series_name] + [''] * (len(df.columns) - 1)  # adding a row
        df.index = df.index + 1  # shifting index
        df = df.sort_index()  # sorting by index
        
        # Save the updated dataframe back to CSV
        df.to_csv(file_path, index=False)
        
        print(f"Updated {filename} with series name: {series_name}")

print("All CSV files have been updated with their corresponding series names.")
