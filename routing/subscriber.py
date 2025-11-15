import pika
import sys

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Create a temporary queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Subscribe to specific severities
severities = ['error', 'warning']  # can choose which messages to receive
for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Received {method.routing_key}: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
