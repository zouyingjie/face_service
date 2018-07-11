
from orange.views import QingChengApiGetMixin
from face.service import FaceIdService
from settings.settings import PROJECT_HOME

class FaceValidApiView(QingChengApiGetMixin):

    def get_action_format(self, params, request, *args, **kwargs):
        image = "{project_home}/data/image/{image}".format(PROJECT_HOME, "3_1.jpg")
        rect = FaceIdService().face_image_rectangle(image=image)
        return {"width": rect.width}
