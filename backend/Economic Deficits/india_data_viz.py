import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv(r"C:\Users\Tanya\OneDrive\Desktop\Capstone Project Codes\india_data.csv")


# Filter year-specific columns and relevant metadata
year_columns = [str(year) for year in range(1990, 2024)]
key_columns = ['Series Name', 'Indicator Type'] + year_columns
filtered_data = data[key_columns].dropna(subset=year_columns, thresh=10)

# Melt the data for plotting
melted = filtered_data.melt(
    id_vars=['Series Name', 'Indicator Type'],
    var_name='Year',
    value_name='Value'
)

# Convert 'Year' to numeric
melted['Year'] = pd.to_numeric(melted['Year'], errors='coerce')

# Create individual plots for each Series Name
unique_series = melted['Series Name'].unique()

# Set up the plots
for series in unique_series:
    # Filter data for the current series
    series_data = melted[melted['Series Name'] == series]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(series_data['Year'], series_data['Value'], marker='o', label=series)
    plt.title(f'Trend of {series} (1990-2023)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()