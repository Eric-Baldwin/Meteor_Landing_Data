import pandas as pd

def load_data():
    filepath = '/home/eric_baldwin/ddiMain/midterm/Meteor_Landing_Data/data/Meteorite_Landings_Cleaned.csv'
    return pd.read_csv(filepath)
