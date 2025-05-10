#%%
import pandas as pd
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

pkl_file_path = 'data/Politics_filtered.pkl'
data = pd.read_pickle(pkl_file_path)
data

#%%

columns = ['cntry','badge', 'bctprd', 'imwbcnt', 'imueclt',
           'imbgeco', 'impcntr', 'vote', 'trstun', 'trstprl', 'trstplt',
           'trstplc', 'trstlgl', 'trstep', 'stflife', 'stfhlth', 'stfedu',
           'stfeco', 'stfdem', 'sgnptit', 'polintr', 'lrscale', 'gincdif',
           'freehms', 'contplt', 'clsprty']
feature_columns = columns[1:]  # Exclude 'cntry' for clustering
data = data[columns]
data = data[data.cntry == 'FR'] 

features_df = data[feature_columns].copy()

for col in features_df.columns:
    try:
        features_df[col] = features_df[col].astype(int)
    except ValueError:
        print(f"Warning: Column {col} could not be converted to int. Check for non-numeric or NaN values.")

print(f"Features for clustering: {feature_columns}")
print(f"Shape of features_df: {features_df.shape}")

#%% --- 2. Determine Optimal Number of Clusters (k) using Elbow Method ---
print("--- 2. Determining Optimal k (Elbow Method) ---")
cost = []
K_range = range(2, 11) # Test k from 2 to 10 (1 cluster is trivial)

# Filter out columns with only one unique value if any, as they can cause issues with some K-Modes initializations
nunique = features_df.nunique()
cols_to_use_for_elbow = nunique[nunique > 1].index.tolist()
if len(cols_to_use_for_elbow) < len(features_df.columns):
    print(f"Warning: Dropping columns with only one unique value for elbow method: {set(features_df.columns) - set(cols_to_use_for_elbow)}")
features_df_elbow = features_df[cols_to_use_for_elbow]


if features_df_elbow.empty:
    print("Error: No features left after removing columns with single unique values. Cannot run K-Modes.")
else:
    for k_val in K_range:
        print(f"Calculating cost for k={k_val}...")
        try:
            # Using 'Cao' or 'Huang' for initialization. 'Cao' is often good.
            # n_init is important to avoid local optima.
            kmodes_model = KModes(n_clusters=k_val, init='Cao', verbose=0, n_init=5, random_state=42)
            kmodes_model.fit(features_df_elbow)
            cost.append(kmodes_model.cost_)
        except Exception as e:
            print(f"Error calculating K-Modes for k={k_val}: {e}")
            cost.append(float('inf')) # Add a large cost if error occurs

    # Plot the cost
    plt.figure(figsize=(10, 6))
    plt.plot(K_range, cost, 'bx-')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Cost (Dissimilarity)')
    plt.title('Elbow Method for K-Modes')
    plt.xticks(list(K_range))
    plt.grid(True)
    plt.show()

    # --- User Input for k ---
    # Based on the elbow plot, choose a k.
    # You would typically inspect the plot and pick the 'elbow' point.
    # For automation, one might look for the point of maximum curvature.
    chosen_k_input = input(f"Enter the chosen k based on the elbow plot (e.g., 3, 4, 5) or press Enter for default (e.g., 4): ")
    try:
        chosen_k = int(chosen_k_input)
    except ValueError:
        chosen_k = 4 # Default k if input is invalid or empty
        print(f"Invalid input or no input. Using default k={chosen_k}.")
    print(f"Chosen k: {chosen_k}\n")


#%% c  --- 3. Perform K-Modes Clustering with Chosen k ---
# Ensure chosen_k is at least 1 and not greater than number of samples
if chosen_k < 1:
    print("k must be at least 1. Setting k=2.")
    chosen_k = 2
if chosen_k > len(features_df):
    print(f"k ({chosen_k}) cannot be greater than the number of samples ({len(features_df)}). Setting k to 3 or num_samples if smaller.")
    chosen_k = min(3, len(features_df))


print(f"--- 3. Performing K-Modes Clustering with k={chosen_k} ---")
# Use the full features_df for the final clustering, not necessarily features_df_elbow
# if features_df was modified for elbow method due to single unique values.
# However, K-Modes might still struggle with columns having very few unique values or one value.
# It's best if your input features_df for KModes fit does not have columns with only 1 unique value.

final_features_df = features_df[cols_to_use_for_elbow] # Use the same features as for elbow or adjust
if final_features_df.empty:
    print("Error: No features available for final clustering. Exiting.")
    exit()

kmodes_final = KModes(n_clusters=chosen_k, init='Cao', verbose=1, n_init=10, random_state=42)
clusters = kmodes_final.fit_predict(final_features_df)

# Add cluster labels to the original dataframe (or a copy that includes all original columns)
data_with_clusters = data.copy() # Start with the full original data
data_with_clusters['cluster'] = clusters # clusters are based on final_features_df rows
print(f"\nCluster assignments added. Example (first 5 rows with cluster and first 3 features):")



