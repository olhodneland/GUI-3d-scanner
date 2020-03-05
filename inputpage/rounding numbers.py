import math

#a = 3.85
#print(math.floor(a))

#number_dec = 1 + (a-int(a))

#print("%.2f" % number_dec)

zAxisLength = float(25.7557392)

#x = (str(zAxisLength)).split('.', 1)
#x1 = (x[1])
#numbers = len(x1)
#print(numbers)


#x = len((str(zAxisLength)).split('.', 1)[1])
#print(x)

zAxisLength = float(205.3)
zAxisRes = float(1.3)

zLayers = float(math.ceil(zAxisLength/zAxisRes))
zHeight = zAxisRes*zLayers

print(zHeight)
