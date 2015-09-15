import math

angle = 0
for angle in range(91):
    sine = math.sin(angle*math.pi/180)
    star = math.trunc(sine*80)
    if angle == 0:
        print '*'
    print (star)*' ','*'
