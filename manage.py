#!/usr/bin/env python
"""Djangoのコマンドラインユーティリティ。管理タスクに使います。"""
import os
import sys

# このスクリプトが直接実行された時に、以下のコードが実行されるよ！
# Reactでいうと、`index.js`とか`main.js`みたいな、アプリのエントリーポイント的な役割を果たす部分だね。
if __name__ == "__main__":
    # Djangoの設定ファイル（`settings.py`）の場所を環境変数に設定するよ。
    # これがないと、Djangoがどこに設定ファイルがあるか分からなくなっちゃうんだ。
    # Reactでいうと、`.env`ファイルとかで環境変数を設定するのに近いかな。
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_project.settings")

    # Djangoのコマンドラインツールを実行するための関数をインポートするよ。
    # Reactでいうと、`npm start`とか`npm run build`みたいなコマンドを実行するのに近いかな。
    from django.core.management import execute_from_command_line

    # コマンドラインから渡された引数を使って、Djangoのコマンドを実行するよ。
    # 例えば、`python manage.py runserver`とか`python manage.py migrate`みたいなコマンドを実行する時に、
    # この関数が実際にDjangoの処理を動かしてくれるんだ。
    # Reactでいうと、`npm start`とか`npm run build`を実行した時に、
    # 内部でWebpackとかが動いてくれるのと同じような感じかな。
    execute_from_command_line(sys.argv)
