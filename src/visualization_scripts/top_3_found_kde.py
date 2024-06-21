import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def top_3_found_kde(df):
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

    # Filter the DataFrame to only include rows with the top 3 recclass
    df_top_3 = df[df['recclass'].isin(top_3_recclass)]

    # Plot the KDE plots for the top 3 in recclass column
    plt.figure(figsize=(12, 8))
    for recclass in top_3_recclass:
        sns.kdeplot(df_top_3[df_top_3['recclass'] == recclass]['year'], label=recclass, fill=True)
    plt.xticks(range(int(df['year'].min()), int(df['year'].max()) + 1, 5))
    plt.title('Top 3 Meteorite Types Found Over the Years (1970 - 2012)')
    plt.xlabel('Year')
    plt.ylabel("Meteorites Found")
    plt.legend()
    plt.grid(True)


    # Save the plot
    plt.savefig(os.path.join(save_dir, 'top_3_found_kde.png'))
    plt.close()
