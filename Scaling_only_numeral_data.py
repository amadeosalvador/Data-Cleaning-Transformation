# Amadeo Salvador 2-14-23

###   Simple Python code to scale on numeral variables of dataset lipidomics 200 for LASSO analysis   ###
# Lipidomics200 has HIPPA data, so it not available here.

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Concatenates the data1 and data2:
data_combined= pd.concat([data1, data2], axis=1)
##Scaling only the numerical data (removing non numeric or binary to add again later)
data_combined_cols = data_combined.columns
binary_columns = [col for col in data_combined_cols if data_combined[col].nunique() <= 2]

# Convert binary columns to numeric data type
binary_data = data_combined[binary_columns].astype('float')
non_binary_columns = data_combined.select_dtypes(exclude=[np.number, 'bool']).columns
categ_data = data_combined[non_binary_columns].astype('object')

# Select only numeric columns for scaling
numeric_columns = [col for col in data_combined.columns if col not in binary_columns and col not in non_binary_columns]
numeric_data = data_combined[numeric_columns]

# Scale the numeric columns
scaler = StandardScaler()
scaled_numeric_data = scaler.fit_transform(numeric_data)
scaled_numeric_data = pd.DataFrame(scaled_numeric_data, columns=numeric_data.columns, index=numeric_data.index)

# Combine the binary and scaled numeric data
scaled_data_combined = pd.concat([scaled_numeric_data, binary_data,categ_data], axis=1)
scaled_data_combined
