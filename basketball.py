import pandas as pd
import matplotlib.pyplot as plt

#csv from https://www.basketball-reference.com/leagues/NBA_stats_totals.html
# Step 1: Load the data from nba.csv
df = pd.read_csv('Chapter_11/nba.csv')

# Step 2: Extract the relevant columns
df_new = df[['FG', '3P', 'FT']]

# Step 3: Rename the columns
df_new.columns = ['FGM', '3PM', 'FTM']

# Step 4: Save the new data to a new file called newnba.csv
df_new.to_csv('Chapter_11/newnba.csv', index=False)

# Step 5: Load the new data from newnba.csv
df_loaded = pd.read_csv('Chapter_11/newnba.csv')

# Step 6: Visualize the data using a bar plot
df_loaded.plot(kind='bar', figsize=(10, 6))
plt.title('FGM, 3PM, and FTM Data')
plt.xlabel('Index')
plt.ylabel('Values')
plt.xticks(rotation=0)
plt.legend(['FGM', '3PM', 'FTM'])
plt.tight_layout()

# Show the plot
plt.show()
