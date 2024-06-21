import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def top_3_found_hist(df):
    """Visualizes the top 3 meteorite types found over the years."""
# Directory to save visualizations
    save_dir = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/visualizations'

# Define the top 3 recclass
    top_3_recclass = [
        'L6',
        'H5',
        'L5'
    ]

# Filter the DataFrame to only include rows with a year >= 1970
    df = df[df['year'] >= 1970.0]

# Filter the DataFrame to only include rows with the top 5 recclass
    df_top_3 = df[df['recclass'].isin(top_3_recclass)]

    # Define colors for the histograms
    color_map = {'L6': 'blue', 'H5': 'orange', 'L5': 'green'}

# Plot individual histograms for the top 3 recclass
    plt.figure(figsize=(12, 8))

    for i, recclass in enumerate(top_3_recclass, 1):
        plt.subplot(3, 1, i)
        sns.histplot(df_top_3[df_top_3['recclass'] == recclass]['year'], bins=30, color=color_map[recclass])
        plt.title(f'Histogram of {recclass} Found Over the Years (1970 - 2012)')
        plt.xlabel('Year')
        plt.ylabel('Number of Meteorites Found')
        plt.ylim(0, 1000)
        plt.xlim(1970, 2012)
        plt.grid(True)
        plt.tight_layout()


    # Save the plot
    plt.savefig(os.path.join(save_dir, 'top_3_found_hist.png'))
    plt.close()
