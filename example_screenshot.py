#import pyscreenshot
#import pyscreenshot #as Imagegrab
import webbrowser
import cv2
import pytesseract
import os
import argparse
from PIL import Image
from halo import Halo
#os.chdir('/Escritorio')

#im=pyscreenshot.grab(bbox=(134,487,567,642))
#im.save('test.jpg')
def read_screen():
	spinner = Halo(text='Reading screen', spinner='bouncingBar')
	spinner.start()
	screenshot_file="q12ejemplo.png"
	

	#prepare argparse
	ap = argparse.ArgumentParser(description='HQ_Bot')
	ap.add_argument("-i", "--image", required=False,default=screenshot_file,help="path to input image to be OCR'd")
	ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
	args = vars(ap.parse_args())

	# load the image 
	image = cv2.imread(args["image"])
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	# store grayscale image as a temp file to apply OCR
	filename = "Screens/{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
	text = pytesseract.image_to_string(Image.open(filename),lang='spa')
	os.remove(filename)
	os.remove(screenshot_file)
	
	# show the output images

	'''cv2.imshow("Image", image)
	cv2.imshow("Output", gray)
	os.remove(screenshot_file)
	if cv2.waitKey(0):
		cv2.destroyAllWindows()
	print(text)
	'''
	spinner.succeed()
	spinner.stop()

	return text
s = read_screen()
webbrowser.open('http://google.com/search?q='+ s, new=2)
