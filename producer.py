import json
from kafka import KafkaProducer
import pandas as pd
import time

bootstrap_servers = ['localhost:19092', 'localhost:29092', 'localhost:39092']

topicName = 'test'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

df = pd.read_csv("small_trips.csv")
header = [x for x in df.columns]
for i in range(df.shape[0]):
    s = df.iloc[i, :]
    d = {}
    for j in range(len(header)):
        d[header[j]] = str(s[j])
    msg = json.dumps(d)
    producer.send(topicName, msg.encode())
    print(msg)
    time.sleep(1)
