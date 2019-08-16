import numpy as np; import matplotlib.pyplot as plt; import cv2
training_set = []

for N in range(0,60,10):
    img_name = "C:/Users/magge/OneDrive/Dokumenter/GitHub/P2/database/Database_pic_{}.png".format(N)
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


# =============================================================================
#  Tester de average faces
# =============================================================================
#avg_face += 180   # Man skal + 180 for at se avg face, but why? 

fig=plt.figure(figsize=(8, 8))
columns = 3; rows = 2
names = ['Magnus','Caroline','Frederik','Mia','Mads','Kevin']

for i in range(1, 7):
    test = np.reshape(avg_face @ eig_vec[i-1],(260,260)) #np.reshape(avg_face[:,i-1],(260,260))
    fig.add_subplot(rows, columns, i)
    plt.imshow(test, cmap = 'gray')
    plt.title('Eigenface {}'.format(i))
#    plt.title(names[i-1])
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
print('Deleting unnecesary variables')
del(names, N,Number_of_pixels,columns,i,image,images,img,img_name,mean_col,mean_row, ml, pixels, rows)