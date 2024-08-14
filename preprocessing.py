# Check for any missing values
df.isnull().sum()

# Map the species numbers to their names for better readability
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_map)

# Display the updated DataFrame
df.head()
