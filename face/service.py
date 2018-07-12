# -*- coding: utf-8 -*-

# from __future__ import division, unicode_literals, print_function
from settings.settings import PROJECT_HOME

from libs.openailab_faceapi.python import openailabfaceapi

class FaceIdService(object):

    VALID_SUCCESS = 0
    VALID_ERROR_NO_ONE = 1
    VALID_ERROR_QUANTITY = 2
    VALID_ERROR_SAME_PERSON = 3

    def __init__(self):
        log_path = "{project_home}/data/logs/".format(project_home=PROJECT_HOME)
        model_path = "{project_home}/libs/openailab_faceapi/models".format(project_home=PROJECT_HOME)
        print(log_path)
        print(model_path)
        openailabfaceapi.initial(log_path, model_path)

    # 获取图片的人脸矩阵
    def face_image_rectangle(self, image):
        """
        获取图片的人脸矩阵
        :param image:
        :return:
        """
        return openailabfaceapi.FaceExisted(image)

    # 判断图片中是否有人脸
    def face_existed(self, image=None, rectangle=None):
        """
        判断图片是否有人脸
        :param image:
        :param rectangle:
        :return:
        """
        if rectangle is None:
            rectangle = self.face_image_rectangle(image)
        if rectangle.width == 0:
            return False
        return True

    # 判断图片中的人脸是否合格，
    def face_quality_ok(self, image, rectangle=None, threshold=0.8):
        """

        :param image: 图片
        :param rectangle: 图片的人脸矩阵
        :param threshold: 合格标准，默认是 0.8
        :return:
        """
        if rectangle is None:
            rectangle = self.face_image_rectangle(image)

        if not self.face_existed(image, rectangle):
            return False
        return openailabfaceapi.FaceQualityOK(image, rectangle, threshold)

    # 判断多张照片是否为同一个人
    def is_same_person(self, images, threshold=0.5):
        ret = openailabfaceapi.FaceIsSamePerson(images, threshold)
        if ret == 0:
            return False
        return True

    def face_valid(self, photo=None, old_photos=None):

        rect = self.face_image_rectangle(image=photo)
        print(rect.width + "===")
        if not self.face_existed(rectangle=rect):
            return False, self.VALID_ERROR_NO_ONE
        print(111)
        if not self.face_quality_ok(rectangle=rect):
            return False, self.VALID_ERROR_QUANTITY
        print(222)
        if old_photos is not None:
            old_photos.append(photo)
            if not self.is_same_person(old_photos):
                return False, self.VALID_ERROR_SAME_PERSON
        print(333)
        return True, self.VALID_SUCCESS

    def down_photos(self, photo_url=None):
        from settings.settings import PROJECT_HOME
        import requests
        r = requests.get(photo_url, stream=True)
        image_url = "{project_home}/data/image/{image}.jpg".format(project_home=PROJECT_HOME,
                                                             image=photo_url)
        with open(image_url, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
        return image_url
