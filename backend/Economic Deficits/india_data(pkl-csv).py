import pandas as pd

# Path to the input .pkl file
input_file = r"Economic Deficits\india_data.pkl"

# Load the pickle file into a DataFrame
df = pd.read_pickle(input_file)

# Path to the output .csv file
output_file = r"Economic Deficits\india_data.csv"

# Save the DataFrame as a CSV file
df.to_csv(output_file, index=False)

print(f"Data has been successfully converted to CSV and saved as '{output_file}'.")