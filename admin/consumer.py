import pika

params = pika.URLParameters('amqps://waezmnsx:5ATtwcDKyZKVkAqxbGbW3mvrXcbfSlyv@goose.rmq2.cloudamqp.com/waezmnsx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in Admin')
    print(body)
 

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()