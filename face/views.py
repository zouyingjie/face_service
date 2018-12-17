from django.views.generic import View
from face.service import FaceIdService

class FaceValidApiView(View):

    def get(self, request, *args, **kwargs):

        params = request.GET.dict()
        photo = params.pop('photo', None)
        old_photos = params.pop('old_photos', None)
        photo_path = FaceIdService.download_photos(photo_url=photo)
        params['photo'] = photo_path
        if old_photos is not None:
            old_photo_paths = []
            for photo in old_photos:
                path = FaceIdService.download_photos(photo_url=photo)
                old_photo_paths.append(path)
            params['old_photos'] = old_photo_paths

        photo = params.pop('photo', None)
        service = FaceIdService()
        is_valid, code = service.face_valid(photo=photo)
        service.deinitial()
        return {"is_valid": is_valid, "code": code}
