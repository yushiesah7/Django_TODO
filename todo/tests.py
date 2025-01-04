import pytest
from rest_framework.test import APIClient
from rest_framework import status
from todo.models import Todo
from django.db import models


# @pytest.fixture は、Reactでいうところのテスト用のモックデータを作る関数みたいなもんだと思ってください。
# ここでは、APIクライアントのインスタンスを返す関数を定義しています。
@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


# ここでは、テスト用のTodoデータを作成する関数を定義しています。
# db: models.Model は、Djangoのモデルを操作するためのデータベース接続みたいなもんです。
# Reactでいうと、テスト用のモックデータを作るみたいな感じ。
@pytest.fixture
def todo_data(db: models.Model) -> tuple[Todo, Todo]:
    todo1 = Todo.objects.create(title="Test Todo 1")
    todo2 = Todo.objects.create(title="Test Todo 2", completed=True)
    return todo1, todo2


# ここからが実際のテスト関数です。
# api_clientとtodo_dataを引数として受け取っています。
# Reactのテストでいうと、describeとかitみたいなもんです。
def test_get_all_todos(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    # api_clientを使って、/api/todos/にGETリクエストを送信します。
    response = api_client.get("/api/todos/")
    # レスポンスのステータスコードが200 OKであることを確認します。
    assert response.status_code == status.HTTP_200_OK
    # レスポンスのデータ数が2つであることを確認します。
    assert len(response.data) == 2


def test_create_todo(api_client: APIClient, db: models.Model):
    # 新しいTodoデータを作成します。
    new_todo = {"title": "New Todo"}
    # api_clientを使って、/api/todos/にPOSTリクエストを送信します。
    response = api_client.post("/api/todos/", new_todo, format="json")
    # レスポンスのステータスコードが201 Createdであることを確認します。
    assert response.status_code == status.HTTP_201_CREATED
    # Todoモデルのオブジェクト数が1つであることを確認します。
    assert Todo.objects.count() == 1


def test_get_single_todo(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    # todo_dataから最初のTodoオブジェクトを取得します。
    todo1, _ = todo_data
    # api_clientを使って、/api/todos/{todo1.id}/にGETリクエストを送信します。
    response = api_client.get(f"/api/todos/{todo1.id}/")
    # レスポンスのステータスコードが200 OKであることを確認します。
    assert response.status_code == status.HTTP_200_OK
    # レスポンスのデータのタイトルが"Test Todo 1"であることを確認します。
    assert response.data["title"] == "Test Todo 1"


def test_update_todo(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    # todo_dataから最初のTodoオブジェクトを取得します。
    todo1, _ = todo_data
    # 更新するTodoデータを作成します。
    updated_todo = {"title": "Updated Todo", "completed": True}
    # api_clientを使って、/api/todos/{todo1.id}/にPUTリクエストを送信します。
    response = api_client.put(f"/api/todos/{todo1.id}/", updated_todo, format="json")
    # レスポンスのステータスコードが200 OKであることを確認します。
    assert response.status_code == status.HTTP_200_OK
    # レスポンスのデータのタイトルが"Updated Todo"であることを確認します。
    assert response.data["title"] == "Updated Todo"
    # レスポンスのデータのcompletedがTrueであることを確認します。
    assert response.data["completed"] is True


def test_delete_todo(api_client: APIClient, todo_data: tuple[Todo, Todo]):
    # todo_dataから最初のTodoオブジェクトを取得します。
    todo1, _ = todo_data
    # api_clientを使って、/api/todos/{todo1.id}/にDELETEリクエストを送信します。
    response = api_client.delete(f"/api/todos/{todo1.id}/")
    # レスポンスのステータスコードが204 No Contentであることを確認します。
    assert response.status_code == status.HTTP_204_NO_CONTENT
    # Todoモデルのオブジェクト数が1つであることを確認します。
    assert Todo.objects.count() == 1
