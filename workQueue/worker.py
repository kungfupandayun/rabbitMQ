import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# Only give one message to worker at a time
#channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    #time.sleep(body.count(b'.'))  # simulate work
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # acknowledge message

channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
