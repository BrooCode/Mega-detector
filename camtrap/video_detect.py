import cv2
import run_tf_detector as detect



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

vidObj = cv2.VideoCapture("pets-on-cctv.mp4")
count=0
img_array = []
while count!=1000:

  success, image = vidObj.read()
  if success:
#   im = detect.load_and_run_detector(enchance_img(image))
    im,flag = detect.load_and_run_detector(image)
    img = im
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
  # print(count)
  else:
        break
  count += 1
    
out = cv2.VideoWriter('pets-on-cctvresult.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
# video = cv2.VideoWriter(video_name, 0, 1, (width, height)) 

for i in range(len(img_array)):
  out.write(img_array[i])
out.release() 