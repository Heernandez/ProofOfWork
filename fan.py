import random
import zmq
import time
import hashlib


def hashString(s):
    # Recibe una cadena y calcula el sha256
    sha = hashlib.sha256()
    sha.update(s.encode('ascii'))
    return sha.hexdigest()

context = zmq.Context()

# Socket with workers
workers = context.socket(zmq.PUSH)
workers.bind("tcp://*:5557")

# Socket with sink
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press enter when workers are ready ...")
_ = input()

sink.send(b'1')

challenge = hashString("Hernandez")

for i in range(4):
    print("sending task to workers")
    workers.send_string(challenge)
''''
while True:
    pass
'''