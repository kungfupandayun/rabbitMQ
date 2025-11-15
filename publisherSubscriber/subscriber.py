import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same fanout exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Create a temporary queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to the exchange
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Callback function to handle messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# Subscribe to the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Start consuming
channel.start_consuming()
