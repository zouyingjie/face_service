import openailabfaceapi
import os
import sys

ABSPATH=None

if __name__ == '__main__':
    ABSPATH=os.path.abspath(sys.argv[0]) 

print(ABSPATH)

path,f_name=os.path.split(ABSPATH)
print(path)
print(f_name)

# initialization
openailabfaceapi.initial(path+"/../log/", path+"/../models")

# check if there's a face in picture
jpegFileName=path+"/../data/1.jpg"
rect = openailabfaceapi.FaceExisted(jpegFileName)
print("left:", rect.left)
print("top:", rect.top)
print("width:", rect.width)
print("height:", rect.height)
print("faceNum:", rect.faceNum)
if rect.width == 0 :
    print("face is not existed")
else :
    print("face is existed")

# check if the quality is ok
threshold = 0.8
ret = openailabfaceapi.FaceQualityOK(jpegFileName, rect, threshold)
if ret == 0 :
    print("picture qualify is good")
else :
    print("picture is not good", ret)

# check if the same person in lots of pictures
jpegFileNameList=[path+"/../data/3_1.jpg", path+"/../data/3_2.jpg", path+"/../data/3_3.jpg", path+"/../data/3_4.jpg", path+"/../data/3_5.jpg"]
threshold = 0.50
ret = openailabfaceapi.FaceIsSamePerson(jpegFileNameList, threshold)
if ret == 0 :
    print("pictures are not a person")
else :
    print("pictures are a person")

# Select the best picture
threshold = 0.8
index = openailabfaceapi.BestFacePicture(jpegFileNameList, threshold)
print(jpegFileNameList[index] + " is the best picture")

# deinitialization
openailabfaceapi.deinitial()
