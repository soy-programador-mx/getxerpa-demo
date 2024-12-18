from rest_framework.test import APIClient
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_transaction():

    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

    client = APIClient()
    # Using the standard RequestFactory API to create a form POST request
    payload = [
        {
            "description": "Uber",
            "amount": -100,
            "date": "2024-12-17"
        },
        {
            "description": "Testing1",
            "amount": "100",
            "date": "2024-12-17"
        }
    ]
  
    # Create a task  
    response_create = client.post("/transaction/", data=payload, format="json")

    assert response_create.status_code == 201