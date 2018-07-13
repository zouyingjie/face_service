# -*- coding: utf-8 -*-

# from __future__ import division, unicode_literals, print_function
from settings.settings import PROJECT_HOME

from libs.openailab_faceapi.python import openailabfaceapi

class FaceIdService(object):

    VALID_SUCCESS = 0
    VALID_ERROR_NO_ONE = 1
    VALID_ERROR_QUANTITY = 2
    VALID_ERROR_SAME_PERSON = 3

    FACE_OK = 0
    FACE_ERROR_NOT_CLEAR = 1  # 图像不清晰
    FACE_ERROR_ANGLE = 2  # 角度不合理
    FACE_ERROR_OVER_LEFT = 3  # 超过最大左转角度
    FACE_ERROR_OVER_RIGHT = 4  # 超过最大右转角度
    FACE_ERROR_OVER_UP = 5  # 超过最大上仰角度
    FACE_ERROR_OVER_DOWN = 6  # 超过最大俯视角度
    FACE_ERROR_HORIZONTAL_ROTATION = 7  # 超过最大水平旋转角度
    FACE_ERROR_FACE_NO_EXIST = 8  # 没有检测到人脸
    FACE_ERROR_NOT_SAME = 9  # 不是同一个人

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
        result = openailabfaceapi.FaceQualityOK(photo, rectangle, threshold)
        return result

    # 判断多张照片是否为同一个人
    def is_same_person(self, phtots=None, threshold=0.5):
        result = openailabfaceapi.FaceIsSamePerson(phtots, threshold)
        if result == 0:
            return False
        return True

    def face_valid(self, photo=None, old_photos=None):
        if not self.face_existed(photo=photo):
            return False, self.FACE_ERROR_FACE_NO_EXIST

        face_quality = self.face_quality_ok(photo=photo)
        if face_quality == self.FACE_OK:
            if old_photos is not None:
                old_photos.append(photo)
                if not self.is_same_person(phtots=old_photos):
                    return False, self.VALID_ERROR_SAME_PERSON
            return True, self.FACE_OK
        else:
            return False, face_quality

    @classmethod
    def download_photos(cls, photo_url=None):
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
