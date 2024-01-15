# Grouping the data by 'region' and counting unique 'state' values for each region
import pandas as pd
data = pd.read_csv('/Users/Asus/Desktop/vehicles.csv')
unique_states_per_region = data.groupby('region')['state'].nunique()

# Identifying regions with more than one unique state
regions_with_multiple_states = unique_states_per_region[unique_states_per_region > 1]

print(regions_with_multiple_states)
