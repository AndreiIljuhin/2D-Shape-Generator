"""
wrapper functions and definitions for basic shapes

Timo Flesch, 2017
"""
import cairo
import math 

def drawRect(ctx,centre,size):
	ctx.rectangle(0-(size)/2,0-(size)/2,size,size)
	return ctx

def drawPolygon(ctx,centre,size,numVertices=4):
	circ = 2*math.pi
	angle = circ/numVertices
	coords = [(math.sin(angle*ii)*size,math.cos(angle*ii)*size) for ii in range(numVertices)]
	for ii in coords:
		ctx.line_to(ii[0],ii[1])	
	return ctx

def drawStar(ctx,centre,outerRadius,innerRadius,numVertices=5):
	circ = 2*math.pi
	angle = circ/(numVertices*2)
	coords = []
	for ii in range(numVertices*2):
		r = innerRadius if ii%2 else outerRadius
		coords.append([math.sin(angle*ii)*r,math.cos(angle*ii)*r])
	# coords = [[sum(translate_op) for translate_op in zip(coordPair,centre)]for coordPair in coords]
	
	for ii in coords:
		ctx.line_to(ii[0],ii[1])
	# ctx.close_path()
	return ctx


def drawEllipse(ctx,centre,size):
	ctx.arc(0,0,size,0,math.pi*2)
	return ctx
