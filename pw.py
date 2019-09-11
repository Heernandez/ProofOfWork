import string
import random
from pw import hashString

def generation(challenge, size = 25):
    answer = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                      for x in range(size))
    attempt = challenge + answer
    return attempt, answer

def proofOfWork(challenge):
    found = False
    attempts = 0
    while not found:
        attempt, answer = generation(challenge, 64)
        #print(attempt)
        hash = hashString(attempt)
        if hash.startswith('0000'):
            found = True
            print(hash)
        attempts += 1
    print(attempts)
    return answer

# Challenge string will be the last block
#challenge = hashString("CS-rocks!")
#answer = proofOfWork(challenge)
#print(answer)
