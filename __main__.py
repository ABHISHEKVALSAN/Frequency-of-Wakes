import cv2
import numpy as np

def getFreq(data):
	frate	 	= 60.0
	w 			= np.fft.fft(data)
	freqs 		= np.fft.fftfreq(len(w))
	idx 		= np.argmax(np.abs(w))
	freq 		= freqs[idx]
	freq_in_hertz 	= abs(freq * frate)

	return freq_in_hertz


def main():
	img = cv2.imread("wakes_window/wframe1.jpg",0)
	d	= []
	s	= 0.0
	i	= 0
	while True:
		try:
			img = cv2.imread("wakes_window/wframe"+str(i+1)+".jpg",0)
			d.append(img.sum())
			s+=img.sum()
			i+=1
		except:
			break
	avg=s/len(d)

	i=0
	while i<len(d):
		d[i]-=avg
		i+=1
	data 	=	np.array(d)
	freq	=	getFreq(data)
	err		= 	freq*60.0/len(d)
	print(str(freq)+" +/- "+str(err))

if __name__=="__main__":
	main()
