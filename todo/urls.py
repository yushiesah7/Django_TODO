from django.urls import path, include
from rest_framework import routers
from .views import TodoViewSet

# ここがポイント！
# DefaultRouterは、RESTfulなAPIのエンドポイントを自動で生成してくれる便利なやつ。
# 例えば、/todos/ にGETリクエストを送ると、Todoの一覧が取得できたり、
# /todos/1/ にGETリクエストを送ると、idが1のTodoが取得できたりする。
# Reactでいうと、APIのエンドポイントを自分で書かなくても、
# いい感じに作ってくれる魔法の箱みたいなもの。
router = routers.DefaultRouter()

# ここで、/todos というURLに対して、TodoViewSetというViewを紐付けている。
# TodoViewSetは、todo/views.pyで定義した、Todoモデルを操作するためのクラス。
# Reactでいうと、APIからデータを取得したり、更新したりする処理をまとめた関数みたいなもの。
# r'todos' は正規表現で、URLのパスの一部を表す。
# この場合、/todos というURLにアクセスすると、TodoViewSetが処理を行う。
router.register(r'todos', TodoViewSet)

# urlpatternsは、URLとViewを紐付けるためのリスト。
# path('', include(router.urls)) は、
# ルートURL（例えば、http://localhost:8000/）にアクセスすると、
# routerが生成したURLを全て含めるという意味。
# Reactでいうと、ルーティングの設定みたいなもの。
# どのURLにアクセスしたら、どのコンポーネントを表示するかを決めるのと同じ。
urlpatterns = [
    path('', include(router.urls)),
]
