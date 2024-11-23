import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
covid = pd.read_csv("National Disasters\Covid_India.csv")

if 'Unnamed: 0' in covid.columns:
    covid.drop(columns=['Unnamed: 0'], inplace=True)

covid

# Remove columns with identical data
covid = covid.loc[:, ~covid.T.duplicated()]

# Verify that duplicate columns have been removed
print(covid.head())

# Handle missing Date values - Drop rows with missing Date
covid.dropna(subset=['Date'], inplace=True)

# Check the columns of the dataset
print(covid.columns)

#Final structure check
print(covid.info())
print(covid.head())

cleaned_file_path = "National Disasters\Covid_cleaneddata .csv"
covid.to_csv(cleaned_file_path, index=False)

# Step 1: Group by 'Name of State / UT' and sum the total confirmed cases
state_cases = covid.groupby('Name of State / UT')['Total Confirmed cases'].sum()

# Step 2: Plot the pie chart
plt.figure(figsize=(14, 14))

# Use a color palette that is distinct for each segment
colors = plt.cm.tab20.colors  # Using a colormap for better distinction

# Create the pie chart with more clarity
plt.pie(state_cases, 
         labels=state_cases.index, 
         autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '',  # Only show percentages above 0
         startangle=140, 
         colors=colors,
         wedgeprops=dict(edgecolor='white'))  # Add white edges for clarity

# Add a title
plt.title("Distribution of Total Confirmed COVID-19 Cases by State/UT in India", fontsize=18)

# Equal aspect ratio ensures that pie chart is circular
plt.axis('equal')  

# Create a legend
plt.legend(state_cases.index, title="States/UTs", loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.tight_layout()  # Adjust layout to make room for the legend
plt.show()
