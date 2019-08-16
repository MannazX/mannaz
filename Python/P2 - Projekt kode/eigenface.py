#import numpy as np
#import matplotlib.pyplot as plt
#import math as m
import cv2
def overlay(img):
#               Squ5are
#        cv2.rectangle(img,(192,112),(448,368),0,3) #Topleft, bottomright, color RGB, linewidth
        cv2.rectangle(img,(240,160),(400,320),0,3) #Topleft, bottomright, color RGB, linewidth
        cv2.line(img,(320,0),(320,600),(0,0,255),1) #leftvertical -r
#               Left eye
        cv2.line(img,(268,198),(268,183),(0,0,255),1) #leftvertical -r
        cv2.line(img,(303,198),(303,183),(0,0,255),1) #rightvertical -r
        cv2.line(img,(268,198),(303,198),(0,0,255),1) #lower -r
        cv2.line(img,(268,183),(303,183),(0,0,255),1) #upper -r
#               Right eye
        
#               Left eye
#        cv2.line(img,(220,150),(220,190),(0,0,255),1) #leftvertical -r
#        cv2.line(img,(220,150),(290,150),(0,0,255),1) #upper -r
#        cv2.line(img,(290,150),(290,190),(0,0,255),1) #rightvertical -r
#        cv2.line(img,(220,190),(290,190),(0,0,255),1) #lower -r
#        cv2.line(img,(243,160),(243,180),255,1) # leftvertical -b
#        cv2.line(img,(271,160),(271,180),255,1) # rightvertical -b
#        cv2.line(img,(0,160),(640,160),255,1)
#        cv2.line(img,(0,180),(640,180),255,1)
##               Right eye
#        cv2.line(img,(355,150),(355,190),(0,0,255),1) #leftvertical -r
#        cv2.line(img,(355,150),(425,150),(0,0,255),1) #upper -r
#        cv2.line(img,(425,150),(425,190),(0,0,255),1) #rightvertical -r
#        cv2.line(img,(355,190),(425,190),(0,0,255),1) #lower -r
#
#        cv2.line(img,(374,160),(374,180),255,1)
#        cv2.line(img,(402,160),(402,180),255,1)
##               Nose
#        cv2.line(img,(305,150),(305,220),(0,255,0),1)
#        cv2.line(img,(340,150),(340,220),(0,255,0),1)
        
def show_image(images): 
    for i in range(images):
        img_title = 'Database_pic_{}'.format(i)
#        img_name = "C:/Users/Frederik/Desktop/checkpic_{}.png".format(i)
        img = cv2.imread(img_name) # cv2.IMREAD_GRAYSCALE, farvebilleder til grayscale
        cv2.imshow(img_title ,img)
#        plt.imshow() # man kan bare benytte cv2.imshow

def show_webcam():
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret_val, img = cam.read() 
        upload_ret_val, upload_img = cam.read() 
        img = cv2.flip(img, 1)

        upload_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #cv2.COLOR_RGB2GRAY

        overlay(img)
        img = cv2.resize(img, (1024,768))
        
        cv2.imshow('my webcam', img)

#        if cv2.waitKey(1) == 32: 
#            overlay(img)
##            img_name = "C:/Users/Frederik/Desktop/database/Database_pic_{}.png".format(img_counter)
#            upload_img = upload_img[110:370,190:450]
#            cv2.imwrite(img_name ,upload_img)
#            print("Database_pic_{} written!".format(img_counter))
#            img_counter += 1
            
        if cv2.waitKey(1) == 27: # esc to quit 
            break

    cv2.destroyAllWindows() 
    cam.release()
#    show_image(img_counter)
    return img
img = show_webcam()


"""
To create a set of eigenfaces, one must:
1.Prepare a training set of face images. The pictures constituting the training 
set should have been taken under the same lighting conditions, and must be normalized 
to have the eyes and mouths aligned across all images. They must also be all resampled
to a common pixel resolution (r × c). Each image is treated as one vector, simply by 
concatenating the rows of pixels in the original image, resulting in a single column 
with r × c elements. For this implementation, it is assumed that all images of the 
training set are stored in a single matrix T, where each column of the matrix is an image.


2.Subtract the mean. The average image a has to be calculated and then subtracted from each 
original image in T.

3.Calculate the eigenvectors and eigenvalues of the covariance matrix S. Each eigenvector 
has the same dimensionality (number of components) as the original images, and thus can 
itself be seen as an image. The eigenvectors of this covariance matrix are therefore called 
eigenfaces. They are the directions in which the images differ from the mean image. Usually 
this will be a computationally expensive step (if at all possible), but the practical 
applicability of eigenfaces stems from the possibility to compute the eigenvectors of 
S efficiently, without ever computing S explicitly, as detailed below.

4.Choose the principal components. Sort the eigenvalues in descending order and arrange 
eigenvectors accordingly. The number of principal components k is determined arbitrarily 
by setting a threshold ε on the total variance. 
Total variance {\displaystyle v=(\lambda _{1}+\lambda _{2}+...+\lambda _{n})} {\displaystyle v=(\lambda _{1}+\lambda _{2}+...+\lambda _{n})}, n = number of components.

5.k is the smallest number satisfies : {\displaystyle {\frac {(\lambda _{1}+\lambda _{2}+...+\lambda _{k})}{v}}>\epsilon } {\displaystyle {\frac {(\lambda _{1}+\lambda _{2}+...+\lambda _{k})}{v}}>\epsilon }

Kilde:
https://en.wikipedia.org/wiki/Eigenface#Use_in_facial_recognition
Under practical implementation
"""