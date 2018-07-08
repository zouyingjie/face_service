from libs.openailab_faceapi.python import openailabfaceapi
from settings.settings import PROJECT_HOME

# initialization
# openailabfaceapi.initial("../log/")
from python.test import face_existed

# check if there's a face in picture
jpegFileName="{project_home}/libs/openailab_faceapi/data/3_1.jpg".format(project_home=PROJECT_HOME)
rect = face_existed(jpegFileName)
print("left:", rect.left)
print("top:", rect.top)
print("width:", rect.width)
print("height:", rect.height)
