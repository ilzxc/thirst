from random import random
from instruments import *
from odotsetup import *
import socket

def grab(indices, coll):
	result = []
	for ind in indices:
		result.append(coll[ind])
	return result

def find(item, coll, coll2 = None):
	result = []
	for ind, val in enumerate(coll):
		if val == coll[ind]: result.append(ind) 
	if coll2 is None:
		return result
	else: return grab(result, coll2)

def frange(end, step):
	i = 0.0
	result = []
	while i < end:
		result.append(i)
		i += step
	return result

def staticRhythm(time, numEvents = -1):
	if numEvents is -1:
		numEvents = int(round(time * (random() * 2 + 3)))
	return frange(time, time / numEvents)

def randomAmps(events):
	result = [random() * 0.25 + 0.50]
	for e in events[1:]:
		result.append(result[-1:][0] + random() * .1 - .05)
	return result

def make_staccs(instrs):
	bndls = []
	for instr in instrs:
		coll = samples[instr]['staccato']
		sample = coll[int(random() * len(coll))][0]
		times = staticRhythm(2.33)
		amps = randomAmps(times)
		b = o.bundle(messages = [
			o.message('/sample', sample),
			o.message('/times', times),
			o.message('/amps', amps)
		])
		bndls.append(b)
	return bndls



### udp socket stuff:
#RINFO = ('127.0.0.1', 56765)
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print("Sending udp packets to " + str(RINFO))
def send(message, RINFO): 
	sock.sendto(message.getBytes(), RINFO) ### assumes o.bundle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
base_port = 56765
for i, b in enumerate(make_staccs(['violin', 'viola', 'cello', 'oboe'])):
	send(b, ('127.0.0.1', base_port + i))
