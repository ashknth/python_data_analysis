import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (replace 'bread_price.csv' with your actual file path)
file_path = '/Users/dhirajnath/Downloads/Week7Programs/Chapter_11/bread_price.csv'
data = pd.read_csv(file_path)

# Rename the first column as 'Year' and clean up the rest of the columns
data.columns = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Drop rows where 'Year' is missing
data = data.dropna(subset=['Year'])

# Convert all columns to numeric (handle non-numeric values)
monthly_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data[monthly_columns] = data[monthly_columns].apply(pd.to_numeric, errors='coerce')

# Calculate the yearly average price, ignoring missing data
data['Yearly Average'] = data[monthly_columns].mean(axis=1)

# Ensure 'Year' is numeric and drop rows with non-numeric years
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
data = data.dropna(subset=['Year'])

# Plot the yearly average price
plt.figure(figsize=(10,6))
plt.plot(data['Year'], data['Yearly Average'], marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Average Bread Price per Year (U.S. City Average)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Price (USD)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
