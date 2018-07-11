# -*- coding: utf-8 -*-

# from __future__ import division, unicode_literals, print_function
from libs.openailab_faceapi.python import openailabfaceapi
from settings.settings import PROJECT_HOME

class FaceIdService(object):

    VALID_SUCCESS = 0
    VALID_ERROR_NO_ONE = 1
    VALID_ERROR_QUANTITY = 2
    VALID_ERROR_SAME_PERSON = 3

    def __init__(self):
        log_path = "{project_home}/data/logs/".format(project_home=PROJECT_HOME)
        model_path = "{project_home}/libs/openailab_faceapi/models".format(project_home=PROJECT_HOME)

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

    def face_valid(self, image=None, old_images=None):

        rect = self.face_image_rectangle(image=image)
        if not self.face_existed(rectangle=rect):
            return False, self.VALID_ERROR_NO_ONE

        if not self.face_quality_ok(rectangle=rect):
            return False, self.VALID_ERROR_QUANTITY

        if old_images is not None:
            old_images.append(image)
            if not self.is_same_person(old_images):
                return False, self.VALID_ERROR_SAME_PERSON

        return True, self.VALID_SUCCESS