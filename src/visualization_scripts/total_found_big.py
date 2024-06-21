import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

def total_found_big(df):
    """Visualizes the top 3 meteorite types found over the years."""
# Directory to save visualizations
    save_dir = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/visualizations'

# Group by year and count the number of meteorites found each year
    meteorites_per_year = df['year'].value_counts().sort_index()
    meteorites_per_year.head()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=meteorites_per_year.index, y=meteorites_per_year.values)
    plt.title('Number of Meteorites Found Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Meteorites Found')
    plt.grid(True)


    # Save the plot
    plt.savefig(os.path.join(save_dir, 'total_found_big.png'))
    plt.close()
