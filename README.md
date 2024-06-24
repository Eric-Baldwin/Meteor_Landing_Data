# Meteor_Landing_Data

## Overview

This project involves the exploratory data analysis (EDA) of meteorite landing data. The aim is to analyze various aspects of the meteorite landings, such as their mass distributions, classifications, and the years they were found. The analysis is performed using Python and several data analysis and visualization libraries, including Pandas, Matplotlib, and Seaborn.


## Data

### Description

The dataset used in this project contains information about various meteorite landings. Key columns in the dataset include:
- `name`: The name of the meteorite.
- `id`: A unique identifier for the meteorite.
- `recclass`: The classification of the meteorite.
- `mass (g)`: The mass of the meteorite in grams.
- `fall`: Indicates whether the meteorite was found or fell.
- `year`: The year the meteorite was found or observed falling.
- `reclat`: The latitude where the meteorite was found.
- `reclong`: The longitude where the meteorite was found.
- `GeoLocation`: A combination of the latitude and longitude.

### Cleaning Process

The data cleaning script (`data_cleaning.py`) performs the following tasks:
- Removes rows where the year is greater than 2024.
- Removes rows where the meteorite's fall status is 'Fell'.
- Removes rows where GeoLocation is (0.0, 0.0).
- Removes rows where GeoLocation is NaN.

## Analysis

### Exploratory Data Analysis (EDA)

The EDA is conducted through a series of Jupyter Notebooks located in the `notebooks` directory. These notebooks include:
- **initial_notes.ipynb**: Initial exploration and understanding of the dataset.
- **info_gathering.ipynb**: Gathering specific information and insights from the data.
- **avg_mass_charts.ipynb**: Analysis and visualization of average mass distributions.
- **L6.ipynb**: Detailed analysis of meteorites classified as L6.
- **pallasite.ipynb**: Focused analysis on meteorites classified as Pallasite. (Unused in final project)
- **top_3_mass.ipynb**: Comparative analysis of the top 3 meteorite classes by mass.
- **years.ipynb**: Analysis of meteorite finds over different years.

### Visualizations

Various visualizations are created to analyze the meteorite data. The scripts for these visualizations are located in the `src/visualization_scripts` directory. Key visualizations include:

#### Mass Distribution Boxplots
- **`found_avg_mass_big.py`**: Generates box plots showing the mass distribution of found meteorites.
  - **found_avg_mass_big.png**: Full range mass distribution.
  - **found_avg_mass_big_trunc.png**: Truncated mass distribution up to 1000g.

- **`found_avg_mass_small.py`**: Generates box plots showing the mass distribution of smaller found meteorites.
  - **found_avg_mass_small.png**: Full range mass distribution.
  - **found_avg_mass_small_trunc.png**: Truncated mass distribution up to 1000g.

#### Top 3 Found Meteorites Histogram
- **`top_3_found_hist.py`**: Creates histograms for the top 3 meteorite classifications (L6, H5, L5) found over the years.
  - **top_3_found_hist.png**: Displays histograms with specified colors for each classification.

#### Top 3 Found Meteorites KDE Plot
- **`top_3_found_kde.py`**: Creates KDE plots for the top 3 meteorite classifications (L6, H5, L5) found over the years.
  - **top_3_found_kde.png**: Displays KDE plots for each classification.

#### Total Found Meteorites
- **`total_found_big.py`**: Analysis of total found over all years.
  - **total_found_big.png**: Displays the analysis results in a line plot.

- **`total_found_small.py`**: Analysis of total found meteorites between 1970-2012.
  - **total_found_small.png**: Displays the analysis results in a line plot.

## Running the Analysis

### Prerequisites

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

### Setup

1. Clone the repository:
   - SSH
   - git clone git@github.com:Eric-Baldwin/Meteor_Landing_Data.git
   - cd Meteor_Landing_Data
   - pip install pandas matplotlib seaborn jupyter
   - save csv file from https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data into data directory
   - cd src
   - edit the "input_file_path" in line 28 of the data_cleaning.py script with the path to the csv you just saved
   - python data_cleaning.py
   - python main.py



---------------------------------------------------------------------------s






DDI Midterm project




----- Where your dataset can be found

https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data



----- Submit the link to your repository below.

https://github.com/Eric-Baldwin/Meteor_Landing_Data




----- What is the shape of your dataset (rows, columns)?

45,716 x 10



----- Describe the available fields.

There are 8 categorical fields (name, id, nametype, recclass, fall, reclat, reclong, GeoLocation)

name: Represents the name of the entity.
id: Represents a unique identifier for the entity.
nametype: Represents the type of name.
recclass: Represents the classification of the entity.
fall: Represents whether the entity fell or was found.
reclat: Represents the latitude as text.
reclong: Represents the longitude as text.
GeoLocation: Represents the geographical location.

There are 2 quantitative fields (mass, year)

mass (g): Represents the mass in grams.
year: Represents the year as a floating timestamp.

There is some missing data but not enough to hinder analysis in my opinion.

Missing data points:
name                0
id                  0
nametype            0
recclass            0
mass (g)            131
fall                0
year                291
reclat              7315
reclong             7315
GeoLocation         7315

The data has not been summarized. This is raw data.



----- Potential avenues of inquiry

What is the average mass of a meteorite that is observed?

Is there a min mass a meteorite has in order to be found?

Are there areas on the globe where meteorites strike more than others?

Are meteorites being found more in the current time or in the past?

What percent of observed meteorites are found?

Are meteorites found in certain places more than others?





----- Value proposition

Stakeholders may want to aquire fallen meteorites. By studying data about where they fall, how big they are and where they are found, there might be a way to focus on certain areas of the globe which have a higher chance of collecting fallen meteorites.

