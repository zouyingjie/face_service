
from orange.views import QingChengApiGetMixin

from face.openailab_faceapi.python.service import FaceIdService


class FaceValidApiView(QingChengApiGetMixin):

    get_model_service = FaceIdService

    def get_action_format(self, params, request, *args, **kwargs):
        old_images = params.pop("old_images", None)
        new_image = params.pop("new_image", None)
        face_valid = self.get_model_service().face_valid(new_image=new_image, old_images=old_images)
        json_data = {"valid": face_valid}
        return json_data
