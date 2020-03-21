#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.2'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'General'
message = ' '.join(sys.argv[2:]) or 'Mensaje por defecto'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Se envió el siguiente mensaje a %r:%r" % (severity, message))
connection.close()
