# import openailabfaceapi
#
# # initialization
# openailabfaceapi.initial("../log/", "../models")
#
# # check if there's a face in picture
# jpegFileName="../data/3_1.jpg"
# rect = openailabfaceapi.FaceExisted(jpegFileName)
# print("left:", rect.left)
# print("top:", rect.top)
# print("width:", rect.width)
# print("height:", rect.height)
# if rect.width == 0 :
#     print("face is not existed")
# else :
#     print("face is existed")
#
# # check if the quality is ok
# threshold = 0.8
# ret = openailabfaceapi.FaceQualityOK(jpegFileName, rect, threshold)
# if ret == 0 :
#     print("picture qualify is good")
# else :
#     print("picture is not good", ret)
#
# # check if the same person in lots of pictures
# jpegFileNameList=["../data/3_1.jpg", "../data/3_2.jpg", "../data/3_3.jpg", "../data/3_4.jpg", "../data/3_5.jpg"]
# threshold = 0.50
# ret = openailabfaceapi.FaceIsSamePerson(jpegFileNameList, threshold)
# if ret == 0 :
#     print("pictures are not a person")
# else :
#     print("pictures are a person")
#
# # Select the best picture
# threshold = 0.8
# index = openailabfaceapi.BestFacePicture(jpegFileNameList, threshold)
# print(jpegFileNameList[index] + " is the best picture")
#
# # deinitialization
# openailabfaceapi.deinitial()
