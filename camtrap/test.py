import run_tf_detector as detect
import cv2



def enchance_img(frame):
    temp_img = frame 
    wb = cv2.xphoto.createGrayworldWB()
    wb.setSaturationThreshold(0.99)
    img_wb = wb.balanceWhite(temp_img)
    img_lab = cv2.cvtColor(img_wb,cv2.COLOR_BGR2LAB)
    l,a,b = cv2.split(img_lab)
    # print(type(l))
    # g_l = cv2.cvtColor(l,cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=6,tileGridSize=(8,8))
    img_l = clahe.apply(l)
    img_clahe = cv2.merge((img_l,a,b))
    return cv2.cvtColor(img_clahe,cv2.COLOR_Lab2BGR)




im = cv2.imread('test_images\\test_images\wcs_camera_traps_animals_0090_1439.jpg')
res,flag = detect.load_and_run_detector((im))
if flag==1:
    print("Animal Detected")
cv2.imwrite('result_img\\result1.png',res)