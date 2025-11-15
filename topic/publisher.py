import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a topic exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# Routing key example: "kern.critical", "auth.info", etc.
routing_key = 'kern.'
message = 'A critical kernel error'

# Publish message
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(f" [x] Sent '{message}' with routing key '{routing_key}'")

connection.close()
