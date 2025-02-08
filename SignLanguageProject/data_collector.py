## This Data_Collector.py file is used mainly for the collection of the real time data
import os
import time
import cv2 ## OpenCV library
import uuid ## UUID - Use for the Unique ID name for the each file names(It provide unique name and id)

IMAGE_PATH = "CollectedImages"

labels = [ 'Hello' , 'Yes' , 'No' , 'Thanks' , 'ILoveYou' , 'Please' ]

number_of_images = 5 

## this for loop used for creating each new image with their pre defined folder and then create the 
## .jpg file
for label in labels :
    img_path = os.path.join(IMAGE_PATH,label) ##This is used for the joining the image path with label
    os.makedirs(img_path) ## create the new directories

    ## Open the Camera module
    cap = cv2.VideoCapture(0) ## Capturing the images
    print(f"Collecting Images for {label}")
    time.sleep(3) ## Camera is sleep after every 5 sec

    ## This for loop used mainly for the creating the imagename with .jpg format
    for imgnum in range(number_of_images) : 
        ret, frame = cap.read()
        imagename = os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame) ## Used for the saving the image
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1)  & 0xFF==ord('q'):
            break

    cap.release()
