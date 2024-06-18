import os
from data_loading import load_data
from visualization_scripts.vis_mass_dist import vis_mass_dist

def main():
    # Load data
    data = load_data()

    # Visualize data
    vis_mass_dist(data)

if __name__ == "__main__":
    main()
