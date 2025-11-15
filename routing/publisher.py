import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Routing keys (e.g., severity of logs)
severity = 'error'  # could be 'info', 'warning', 'error'
message = 'This is an error message'

# Publish the message with a routing key
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Sent '{message}' with severity '{severity}'")

connection.close()
