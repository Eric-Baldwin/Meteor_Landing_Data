import os
from data_loading import load_data
from visualization_scripts.vis_mass_dist import vis_mass_dist
from visualization_scripts.vis_avg_mass import vis_avg_mass

def main():
    # Load data
    data = load_data()

    # Visualize data
    vis_mass_dist(data)
    vis_avg_mass(data)

if __name__ == "__main__":
    main()
