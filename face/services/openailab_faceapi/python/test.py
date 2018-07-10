import openailabfaceapi

PROJECT_HOME = "/home/chiyuan/projects/face_service"

def face_existed(image):
    return openailabfaceapi.FaceExisted(image)

jpegFileName="{project_home}/libs/openailab_faceapi/data/3_1.jpg".format(project_home=PROJECT_HOME)
# rect = openailabfaceapi.FaceExisted(jpegFileName)
# print("left:", rect.left)
# print("top:", rect.top)
# print("width:", rect.width)
# print("height:", rect.height)

rect = face_existed(jpegFileName)
print("left:", rect.left)
print("top:", rect.top)
print("width:", rect.width)
print("height:", rect.height)