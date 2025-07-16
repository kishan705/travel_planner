import pandas as pd

# Load dataset
DF = pd.read_csv("data/worldcities.csv")

# Drop rows where city name is missing
DF = DF.dropna(subset=["city"])

# Build dictionary: city_name -> (lat, lng)
CITY_COORDS = {
    row.city.lower(): (row.lat, row.lng)
    for _, row in DF.iterrows()
}

def validate_city(city):
    return city.lower() in CITY_COORDS

def get_coordinates(city):
    return CITY_COORDS.get(city.lower())
