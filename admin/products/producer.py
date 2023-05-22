import pika

params = pika.URLParameters('amqps://waezmnsx:5ATtwcDKyZKVkAqxbGbW3mvrXcbfSlyv@goose.rmq2.cloudamqp.com/waezmnsx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello world')