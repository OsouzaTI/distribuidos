import pika
import psutil
import time

class CpuTemperatura:

    def __init__(self) -> None:        
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='temperatura')

    def ler_temperatura(self):
        temperature = psutil.sensors_temperatures()['coretemp'][0].current
        self.channel.basic_publish(exchange='', routing_key='temperatura', body=str(temperature))

    def run(self):
        while True:
            self.ler_temperatura()
            time.sleep(5)
        
cpu = CpuTemperatura()
cpu.run()
