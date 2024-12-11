import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('output_data.csv')

# Access data in the DataFrame using column names or indexing
print("Length of data(row):", len(df))
#print("Inspect column policy", df['policy'])
print("Length of column", len(df.iloc[0]))
print("Access first row:")
print(df.iloc[0])
print("Length of the first column:", len(df.iloc[0][0]), "Type: ", type(df.iloc[0][0]))
print(df.iloc[0][0])
print("Length of the second column:", len(df.iloc[0][1]), "Type: ", type(df.iloc[0][1]))


print("##############################################################")
# import csv

# # Open the CSV file in read mode
# with open('output_data.csv', 'r') as csvfile:
#   # Create a reader object
#   csv_reader = csv.reader(csvfile)
  
#   # Iterate through the rows in the CSV file
#   for row in csv_reader:
#     # Access each element in the row
#     print(row)



import pandas as pd
import numpy as np
import ast  # To safely evaluate string representations of lists

# Read the CSV file into a DataFrame
df = pd.read_csv('output_data.csv')

# Process the 'policy' column to fit the shape of action
# Convert the string into a list of floats
df['policy'] = df['policy'].apply(ast.literal_eval)

# Convert to numpy array of appropriate dtype
actions = np.array(df['policy'].tolist(), dtype=np.float32)

# Check shape
print("Shape of actions:", actions.shape)

# Process the 'sampled_points' column to fit the shape of point_cloud
df['sampled_points'] = df['sampled_points'].apply(ast.literal_eval)

# Convert to numpy array of appropriate dtype
point_clouds = np.array(df['sampled_points'].tolist(), dtype=np.float32)

# Check shape
print("Shape of point clouds:", point_clouds.shape)

# Example: Accessing one action and one point cloud
action = actions[0]  # First row's action
point_cloud = point_clouds[0]  # First row's point cloud

print("Action shape:", action.shape, "Point cloud shape:", point_cloud.shape)


# Output:
# Shape of actions: (423, 1, 18)
# Shape of point clouds: (423, 1024, 3)
# Action shape: (1, 18) Point cloud shape: (1024, 3)
