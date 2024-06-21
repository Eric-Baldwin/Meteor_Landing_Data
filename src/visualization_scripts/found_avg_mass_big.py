import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def found_avg_mass_big(df):
    """Visualizes the average mass of all found items."""
# Directory to save visualizations
    save_dir = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/visualizations'

# Extract the masses for all items in the mass (g) column
    mass_found = df['mass (g)']

    # Create a box plot using Seaborn
    plt.figure(figsize=(4, 6))
    sns.boxplot(y=mass_found)
    plt.title('Mass Distribution of Found Meteorites')
    plt.ylabel('Mass (g)')
    plt.ylim(0, mass_found.max())
    plt.grid(True)

    # Save the plot
    plt.savefig(os.path.join(save_dir, 'found_avg_mass_big.png'))
    plt.close()

    # Create a truncated box plot
    plt.figure(figsize=(6, 6))
    sns.boxplot(y=mass_found)
    plt.title('Mass Distribution of Found Meteorites (Truncated)')
    plt.ylabel('Mass (g)')
    plt.ylim(0, 500)
    plt.grid(True)

    # Save the plot
    plt.savefig(os.path.join(save_dir, 'found_avg_mass_big_trunc.png'))
    plt.close()
