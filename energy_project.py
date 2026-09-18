import pandas as pd
import matplotlib.pyplot as plt


print('hello world')
print('good lock')


# Source: Norouzi, M., Labbafan, S., Farajnia, B., Torabi, M., & Norouzi, M. R. (2023). Dataset on environmental impacts and costs of energy consumption in educational buildings in Iran. Data in Brief, 51, 109606. DOI: 10.17632/6w6vv8n4tf.1
# Load the dataset
df = pd.read_excel('energy_project.xlsx') 

# print(df.head())
# print(df.describe())
# print(df.isnull().sum())

# Drop columns with excessive missing values
df_clean = df.drop(columns=[
    'Schools Name',
    'City_Code',
    'Serial Number[Shomareh Eshterak Gas]',
    'Area[m2]',
    'number of students'
])

# Fill missing temperature values with the mean
temp_cols = [
    'Highest Monthly Outdoor Tempreture',
    'Lowest Monthly Outdoor Tempreture',
    'Average Monthly Tempreture'
]
for col in temp_cols:
    df_clean[col] = df_clean[col].fillna(df_clean[col].mean())

# Calculate mean, median, and standard deviation of gas consumption
consumption_summary = df_clean['Natural Gas Consumtion[m3]'].agg(['mean', 'median', 'std'])

# Convert Date column to datetime
df_clean['Date'] = pd.to_datetime(df_clean['Date'])

df_clean['Month'] = df_clean['Date'].dt.month
df_clean['Year'] = df_clean['Date'].dt.year

season_map = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Fall',
    10: 'Fall', 11: 'Fall', 12: 'Winter'
}
df_clean['Season'] = df_clean['Month'].map(season_map)

# Save the cleaned dataset as CSV
df_clean.to_csv('cleaned_energy_data.csv', index=False) 

# Plot monthly consumption trend (line chart)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

monthly_consumption = df.groupby(['Year', 'Month'])['Natural Gas Consumtion[m3]'].sum()
monthly_consumption = monthly_consumption.reset_index()
monthly_consumption['Date'] = pd.to_datetime(
    monthly_consumption['Year'].astype(str) + '-' + monthly_consumption['Month'].astype(str)
)

plt.figure(figsize=(12, 6))
plt.plot(monthly_consumption['Date'], monthly_consumption['Natural Gas Consumtion[m3]'], marker='o', color='navy')
plt.title('12-Month Gas Consumption Trend')
plt.xlabel('Date')
plt.ylabel('Gas Consumption [m3]')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot seasonal consumption (bar chart)
df_clean['Date'] = pd.to_datetime(df_clean['Date'])
df_clean['Month'] = df_clean['Date'].dt.month


season_map = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Fall',
    10: 'Fall', 11: 'Fall', 12: 'Winter'
}
df_clean['Season'] = df_clean['Month'].map(season_map)

seasonal_consumption = df_clean.groupby('Season')['Natural Gas Consumtion[m3]'].sum()

seasonal_consumption.plot(kind='bar')
plt.title('Seasonal Gas Consumption')
plt.xlabel('Season')
plt.ylabel('Gas Consumption [m3]')
plt.show()

# Plot scatter plot (consumption vs. cost)
x = df_clean['Natural Gas Consumtion[m3]']
y = df_clean['Payable_Amount[USD]']

plt.scatter(x, y)
plt.title('Gas Consumption vs Payable Amount')
plt.xlabel('Gas Consumption [m3]')
plt.ylabel('Payable Amount [USD]')
plt.show()