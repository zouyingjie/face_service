from libs.openailab_faceapi.python import openailabfaceapi
from settings.settings import PROJECT_HOME

# initialization
# openailabfaceapi.initial("../log/")

# check if there's a face in picture
jpegFileName="{project_home}/libs/openailab_faceapi/data/3_1.jpg".format(project_home=PROJECT_HOME)
rect = openailabfaceapi.FaceExisted(jpegFileName)
print("left:", rect.left)
print("top:", rect.top)
print("width:", rect.width)
print("height:", rect.height)
