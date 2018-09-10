import cv2
import numpy as np

#------------------------------------------#
#---- Returns requency of a wave array ----#
#------------------------------------------#
def getFreq(data):

	frate	 	= 60.0
	w 		= np.fft.fft(data)
    	freqs 		= np.fft.fftfreq(len(w))
    	idx 		= np.argmax(np.abs(w))
    	freq 		= freqs[idx]
    	freq_in_hertz 	= abs(freq * frate)

	return freq_in_hertz

#-----------------------------------------#
#-------- Convert Images to wave array ---#
#-----------------------------------------#
def waveConv():
	img 	= cv2.imread("wakes_window/wframe1.jpg",0)
	d	= []
	s	= 0.0
	i	= 0
	while True:
		try:
			print i
			img = cv2.imread("wakes_window/wframe"+str(i+1)+".jpg",0)
			d.append(img.sum())
			s+=img.sum()
			i+=1
		except:
			break
		# Each element in d represents an image
		# Image is represented by the sum of its pixel values
		
	
	# Shift the wave to x axis by subtracting each element by the average of array
	avg=s/len(d)
	
	i=0
	while i<len(d):
		d[i]-=avg
		i+=1
	# data is an array where index represent time in x axis and values represent amplitude in y axis
	data 	=	np.array(d)
	freq	=	getFreq(data)
	err	= 	freq*60.0/len(d)	
	print	str(freq)+" +/- "+str(err)
	
def main():
	waveConv()

if __name__=="__main__":
	main()
