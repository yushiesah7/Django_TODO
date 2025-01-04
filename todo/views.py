from rest_framework import viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer


# ModelViewSetは、Django REST Frameworkが提供する便利なクラスで、
# CRUD（作成、読み取り、更新、削除）の処理をまとめてやってくれるんだ。
# Reactでいうと、APIとのやり取りを抽象化して、
# データの取得や更新を簡単にしてくれるライブラリみたいなものかな。
class TodoViewSet(viewsets.ModelViewSet):
    # querysetは、どのデータを扱うかを指定するんだ。
    # ここでは、Todoモデルの全てのオブジェクトを取得するように設定している。
    # Reactでいうと、APIから取得するデータの範囲を指定するようなもの。
    queryset = Todo.objects.all()
    # serializer_classは、取得したデータをJSON形式に変換したり、
    # JSON形式のデータをTodoモデルに変換したりするためのクラスを指定するんだ。
    # ここでは、TodoSerializerを使っている。
    # Reactでいうと、APIから受け取ったデータをコンポーネントで使いやすい形に変換したり、
    # コンポーネントから送るデータをAPIが理解できる形に変換したりする処理をまとめたもの。
    serializer_class = TodoSerializer
