import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def vis_avg_mass(df):
    """Visualizes the average mass of all found items."""
# Directory to save visualizations
    save_dir = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/visualizations'

# Extract the masses for found and fell items
    mass_found = df[df['fall'] == 'Found']['mass (g)']
    mass_fell = df[df['fall'] == 'Fell']['mass (g)']

# Create a DataFrame suitable for Seaborn
    data = {
        'Mass (g)': pd.concat([mass_found, mass_fell]),
        'Category': ['Found'] * len(mass_found) + ['Fell'] * len(mass_fell)
        }
    plot_df = pd.DataFrame(data)

# Create a box plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Category', y='Mass (g)', data=plot_df)
    plt.title('Mass Distribution of Found vs Fell Meteorites')
    plt.ylabel('Mass (g)')
    plt.xlabel('')

# Set y-axis limits
    plt.ylim(0, plot_df['Mass (g)'].max() / 10)

    plt.savefig(os.path.join(save_dir, 'mass_comparison_boxplot.png'))