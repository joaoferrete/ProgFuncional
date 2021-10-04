from math import pi
def areaVolume (r):
	area= 4*pi*r**2
	volume=(4*pi*r**3)/3
	print ("A Área é {} e o volume é {}".format(area, volume))
	return area, volume
areaVolume(2)
print(areaVolume(2))
