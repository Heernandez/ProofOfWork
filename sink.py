import random
import zmq
import time

context = zmq.Context()
# Socket para recibir respuestas
fan = context.socket(zmq.PULL)
fan.bind("tcp://*:5558")

# Esperar a recibir confirmacion del fan
y = fan.recv()
y = y.decode('utf-8')
y = int(y)

# Capturar tiempo inicial
tStart = time.time()

for task in range(y):
    s = fan.recv()
    print("The Answer is :",s.decode('utf-8'))
    
tEnd = time.time()

print("El tiempo total fue de  : %d sec" % ((tEnd - tStart)))

for task in range(3):
    s = fan.recv()