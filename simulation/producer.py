import json
from kafka import KafkaProducer
import pandas as pd
import time
from tqdm import tqdm
# from random import randint

bootstrap_servers = ['localhost:9092', 'localhost:9094']

topicName = 'trips'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

df = pd.read_csv("data/trips.csv")

header = [x for x in df.columns]
counter = 0
for i in tqdm(range(df.shape[0] // 3)):
    d = {}
    for j in range(len(header)):
        d[header[j]] = str(df[header[j]][i])
    msg = json.dumps(d)
    producer.send(topicName, msg.encode())
    # print(msg)
    time.sleep(0.001)
    counter += 1
print(f"Sent {counter} records")

# WORD_FILE = 'fake_data.txt'
# WORDS = open(WORD_FILE).read().splitlines()
# while True:
#     message = ''
#     for _ in range(randint(2, 7)):
#         message += WORDS[randint(0, len(WORDS) - 1)] + ' '
#     print(f">>> '{message}'")
#     producer.send(topicName, bytes(message, encoding="utf8"))
#     time.sleep(2)
