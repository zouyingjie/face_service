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
    def photo_rectangle(self, photo=None):
        """
        获取图片的人脸矩阵
        :param image:
        :return:
        """
        return openailabfaceapi.FaceExisted(photo)

    # 判断图片中是否有人脸
    def face_existed(self, photo=None, rectangle=None):
        """
        判断图片是否有人脸
        :param image:
        :param rectangle:
        :return:
        """
        if rectangle is None:
            rectangle = self.photo_rectangle(photo)
        if rectangle.width == 0:
            return False
        return True

    # 判断图片中的人脸是否合格，
    def face_quality_ok(self, photo=None, rectangle=None, threshold=0.1):
        """

        :param image: 图片
        :param rectangle: 图片的人脸矩阵
        :param threshold: 合格标准，默认是 0.8
        :return:
        """
        if rectangle is None:
            rectangle = self.photo_rectangle(photo)

        if not self.face_existed(photo, rectangle):
            return False
        return openailabfaceapi.FaceQualityOK(photo, rectangle, threshold)

    # 判断多张照片是否为同一个人
    def is_same_person(self, phtots=None, threshold=0.5):
        ret = openailabfaceapi.FaceIsSamePerson(phtots, threshold)
        if ret == 0:
            return False
        return True

    def face_valid(self, photo=None, old_photos=None):
        if not self.face_existed(photo=photo):
            return False, self.VALID_ERROR_NO_ONE

        if not self.face_quality_ok(photo=photo):
            return False, self.VALID_ERROR_QUANTITY

        if old_photos is not None:
            old_photos.append(photo)
            if not self.is_same_person(phtots=old_photos):
                return False, self.VALID_ERROR_SAME_PERSON

        return True, self.VALID_SUCCESS

    @classmethod
    def down_photos(cls, photo_url=None):
        from settings.settings import PROJECT_HOME
        import requests
        from libs.datetimes import datetime_now, datetime_to_str
        r = requests.get(photo_url, stream=True)
        image_name = datetime_to_str(datetime_now())
        image_url = "{project_home}/data/image/{image}.jpg".format(project_home=PROJECT_HOME,
                                                             image=image_name)
        print(image_url)
        with open(image_url, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
        return image_url
