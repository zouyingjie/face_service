
from orange.views import QingChengApiGetMixin
from face.service import FaceIdService
from settings.settings import PROJECT_HOME

class FaceValidApiView(QingChengApiGetMixin):

    def get_request_params(self, request, *args, **kwargs):
        params = self.get_params(request, *args, **kwargs)
        # params["photo"] = "{project_home}/data/image/3_1.jpg".format(project_home=PROJECT_HOME)
        # photo = params.pop('photo', None)
        # old_photos = params.pop('old_photos', None)
        # service = FaceIdService()
        # photo_path = service.down_photos(photo_url=photo)
        # params['photo'] = photo_path
        # if old_photos is not None:
        #     old_photo_paths = []
        #     for photo in old_photos:
        #         path = service.down_photos(photo_url=photo)
        #         old_photo_paths.append(path)
        #     params['old_photos'] = old_photo_paths
        return params

    def get_action_format(self, params, request, *args, **kwargs):
        # result = self.get_model_service().face_valid(**params)
        # return result
        service = FaceIdService()
        image = "/home/chiyuan/openailab_faceapi/data/3_1.jpg"
        rect = service.face_image_rectangle(image=image)
        print(rect.width)
        print(service.face_quality_ok(image=image))
        print(service.face_existed(image=image))
        valid, code = service.face_valid(photo=image)
        return {"valid": valid, "code": code}
