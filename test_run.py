import sys
#redefine for yoursellf (find a workaround)
sys.path.append ('/users/jurse/appdata/local/programs/python/python310/lib/site-packages/cv2') 
import cv2
import numpy as np


cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)                         ###set deafolt camera as source


OpenPhoto = cv2.imread("/Users/jurse/Desktop/New folder/Newfolder/image_000_000.png", cv2.IMREAD_ANYCOLOR)

SetOfPhotos = []  
for i in range(0,120,1):                                   ### so lets make ourself some nice array of photos 
        name = "image_" + '{0}'.format(str(i).zfill(3)) + "_000.png"       ### lets start with 10 degrees and no diagonaly 
        #name =  "/Users/jurse/Desktop/New folder/Newfolder/" + name
        name =  "/Users/jurse/Desktop/New folder/Newfolder/" + name
        OpenPhoto = cv2.imread(name, cv2.IMREAD_ANYCOLOR)
        SetOfPhotos.append(OpenPhoto)

MyAngle_X = 500 / 120
MyAngle_Y = 500 / 100
my_position_x = 0
face_segmengation = 5  #split face into X parts to simulate distance 
my_position_x_last = "NaN"
my_position_y_last = "NaN" 
width_of_face_last = "NaN"
change_to_last = "NaN"
while True:                                                 ### Capture frame-by-frame
    ret, frame = video_capture.read()                       ### read from camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.FONT_HERSHEY_SIMPLEX
    )

                                                            ### Draw a rectangle around the faces lets keep or fot now for control 
    for (x, y, w, h) in faces:
        if change_to_last == "NaN":
            my_position_x_last = x
            my_position_y_last = y 
            width_of_face_last = w
            change_to_last = round(my_position_x / MyAngle_X)
        my_position_x = x
        my_position_y = y 
        width_of_face = w
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Video", frame)                              ### Display the resulting frame
    
    # TODO: replace "0" for "-round(my_position_y / MyAngle_Y)"
    #print("position " +str(-round(my_position_x / MyAngle_X)) + "\n" )
    change_to = round(my_position_x / MyAngle_X)
    if ((width_of_face/abs(my_position_x - my_position_x_last)) >= face_segmengation):
        change_to = change_to_last

    cv2.imshow("Image", SetOfPhotos[change_to])

    my_position_x_last = my_position_x 
    my_position_y_last = my_position_y 
    width_of_face_last = width_of_face 
    change_to_last = round(my_position_x / MyAngle_X)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
                
video_capture.release()                                     ### When everything is done, release the capture
cv2.destroyAllWindows()