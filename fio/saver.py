"""
wrapper to save as matlab-compatible file
"""
# import pickle
from scipy.io import savemat

def saveData(data,dimensions,shapes,outDir, name):
	fileName = outDir + name + "_" + "_".join(shapes) + "_dims_" + "_".join(dimensions)
	savemat(fileName+'.mat',data)
