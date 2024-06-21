import os
from data_loading import load_data
from visualization_scripts.found_avg_mass_big import found_avg_mass_big
from visualization_scripts.found_avg_mass_small import found_avg_mass_small
from visualization_scripts.top_3_found_hist import top_3_found_hist
from visualization_scripts.top_3_found_kde import top_3_found_kde
from visualization_scripts.total_found_big import total_found_big
from visualization_scripts.total_found_small import total_found_small

def main():
    # Load data
    data = load_data()

    # Visualize data
    top_3_found_hist(data)
    top_3_found_kde(data)
    found_avg_mass_big(data)
    found_avg_mass_small(data)
    total_found_big(data)
    total_found_small(data)

if __name__ == "__main__":
    main()
