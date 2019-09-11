import sys,time,zmq
from pw import *

context = zmq.Context()

w = context.socket(zmq.PULL)
w.connect("tcp://localhost:5557")

# Socket to send responses
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")


print(" a recibir")
s = w.recv_string()
print("recibo :",s)    
print(" Working....")

answer = proofOfWork(s)
try:
    sink.send_string(answer)
except:
    pass


    

