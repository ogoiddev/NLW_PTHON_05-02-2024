import json

from cerberus import Validator

body = {"data": {"size": "tags", "details": {"name": "Python", "price": 100}, "qt": 1}}

body_validator = Validator(
    {
        "data": {
            "type": "dict",
            "schema": {
                "size": {"type": "string", "allowed": ["tags"]},
                "details": {
                    "type": "dict",
                    "schema": {
                        "name": {"type": "string", "minlength": 3, "maxlength": 50},
                        "price": {
                            "type": "float",
                            "min": 0,
                            "max": 1000000,
                            "empty": False,
                            "required": True,
                        },
                    },
                },
                "qt": {"type": "integer", "min": 1, "max": 1000},
            },
        }
    }
)

response = body_validator.validate(body)

if response is False:
    # Formatando e imprimindo os erros de validação de uma maneira mais legível
    print(json.dumps(body_validator.errors, indent=4))
else:
    print("Validated -> OK body")
