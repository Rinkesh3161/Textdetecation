"""
Created on 30 August 2020
@author: Rinkesh Vamja
Text detection using tesseract and opencv
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img =cv2.imread('3.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_string(img))

###### Detecting a digit only
# hImg,wIMg,_= img.shape
# #this is getting for only digits on images
# cong = r'--oem 3 --psm 9 outputbase digits'
# boxes = pytesseract.image_to_boxes(img,config=cong)
# for i in boxes.splitlines():
#     #print(i)
#     i = i.split(' ')
#     #print(i)
#     x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
#     cv2.putText(img,i[0],(x,hImg-y+15),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

###### Detecting a single character
hImg,wIMg,_= img.shape
boxes = pytesseract.image_to_boxes(img)
for i in boxes.splitlines():
    #print(i)
    i = i.split(' ')
    #print(i)
    x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(img,i[0],(x,hImg-y+15),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


###### Detection Words
# hImg,wIMg,_= img.shape
# boxes = pytesseract.image_to_data(img)
# #print(boxes)
# for x,i in enumerate(boxes.splitlines()):
#     if x!=0:
#         i = i.split()
#         print(i)
#         if len(i)==12:
#               x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
#               cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),2)
#               cv2.putText(img,i[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

###### Detection Digits
# hImg,wIMg,_= img.shape
# cong = r'--oem 3 --psm 9 outputbase digits'
# boxes = pytesseract.image_to_data(img,config=cong)
# #print(boxes)
# for x,i in enumerate(boxes.splitlines()):
#     if x!=0:
#         i = i.split()
#         print(i)
#         if len(i)==12:
#               x,y,w,h = int(i[6]),int(i[7]),int(i[8]),int(i[9])
#               cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),2)
#               cv2.putText(img,i[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

cv2.imshow("Result",img)
cv2.waitKey(0)