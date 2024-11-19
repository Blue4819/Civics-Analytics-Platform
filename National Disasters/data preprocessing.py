import pandas as pd 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

disaster=pd.read_csv(r"National Disasters\Natural_Disasters_in_India.csv")

if 'Unnamed: 0' in disaster.columns:
    disaster.drop(columns=['Unnamed: 0'], inplace=True)

disaster

# Remove columns with identical data
disaster = disaster.loc[:, ~disaster.T.duplicated()]

# Verify that duplicate columns have been removed
print(disaster.head())

# Step 3: Handle missing Date values - Drop rows with missing Date
disaster.dropna(subset=['Date'], inplace=True)

# Drop the 'Duration' column from the DataFrame
if 'Duration' in disaster.columns:
    disaster.drop(columns=['Duration'], inplace=True)

# Verify that the column has been removed
print(disaster.head())

# Step 4: Basic cleaning of text columns 'Title' and 'Disaster_Info'
disaster['Title'] = disaster['Title'].str.strip().str.capitalize()  # Remove leading/trailing spaces and capitalize
disaster['Disaster_Info'] = disaster['Disaster_Info'].str.strip().str.capitalize()  # Same for 'Disaster_Info'

# Check the columns of the dataset
print(disaster.columns)

# Step 7: Final structure check
print(disaster.info())
print(disaster.head())

# Save the cleaned dataset if needed
cleaned_file_path = r"National Disasters\Cleaned_csv.csv"
disaster.to_csv(cleaned_file_path, index=False)

# Step 1: Create a new column for decade ranges
def categorize_decade(year):
    if year < 1990:
        return 'Before 1990'
    elif 1990 <= year < 2000:
        return '1990-1999'
    elif 2000 <= year < 2010:
        return '2000-2009'
    elif 2010 <= year < 2020:
        return '2010-2019'
    elif 2020 <= year <= 2021:
        return '2020-2021'
    else:
        return 'Unknown'

# Apply the function to create a new column
disaster['Decade'] = disaster['Year'].apply(categorize_decade)

# Step 2: Count occurrences of disasters per decade
decade_counts = disaster['Decade'].value_counts()

# Step 3: Create a larger pie chart
plt.figure(figsize=(14, 14))  # Set the figure size for a larger chart

# Step 4: Create an exploded pie chart for better separation
explode = [0.05] * len(decade_counts)  # Slightly explode all slices for separation

# Step 5: Customize the pie chart
plt.pie(
    decade_counts, 
    labels=decade_counts.index,  # Use the decade labels
    autopct='%1.1f%%', 
    startangle=90, 
    explode=explode,  # Explode the slices for clarity
    colors=plt.cm.Paired.colors, 
    textprops={'fontsize': 16},  # Increase font size for readability
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}  # Thicker edges for clarity
)

# Step 6: Add a title reflecting the decade ranges
plt.title('Distribution of Natural Disasters by Decade', fontsize=20)

# Step 7: Ensure the pie is drawn as a circle
plt.axis('equal')

# Step 8: Display the pie chart
plt.show()
