import pika
from termcolor import colored

from Constantes import FOGO_DETECTADO, AGUARDANDO

class DetectaFogo:

    def __init__(self) -> None:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='temperatura')
        self.channel.queue_declare(queue='fogo_detectado')

    def run(self):

        def callback(ch, method, properties, body):
            temperature = float(body)
            if temperature > 50:
                self.channel.basic_publish(exchange='', routing_key='fogo_detectado', body=FOGO_DETECTADO)
                print(colored(FOGO_DETECTADO,'red'))
            else:
                print('Temperatura:', temperature)

        self.channel.basic_consume(queue='temperatura', on_message_callback=callback, auto_ack=True)

        print(AGUARDANDO)
        self.channel.start_consuming()

detecta = DetectaFogo()
detecta.run()
