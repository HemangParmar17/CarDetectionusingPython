import cv2

#Image or Video
Video = cv2.VideoCapture("video.mp4")

#Pre-trained classifire
classifire_file = "cars.xml"

#Create Car Classifier
car_tracker = cv2.CascadeClassifier(classifire_file)

#Run forever
while True:
    #Read the current Frame
    (read_successful, frame) = Video.read()

    #Safe coding
    if read_successful:
        #Must convert to grayscale
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        resizeframe = cv2.resize(grayscale_frame,(540,380) )
        frameresize = cv2.resize(frame,(450,300))
    else:
        break

    #Detect Cars
    Cars = car_tracker.detectMultiScale(frameresize)

    #Draw rectangle around the Cars
    for(x, y, w, h) in Cars:
         cv2.rectangle(frameresize, (x, y), (x+w,y+h),(0,255,0), 2)

    #Display the Image
    cv2.imshow("Car Detection", frameresize)

    #Don't autoclose(Delay)
    key = cv2.waitKey(1)


    #Quit if key q or Q is pressed
    if key == 81 or key == 113:
        break


#Detect cars in an image

# img = cv2.imread("CarImage1.jpg")
#
# Convert image to grayscale
# grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#
# Create Car Classifier
# car_tracker = cv2.CascadeClassifier(classifire_file)
#
# Detect Cars
# Cars = car_tracker.detectMultiScale(grayscale)
#
# Draw rectangle around the Cars
#
# for(x, y, w, h) in Cars:
#     cv2.rectangle(img, (x, y), (x+w,y+h),(0,255,0), 2)

#Display the Image
# cv2.imshow("Car Detection", img)

#Don't autoclose(Delay)
#cv2.waitKey()

print("Code Completed")