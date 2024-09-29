import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

disaster=pd.read_csv(r"C:\Users\Tanya\OneDrive\Desktop\CAP data\Natural_Disasters_in_India .csv")

disaster.drop(columns=['Unnamed: 0'], inplace=True)

disaster

disaster = disaster.loc[:, ~disaster.T.duplicated()]
print(disaster.head())

disaster.dropna(subset=['Date'], inplace=True)

disaster.drop(columns=['Duration'], inplace=True)

print(disaster.head())

disaster['Title'] = disaster['Title'].str.strip().str.capitalize()  # Remove leading/trailing spaces and capitalize
disaster['Disaster_Info'] = disaster['Disaster_Info'].str.strip().str.capitalize()  # Same for 'Disaster_Info'

print(disaster.columns)

print(disaster.info())
print(disaster.head())

cleaned_file_path = r"C:\Users\Tanya\OneDrive\Desktop\CAP data\Cleaned_csv .csv"
disaster.to_csv(cleaned_file_path, index=False)

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

disaster['Decade'] = disaster['Year'].apply(categorize_decade)
decade_counts = disaster['Decade'].value_counts()
plt.figure(figsize=(14, 14))  # Set the figure size for a larger chart

explode = [0.05] * len(decade_counts)  # Slightly explode all slices for separation

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

plt.title('Distribution of Natural Disasters by Decade', fontsize=20)
plt.axis('equal')
plt.show()
