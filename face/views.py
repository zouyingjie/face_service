
from orange.views import QingChengApiGetMixin

from face.service import FaceIdService

class FaceValidApiView(QingChengApiGetMixin):

    get_model_service = FaceIdService

    def get_action_format(self, params, request, *args, **kwargs):
        # old_images = params.pop("old_images", None)
        # new_image = params.pop("new_image", None)

        old_image = "/home/chiyuan/projects/face_service/face/openailab_faceapi/data/3_1.jpg"
        new_image = [
            "/home/chiyuan/projects/face_service/face/openailab_faceapi/data/3_2.jpg",
            "/home/chiyuan/projects/face_service/face/openailab_faceapi/data/3_3.jpg",
            "/home/chiyuan/projects/face_service/face/openailab_faceapi/data/3_4.jpg",
            "/home/chiyuan/projects/face_service/face/openailab_faceapi/data/3_5.jpg",
        ]

        face_valid, error_code = self.get_model_service().face_valid(new_image=new_image, old_images=old_images)
        json_data = {"valid": face_valid, "code": error_code}
        return json_data
