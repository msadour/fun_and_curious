from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from tests.config.factories import CategoryFactory, QuestionFactory
from tests.config.urls import URL_GAME


class GameTestCase(APITestCase):
    """class GameTestCase."""

    def setUp(self) -> None:
        self.client = APIClient()
        categories = CategoryFactory.create_batch(10)
        for category in categories:
            QuestionFactory.create_batch(20, category=category)

    def test_generate_game(self) -> None:
        data = """{
          "label": "Label test 123"
        }"""

        response = self.client.post(
            URL_GAME, data=data, content_type="application/json"
        )
        response_data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["label"], "Label test 123")
        self.assertGreater(len(response_data["content"]), 0)
