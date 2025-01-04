#!/usr/bin/env python
"""Djangoのコマンドラインユーティリティ。管理タスクに使います。"""
import os
import sys


def main():
    """管理タスクを実行します。"""
    # Djangoの設定ファイルがどこにあるかを教える。
    # Reactでいうと、環境変数みたいなもの。
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
    try:
        # Djangoのコマンドを実行する関数をインポート
        # Reactでいうと、何かのライブラリをimportする感じ
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # もしDjangoがインストールされてなかったら、エラーを出す
        # Reactでいうと、ライブラリがインストールされてない時にエラーが出る感じ
        raise ImportError(
            "Djangoがインストールされてないか、Pythonの環境変数にパスが通ってないみたい。"
            "仮想環境をアクティベートするのを忘れてない？"
        ) from exc
    # コマンドラインから渡された引数を使って、Djangoのコマンドを実行
    # Reactでいうと、npm startとか、そういうコマンドを実行する感じ
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # このファイルが直接実行されたら、main関数を実行する
    # Reactでいうと、エントリーポイントみたいなもの
    main()
