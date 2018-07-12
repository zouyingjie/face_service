
from orange.views import QingChengApiGetMixin
from face.service import FaceIdService

class FaceValidApiView(QingChengApiGetMixin):

    def get_request_params(self, request, *args, **kwargs):
        params = self.get_params(request, *args, **kwargs)
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
        service = FaceIdService()
        valid, code = service.face_valid(photo=photo)
        return {"valid": valid, "code": code}
