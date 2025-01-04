import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Todo
# from todo.models import Todo
from django.db import models

@pytest.fixture
def api_client() -> APIClient:
    return APIClient()

@pytest.fixture
def todo_data(db: models.Model) -> tuple[Todo, Todo]:
    todo1 = Todo.objects.create(title="Test Todo 1")
    todo2 = Todo.objects.create(title="Test Todo 2", completed=True)
    return todo1, todo2

def test_get_all_todos(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    response = api_client.get('/api/todos/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

def test_create_todo(api_client: APIClient, db: models.Model):
    new_todo = {'title': 'New Todo'}
    response = api_client.post('/api/todos/', new_todo, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Todo.objects.count() == 1

def test_get_single_todo(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    todo1, _ = todo_data
    response = api_client.get(f'/api/todos/{todo1.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Test Todo 1'

def test_update_todo(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    todo1, _ = todo_data
    updated_todo = {'title': 'Updated Todo', 'completed': True}
    response = api_client.put(f'/api/todos/{todo1.id}/', updated_todo, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Updated Todo'
    assert response.data['completed'] == True

def test_delete_todo(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    todo1, _ = todo_data
    response = api_client.delete(f'/api/todos/{todo1.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Todo.objects.count() == 1
