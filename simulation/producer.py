import argparse
import json
from kafka import KafkaProducer
import pandas as pd
import time
from tqdm import tqdm
import random

RATE_FAKE_EVENT = 0.5

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=1000)
parser.add_argument("--ack", type=str, choices=['0', '1', 'all'], default='1')
parser.add_argument("--delay", type=float, default=0.1)
args = parser.parse_args()

bootstrap_servers = ['localhost:9092', 'localhost:9094', 'localhost:9095']
topicName = 'trips'

if args.ack == 'all':
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, acks=args.ack)
else:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, acks=int(args.ack))

df = pd.read_csv("data/small_trips.csv")

header = [x for x in df.columns]
counter = 0
s1 = time.time()

t1 = time.time()
# delay for test
tmp = -1
while int(t1) % 10 != 0:
    if tmp != int((10 - (int(t1)%10))):
        tmp = int((10 - (int(t1)%10)))
        print(f'Waiting for sending data {tmp} seconds left')
    t1 = time.time()

print('Starting sending data ...')

k = 0
t2 = t1
for i in tqdm(range(args.n)):
    t2 = time.time()
    if t2 - t1 >= 10:
        t1 = t2
        k += 1
        k %= 3
    # print(k)
    d = {}
    d['ID'] = i
    for j in range(len(header)):
        d[header[j]] = str(df[header[j]][i])
    msg = json.dumps(d)
    # rate of fake late event
    
    # if (rd_fake_late < RATE_FAKE_EVENT):
    #     # time for late
    #     late_time = random.randint(0, 10)
    #     now = time.time()
    #     producer.send(topic=topicName, value=msg.encode(), timestamp_ms=int(now) * 1000 - late_time * 1000)
    # else:
    if k == 2:
        rd_fake_late = random.uniform(0, 1)
        if rd_fake_late < RATE_FAKE_EVENT:
            print("late event")
            now = time.time()
            producer.send(topic=topicName, value=msg.encode(), timestamp_ms=int(now) * 1000 - 10 * 1000)
        else:
            producer.send(topic=topicName, value=msg.encode())
    else:
        producer.send(topic=topicName, value=msg.encode())
    time.sleep(args.delay)
    counter += 1
s2 = time.time()
print(f"Sent {counter} records in {s2 - s1} seconds")
print(f"Sending rate: {counter / (s2 - s1)} records/s")

