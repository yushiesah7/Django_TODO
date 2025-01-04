"""
WSGI (Web Server Gateway Interface) の設定ファイルだよ！

DjangoアプリをWebサーバー（例えば、ApacheやNginx）で動かす時に、
このファイルがDjangoとWebサーバーの間を取り持ってくれるんだ。
Reactでいうと、ブラウザとReactアプリの間でデータのやり取りを仲介するAPIサーバーみたいなものかな。

詳しくは公式ドキュメントを見てね！
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 環境変数 'DJANGO_SETTINGS_MODULE' に、Djangoの設定ファイル（settings.py）の場所を設定しているよ。
# Reactでいうと、環境変数にAPIのエンドポイントを設定するみたいな感じ。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

# DjangoアプリのWSGIアプリケーションを取得しているよ。
# これが、WebサーバーからのリクエストをDjangoアプリに渡すための入り口になるんだ。
# Reactでいうと、APIサーバーのエントリーポイントみたいなもの。
application = get_wsgi_application()
