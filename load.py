# Load the Iris dataset
iris = load_iris()

# Convert to a Pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
df['species'] = iris.target

# Display the first few rows of the DataFrame
df.head()
