import numpy as np
import cv2

img = cv2.imread('cluster_test_input5.jpg')
img = cv2.imread('Example_results_Easygel_test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
# cv2.THRESH_BINARY,25,1)

ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

connect = 4
n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity=connect)

print(n_labels)
print(stats)
size_thresh_min = 5
size_thresh_max = 5000
print(stats[:,4])
print(stats[:,4][np.where((stats[:,4]>size_thresh_min) & (stats[:,4]<size_thresh_max))])
print(stats[:,4][np.where((stats[:,4]>size_thresh_min) & (stats[:,4]<size_thresh_max))].size)
# print(np.where(stats[:,4]>size_thresh).size)


for i in range(1, n_labels):
    if size_thresh_min <= stats[i, cv2.CC_STAT_AREA] < size_thresh_max:
        #print(stats[i, cv2.CC_STAT_AREA])
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=1)

# cv2.imwrite(f"cluster_test_out5_{connect}.jpg", img)
cv2.imwrite(f"Example_results_Easygel_test_{connect}.jpg", img)