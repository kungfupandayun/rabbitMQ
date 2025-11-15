import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same topic exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# Create a temporary queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Bind the queue to patterns
binding_keys = ['kern.*', '*.critical']  # '*' = one word, '#' = zero or more words
for key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Received {method.routing_key}: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
