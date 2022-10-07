import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np

reader = easyocr.Reader(['ko','en'])

img_path = 'D:/python/project/OCR/target_image.jpg'

img = cv2.imread(img_path)
###-----------##show image
# plt.figure(figsize=(10,6))
# plt.imshow(img[:,:,::-1])
# plt.axis('off')
# plt.show()

###read OCR
result = reader.readtext(img_path)
###Test all output

# for i in range(len(result)):
#     print(str(i+1)+"번째 글씨---------------------------------------------------------------------")
#     print(result[i][0]) ##position
#     print(result[i][1]) ###letter
#     print(result[i][2]) ##confidence


###후처리 - 1 for box
THRESHOLD = 0.4 #confidence 기준. ----------------인식이 정답과 많이 달라도 confidence 낮아짐.
Real_letter = []
for box, letter, conf in result:
    if conf < THRESHOLD:
        continue
    else:
        cv2.rectangle(img, pt1=box[0], pt2 = box[2], color = (0,0,255), thickness=3)##color BGR
        print(letter)
        Real_letter.append(letter)

##결과 box 보여주기.
plt.figure(figsize=(10,6))
plt.imshow(img[:,:,::-1])
plt.axis('off')
plt.show()
Real_letter


###후처리 -2 box + letter 동시에.
# THRESHOLD = 0.4 #confidence 기준. ----------------인식이 정답과 많이 달라도 confidence 낮아짐.
# Real_letter = []
# for box, letter, conf in result:
#     if conf < THRESHOLD:
#         continue
#     else:
#         cv2.rectangle(img, pt1=box[0], pt2 = box[2], color = (0,0,255), thickness=3)##color BGR
#         img = cv2.putText(img, letter, box[0][0], int(np.float32(box[0][1] - 10)), (0, 255, 0), 2)
