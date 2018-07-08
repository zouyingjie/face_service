# -*- coding: utf-8 -*-


from __future__ import division, unicode_literals, print_function

import openailabfaceapi

from settings.settings import PROJECT_HOME


class FaceIdService(object):
    def __init__(self):
        path = PROJECT_HOME + "/data/logs/face_logs/"
        openailabfaceapi.initial(path)

    # 获取图片的人脸矩阵
    def face_image_rectangle(self, image):
        """
        获取图片的人脸矩阵
        :param image:
        :return:
        """
        return openailabfaceapi.FaceExisted(image)

    # 判断图片中是否有人脸
    def face_existed(self, image, rectangle=None):
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

    def is_same_person(self, images, threshold=0.5):
        ret = openailabfaceapi.FaceIsSamePerson(images, threshold)
        if ret == 0:
            return False
        return True
