"""
URL configuration for todo_project project.

このファイルは、URLとどの処理（View）を結びつけるかを設定する場所だよ！
Reactでいうと、ルーティングの設定ファイルみたいなもの。
どのURLにアクセスしたら、どのコンポーネントを表示するかを決めるのと同じだよ。

詳しくは公式ドキュメントを見てね！
https://docs.djangoproject.com/en/5.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include

# urlpatternsは、URLとViewを紐付けるためのリストだよ。
# Reactでいうと、ルーティングの設定を記述する場所。
urlpatterns = [
    # /admin/ というURLにアクセスすると、Djangoの管理サイトが表示されるよ。
    # これはDjangoが自動で用意してくれている便利な機能。
    # Reactでいうと、管理画面用のコンポーネントみたいなもの。
    path("admin/", admin.site.urls),
    # /api/ というURLにアクセスすると、todoアプリのurls.pyに処理が移るよ。
    # include()は、他のurls.pyファイルの内容をこのファイルに含めるためのもの。
    # Reactでいうと、ルーティングの設定を別のファイルに分割して、それをimportするみたいな感じ。
    path("api/", include("todo.urls")),
]
