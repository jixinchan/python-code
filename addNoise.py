"""
#对某图片添加椒盐噪声(此处为3通道图片)
"""
def addNoise(filename):
	import cv2
	import random
	import numpy as np

	im = cv2.imread(filename)
	cv2.imshow('original img',im)
	h,w = im.shape[0:2]
	pNum = h*w
	nRate = 0.3
	for r in range(int(pNum*nRate)):
		randh = random.randint(0,h-1)
		randw = random.randint(0,w-1)
		#print(h,randh,w,randw)
		if random.random()<0.5:
			im[randh,randw,:] = np.array([0,0,0])
		else:
			im[randh,randw,:] = np.array([255,255,255])
	cv2.imshow('add noise',im)
	cv2.waitKey(0)

#addNoise('test.png')