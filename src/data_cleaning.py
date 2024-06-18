import pandas as pd

def clean_data(file_path, output_path=None):
    """Cleans the meteorite data"""

    df = pd.read_csv(file_path)

    # Remove rows where year is greater than 2024
    df = df[df['year'] <= 2024]

    # Remove rows where fall is 'Fell'
    df = df[df['fall'] != 'Fell']

    # Remove rows where GeoLocation is (0.0, 0.0)
    df = df[df['GeoLocation'] != '(0.0, 0.0)']

    # Remove rows where GeoLocation is NaN
    df = df[df['GeoLocation'] != 'NaN']

    # Save the cleaned data to a new CSV file if output_path is provided
    if output_path:
        df.to_csv(output_path, index=False)

    return df

if __name__ == "__main__":
    # Define file paths
    input_file_path = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/data/Meteorite_Landings_20240617.csv'
    output_file_path = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/data/Meteorite_Landings_Cleaned.csv'

    # Clean the data and save it to a new file
    clean_data(input_file_path, output_file_path)
