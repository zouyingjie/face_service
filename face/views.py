
from orange.views import QingChengApiGetMixin
from face.service import FaceIdService
from settings.settings import PROJECT_HOME

class FaceValidApiView(QingChengApiGetMixin):

    def get_request_params(self, request, *args, **kwargs):
        params = self.get_params(request, *args, **kwargs)
        # params["photo"] = "{project_home}/data/image/3_1.jpg".format(project_home=PROJECT_HOME)
        photo = params.pop('photo', None)
        old_photos = params.pop('old_photos', None)
        photo_path = FaceIdService.down_photos(photo_url=photo)
        params['photo'] = photo_path
        if old_photos is not None:
            old_photo_paths = []
            for photo in old_photos:
                path = FaceIdService.down_photos(photo_url=photo)
                old_photo_paths.append(path)
            params['old_photos'] = old_photo_paths
        return params

    def get_action_format(self, params, request, *args, **kwargs):
        photo = params.pop('photo', None)
        # result = self.get_model_service().face_valid(**params)
        # return result
        service = FaceIdService()
        # photo = "/home/chiyuan/openailab_faceapi/data/3_1.jpg"
        rect = service.photo_rectangle(photo=photo)
        print(rect.width)
        print(service.face_quality_ok(photo=photo))
        print(service.face_existed(photo=photo))
        # return {"width": rect.width}
        valid, code = service.face_valid(photo=photo, old_photos=None)
        # return {"width": rect.width}
        return {"valid": valid, "code": code}
