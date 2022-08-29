import os 
import cv2

path = "Images/"
images = []

for file in os.listdir(path):
    name, ext == os.path.splitText(file)

    if ext in['.png', 'gif', 'jpg', 'jpeg','jfif']:
        file_name = path + "/" + file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
width, height , Channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5 , size)

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")