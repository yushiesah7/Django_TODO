from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Todo

# ここからテストケースを書いていくよ！
# TestCaseは、Djangoが提供するテスト用のクラスで、これを使うとテストが書きやすくなるんだ。
class TodoTests(TestCase):
    # setUpメソッドは、各テストメソッドが実行される前に必ず実行されるよ。
    # ここでは、APIクライアントの初期化と、テスト用のTodoデータを作成しているんだ。
    # Reactでいうと、各テストケースで使う共通の初期設定みたいなものかな。
    def setUp(self):
        # APIClientは、APIのエンドポイントをテストするためのクライアントだよ。
        # これを使うと、実際にHTTPリクエストを送信して、レスポンスを検証できるんだ。
        # Reactでいうと、axiosとかfetchを使ってAPIを叩くのと同じような感じかな。
        self.client = APIClient()
        # テスト用のTodoデータを2つ作成。
        # 1つは完了していないタスク、もう1つは完了済みのタスク。
        self.todo1 = Todo.objects.create(title="Test Todo 1")
        self.todo2 = Todo.objects.create(title="Test Todo 2", completed=True)

    # test_get_all_todosメソッドは、全てのTodoを取得するAPIをテストするメソッドだよ。
    def test_get_all_todos(self):
        # APIにGETリクエストを送信して、レスポンスを受け取る。
        response = self.client.get('/api/todos/')
        # レスポンスのステータスコードが200 OKであることを検証。
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # レスポンスのデータ（JSON形式）の長さが2であることを検証。
        # これは、setUpで作成したTodoデータが2つあるから。
        self.assertEqual(len(response.data), 2)

    # test_create_todoメソッドは、新しいTodoを作成するAPIをテストするメソッドだよ。
    def test_create_todo(self):
        # 新しいTodoデータを作成するための辞書。
        new_todo = {'title': 'New Todo'}
        # APIにPOSTリクエストを送信して、新しいTodoを作成。
        response = self.client.post('/api/todos/', new_todo, format='json')
        # レスポンスのステータスコードが201 Createdであることを検証。
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Todoモデルのレコード数が3になっていることを検証。
        # これは、setUpで2つ、このテストで1つ作成したから。
        self.assertEqual(Todo.objects.count(), 3)

    # test_get_single_todoメソッドは、特定のIDのTodoを取得するAPIをテストするメソッドだよ。
    def test_get_single_todo(self):
        # APIにGETリクエストを送信して、特定のIDのTodoを取得。
        response = self.client.get(f'/api/todos/{self.todo1.id}/')
        # レスポンスのステータスコードが200 OKであることを検証。
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # レスポンスのデータのtitleが、setUpで作成したtodo1のtitleと同じであることを検証。
        self.assertEqual(response.data['title'], 'Test Todo 1')

    # test_update_todoメソッドは、既存のTodoを更新するAPIをテストするメソッドだよ。
    def test_update_todo(self):
        # 更新するTodoデータを作成するための辞書。
        updated_todo = {'title': 'Updated Todo', 'completed': True}
        # APIにPUTリクエストを送信して、Todoを更新。
        response = self.client.put(f'/api/todos/{self.todo1.id}/', updated_todo, format='json')
        # レスポンスのステータスコードが200 OKであることを検証。
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # レスポンスのデータのtitleが、更新後のtitleと同じであることを検証。
        self.assertEqual(response.data['title'], 'Updated Todo')
        # レスポンスのデータのcompletedが、更新後のcompletedと同じであることを検証。
        self.assertEqual(response.data['completed'], True)

    # test_delete_todoメソッドは、Todoを削除するAPIをテストするメソッドだよ。
    def test_delete_todo(self):
        # APIにDELETEリクエストを送信して、Todoを削除。
        response = self.client.delete(f'/api/todos/{self.todo1.id}/')
        # レスポンスのステータスコードが204 No Contentであることを検証。
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Todoモデルのレコード数が1になっていることを検証。
        # これは、setUpで2つ作成し、このテストで1つ削除したから。
        self.assertEqual(Todo.objects.count(), 1)
