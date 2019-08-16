import numpy as np; import matplotlib.pyplot as plt; import cv2
def overlay(img):
# cv2.putText arg: image, text, bottomleftcorner-(x,y), font, fontscale, fontcolor (BGR), linewidth
    cv2.putText(img,"PRESS 'SPACE' TO TAKE PICTURE !", (190,350),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    cv2.putText(img,"PLACE EYES IN RED BOX.", (220,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    cv2.putText(img,"PLACE NOSE IN GREEN BOX.", (220,120),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.rectangle arg: image, topleft-(x,y), bottomright-(x,y), color, linewidth
    cv2.rectangle(img,(238,158),(402,322),0,3)                                 #Frame
# cv2.line arg: image, Top-(x,y), bottom-(x,y), color, linewidth
    cv2.line(img, (320,160), (320,320),(255,0,0),1)                            #x-middle
    cv2.line(img, (240,240), (400,240),(255,0,0),1)                            #y-middle
    cv2.rectangle(img,(305,170),(335,240),(0,255,0),1)                         #Nose
    cv2.rectangle(img,(260,175),(380,205),(0,0,255),1)                         #Eyes        

def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read() 
        upload_ret_val, upload_img = cam.read() 
        img = cv2.flip(img, 1)
        upload_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #cv2.COLOR_RGB2GRAY
        overlay(img)
        img = cv2.resize(img, (933,700))#(1024,768))        
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 32: 
            overlay(img)
            img_name = "C:/Users/Frederik/Desktop/database/Database_pic_{}.png".format(img_counter)
            upload_img = upload_img[158:322,238:402]#238,158),(402,322
            cv2.imwrite(img_name ,upload_img)
            print('Picture taken. -Checking system.')
            break
    cv2.destroyAllWindows() 
    cam.release()
    return upload_img[158:322,238:402]
img = show_webcam()
def Eigenfaces(img):
    
    training_set = []    
    for N in range(0,60,10):
        img_name = "C:/Users/Frederik/Desktop/database/Database_pic_{}.png".format(N)
        img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_GRAYSCALE, farvebilleder til grayscale
        img = np.concatenate(img)
        training_set.append(img)
    
    training_set = np.array(training_set).T
    
    images = len(training_set[1])
    Number_of_pixels = len(training_set)
    ml = np.zeros((67600,6))
    
    
    print('Creating column mean', end=' ... ')
    for pixels in range(67600):
        mean_col = sum(training_set[pixels])/images
        ml[pixels,:] = np.add(ml[pixels],mean_col)
    print('DONE')
    
    
    print('Creating row mean', end=' ... ')
    for image in range(6):
        mean_row = sum(training_set[:,image])/Number_of_pixels
        ml[:,image] = np.add(ml[:,image],mean_row)
    print('DONE')
    
    avg_face = training_set-ml
    print('Creating Covariance Matrix', end=' ... ')
    Cov_matrix = np.cov(avg_face.T) #avg_face.T @ avg_face
    print('DONE'); print('Creating Eigenface', end=' ... ')
    eig_val, eig_vec = np.linalg.eig(Cov_matrix)
    print('DONE')
    
    
