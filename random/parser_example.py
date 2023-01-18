# refrence: https://www.youtube.com/watch?v=cdblJqEUDNo

import argparse
import math
import sys  

parser = argparse.ArgumentParser(description="calculate volume of cylinder")
parser.add_argument('-r','--radious', type=int, metavar='', required=True,  help='radious of cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='height of cylinder')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quite', action='store_true', help='print quite')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')

args = parser.parse_args()

def cylinder_volume(radious, height):
	vol = (math.pi) * (radious ** 2) * (height)
	return(vol) 


if __name__ == '__main__':
	
	volume = cylinder_volume(args.radious, args.height)
	
	if args.quite:
		print (volume)
	
	elif args.verbose:
		print ("Volume of the Cylinder with radious %s and height %s is %s" % (args.radious, args.height, volume))
	
	else:
		print("The volume is %s", (volume))


