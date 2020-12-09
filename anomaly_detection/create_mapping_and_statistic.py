import numpy as np
import pandas as pd
from tqdm import tqdm
# import seaborn as sns
import yaml

s = pd.read_csv('data/trips.csv')

columns = [
    ('ArrivalTime', 'continous'),
    ('BusinessLeisure', 'categorical'),
    ('CabinCategory', 'categorical'),
    ('CreationDate', 'continous'),
    ('CurrencyCode', 'categorical'),
    ('DepartureTime', 'continous'),
    ('Destination', 'categorical'),
    ('OfficeIdCountry', 'categorical'),
    ('Origin', 'categorical'),
    ('TotalAmount', 'continous'),
    ('nPAX', 'continous'),
]


def process_continous(series) -> (float, float):
    series = series.dropna()
    s = series.describe()
    return float(s['mean']), float(s['std'])


def process_categorical(series) -> (dict, float, float):
    series = series.dropna()
    unique_values = list(series.unique())
    mapping = {}
    for i in range(len(unique_values)):
        mapping[str(unique_values[i])] = i
    s = []
    for v in series:
        s.append(mapping[str(v)])
    s = np.array(s)
    return mapping, float(s.mean()), float(s.std())

d = {}

for column, t in tqdm(columns):
    if t == 'continous':
        mean, std = process_continous(s[column])
        d[column] = {
            'statistic': {'mean': mean, 'std': std}
        }
    elif t == 'categorical':
        mapping, mean, std = process_categorical(s[column])
        d[column] = {
            'mapping': mapping,
            'statistic': {'mean': mean, 'std': std}
        }

with open('src/notebook-spark-streaming-slow-branch/mapping_and_statistic.yml', 'w') as outfile:
    yaml.dump(d, outfile)
