import pandas as pd
import os

# Path to the Excel file
excel_file_path = 'Economic Deficits/Datasets/Fiscal-space-data.xlsx'

# Read the Excel file
xl = pd.ExcelFile(excel_file_path)

# Get the directory of the Excel file
output_dir = os.path.dirname(excel_file_path)

# Iterate through all sheets
for sheet_name in xl.sheet_names:
    # Read the sheet
    df = xl.parse(sheet_name)
    
    # Create a valid filename
    valid_filename = f"{sheet_name.replace(' ', '_')}.csv"
    
    # Create the full output path
    output_path = os.path.join(output_dir, valid_filename)
    
    # Save the dataframe as a CSV file
    df.to_csv(output_path, index=False)
    
    print(f"Saved {sheet_name} to {output_path}")

print("All sheets have been saved as separate CSV files.")