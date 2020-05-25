from lib.api import JSONApi
import json


def test_api_json_typicode():
    api_handler = JSONApi()
    json_response = api_handler.get_json("https://jsonplaceholder.typicode.com/todos/1")
    expected_response = json.loads(
        """{
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
        }"""
    )

    assert json_response == expected_response
