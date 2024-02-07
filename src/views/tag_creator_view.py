from src.controller.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
    responsibility to interacting with HTTP
    """

    def validate_nd_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]

        # logica e regra de negocio
        formatted_response = tag_creator_controller.create(product_code)

        # retorno HTTP
        return HttpResponse(status_code=200, body=formatted_response)
