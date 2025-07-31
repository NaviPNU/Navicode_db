import pandas as pd
import numpy as np


df = pd.read_csv('starbucks.csv', encoding='cp949')

def calculate_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

navicode = '3232'
latitude = '35.825591'
longitude = '128.754325'
lati = float(latitude)
long = float(longitude)
result = df[df['navicode'].str.startswith(navicode)]
result['distance'] = result.apply(
    lambda row: calculate_distance(lati, long, row[2], row[3]), axis=1
    )

nearest = result.sort_values(by='distance').head(10)

output = []
for _, row in nearest.iterrows():
    output.append({
        'name': row[0],
        'latitude': row[2],
        'longitude': row[3]
    })



print(output)