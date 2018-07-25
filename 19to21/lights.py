import itertools as it
import sys
import time

counter = 0
lights = ['Green', 'Amber', 'Red']
traffic_lights = it.cycle(lights)

while counter < 7:
    sys.stdout.write(next(traffic_lights) + '\n')
    sys.stdout.flush()
    time.sleep(3)
    counter += 1