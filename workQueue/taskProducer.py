import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a durable queue
channel.queue_declare(queue='task_queue', durable=True)

# Messages: simulate tasks
tasks = ['Task 1...', 'Task 2..', 'Task 3....']
for task in tasks:
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=task,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(f" [x] Sent {task}")
    #time.sleep(1)  # simulate delay

connection.close()
