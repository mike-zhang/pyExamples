#! /usr/bin/env python3
#-*- coding:utf-8 -*-

from kafka import KafkaConsumer

#consumer = KafkaConsumer('test', group_id= 'group2', bootstrap_servers= ['localhost:9092'])
consumer = KafkaConsumer('test',bootstrap_servers=['localhost:9092'])
for msg in consumer:
    print(msg)


