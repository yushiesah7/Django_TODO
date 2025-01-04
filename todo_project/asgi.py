"""
ASGI (Asynchronous Server Gateway Interface)の設定ファイルだぜ！

Djangoアプリを非同期で動かすための設定が書いてある。
Reactでいうと、サーバーサイドの処理を効率的に行うための裏方みたいなもんだ。

このファイルは、Djangoがリクエストを処理する方法を定義している。
具体的には、ASGIという規格を使って、WebサーバーとDjangoアプリの間でデータをやり取りする。

もっと簡単に言うと、
「WebサーバーからのリクエストをDjangoアプリに渡すための橋渡し役」
みたいなもんだと思ってくれ。

詳細な情報は、公式ドキュメントを見てくれ！
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 環境変数DJANGO_SETTINGS_MODULEを設定している。
# これで、Djangoがどの設定ファイルを使うか教えている。
# Reactでいうと、環境変数を使って、開発環境と本番環境で設定を切り替えるみたいなもんだ。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

# DjangoのASGIアプリケーションを取得している。
# これが、Webサーバーからのリクエストを処理するメインの処理になる。
# Reactでいうと、ReactDOM.render()でアプリを起動するみたいなもんだ。
application = get_asgi_application()
