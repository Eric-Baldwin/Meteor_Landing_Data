import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def vis_mass_dist(df):
    """Visualizes the mass distribution of the meteorites."""
# Directory to save visualizations
    save_dir = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/visualizations'
    os.makedirs(save_dir, exist_ok=True)

# Plot the distribution of meteorite masses
    plt.figure(figsize=(10, 2))
    df['mass (g)'].hist(bins=5)
    plt.title('Distribution of Meteorite Mass')
    plt.xlabel('Mass (g)')
    plt.ylabel('Frequency')

# Save the plot as a PNG file
    plt.savefig(os.path.join(save_dir, 'mass_distribution.png'))