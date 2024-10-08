from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from .models import TrainModel


class TrainModelAPITestCase(APITestCase):
    """
    Test Training Model API endpoints.
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@example.com",
            password="testpassword",
            is_staff=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)
        self.model_data = {
            "number": 1,
            "name": "Test Model",
            "description": "This is a test model",
        }
        self.create_url = "/models/create/"
        self.update_url = "/models/update/"
        self.delete_url = "/models/delete/"

    def test_create_model(self):
        """
        Test creating a new model.
        """
        response = self.client.post(self.create_url, self.model_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TrainModel.objects.count(), 1)
        self.assertEqual(TrainModel.objects.get().name, self.model_data["name"])

    def test_get_list_of_models(self):
        """
        Test retrieving a list of models.
        """
        TrainModel.objects.create(**self.model_data)
        response = self.client.get("/models/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_update_model(self):
        """
        Test updating an existing model.
        """
        model = TrainModel.objects.create(**self.model_data)
        updated_data = {
            "number": 2,
            "name": "Updated Model",
            "description": "This is an updated model",
        }
        response = self.client.put(
            f"{self.update_url}{model.id}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        model.refresh_from_db()
        self.assertEqual(model.name, updated_data["name"])

    def test_delete_model(self):
        """
        Test deleting an existing model.
        """
        model = TrainModel.objects.create(**self.model_data)
        response = self.client.delete(f"{self.delete_url}{model.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(TrainModel.objects.filter(id=model.id).exists())
