
from orange.views import QingChengApiGetMixin

from face.service import FaceIdService
from settings.settings import PROJECT_HOME

class FaceValidApiView(QingChengApiGetMixin):

    get_model_service = FaceIdService

    def get_action_format(self, params, request, *args, **kwargs):

        image = "{project_home}/data/image/{image}".format(PROJECT_HOME, "3_1.jpg")
        rect = self.get_model_service().face_image_rectangle(image=image)
        return {"width": rect.width}
