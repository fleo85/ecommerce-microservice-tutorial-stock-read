import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqhost'))
channel = connection.channel()

channel.queue_declare(queue='products')

product = {
            "id": 1232,
            "nome": "pasta",
            "produttore": "Molisana",
            "quantita": 2
          }

channel.basic_publish(exchange='', routing_key='products', body=json.dumps(product))
print(f" [x] Sent {product}")

connection.close()

