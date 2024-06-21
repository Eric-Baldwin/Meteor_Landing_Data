import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def found_avg_mass_small(df):
    """Visualizes the average mass of all found items."""
# Directory to save visualizations
    save_dir = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/visualizations'

# Define the top 3 recclass
    top_3_recclass = ['L6', 'H5', 'L5']

# Filter the DataFrame to only include rows with the top 3 recclass
    df_top_3 = df[df['recclass'].isin(top_3_recclass)]

# Plot the boxplots for mass distribution comparison
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='recclass', y='mass (g)', data=df_top_3, palette=['blue', 'orange', 'green'])
    plt.title('Mass Distribution Comparison of L6, H5, L5 Meteorites')
    plt.xlabel('Top 3 Meteorites Found')
    plt.ylabel('Mass (g)')
    plt.ylim(0, 60000000)
    plt.grid(True)


# Save the plot
    plt.savefig(os.path.join(save_dir, 'found_avg_mass_small.png'))
    plt.close()

# Plot the boxplots for mass distribution comparison truncated
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='recclass', y='mass (g)', data=df_top_3, palette=['blue', 'orange', 'green'])
    plt.title('Mass Distribution Comparison of L6, H5, L5 Meteorites (Truncated)')
    plt.xlabel('Top 3 Meteorites Found')
    plt.ylabel('Mass (g)')
    plt.ylim(0, 500)
    plt.grid(True)


# Save the plot
    plt.savefig(os.path.join(save_dir, 'found_avg_mass_small_trunc.png'))
    plt.close()