import json
import pika, django, os

from products.models import Product


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()

params = pika.URLParameters('amqps://waezmnsx:5ATtwcDKyZKVkAqxbGbW3mvrXcbfSlyv@goose.rmq2.cloudamqp.com/waezmnsx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

if channel.is_open:

    channel.queue_declare(queue='admin')

    def callback(ch, method, properties, body):
        print('Received in Admin')
        print(body)
        id = json.loads(body)
        print(id)
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        product.save()
        print('Product likes imcreased')
    

    channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

    print('Started Consuming')

    channel.start_consuming()

    channel.close()
else :
    print('Failed to consume')