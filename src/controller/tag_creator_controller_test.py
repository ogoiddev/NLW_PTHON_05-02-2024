from unittest.mock import patch

from src.controller.tag_creator_controller import TagCreatorController
from src.drivers.barcode_handler import BarcodeHandler


@patch.object(BarcodeHandler, "create_barcode")
def test_tag_creator_controller(mock_create_barcode):
    mock_value = "img_path"
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    print(result)

    assert isinstance(result, dict)
    assert "data" in result

    assert result["data"]["type"] == "Tag Image"

    assert result["data"]["path"] == f"{mock_value}.png"
