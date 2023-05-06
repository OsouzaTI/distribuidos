#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('172.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')