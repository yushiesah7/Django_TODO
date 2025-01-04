# pre-commitの使い方ガイド

## 背景

Reactではコミット前に自動でコードフォーマットや静的解析を行うツールが一般的に使用されており、コード品質の維持が容易です。しかし、Django+Pythonのプロジェクトではこれらの自動化が必ずしも標準で設定されているわけではありません。

- コードの一貫性の欠如
- バグの早期発見が困難
- チーム開発時の統一感の欠如

## 問題定義

Djangoプロジェクトでコミット前に自動的にコードフォーマットと静的解析を実行する仕組みが整っておらず、開発効率とコード品質に課題が生じています。

**.pre-commit-config.yaml**

```python
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  - repo: https://gitlab.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

## pre-commitとは

pre-commitはGitのコミットプロセスにフックを追加し、コミット前に自動的に指定したツールを実行するためのツールです。これにより、手動でツールを実行する手間を省き、コード品質を継続的に維持することができます。

- コードフォーマットの自動化
- 静的解析によるバグの検出
- コミット時の自動チェック

## なぜpre-commitを使うのか

pre-commitを使用することで、チーム全体で一貫したコードスタイルを維持し、潜在的なバグを早期に発見することができます。これにより、開発プロセスが効率化され、コードの品質が向上します。

- 自動化による手間の削減
- コード品質の向上
- チーム間の統一感の確保

## pre-commitの導入手順

- `pre-commit` をインストールする:

**  **

```python
pip install pre-commit
```

- プロジェクトルートに `.pre-commit-config.yaml` を作成する:

**.pre-commit-config.yaml**

```python
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  - repo: https://gitlab.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```

- pre-commitフックをインストールする:

**  **

```python
pre-commit install
```

- すべてのファイルに対してフックを実行する:

**  **

```python
pre-commit run --all-files
```

これらの手順を実行することで、コミット時に自動的にBlackとFlake8が実行され、コードのフォーマットと静的解析が行われます。

## pre-commitの使用方法

pre-commitを正しく設定すると、コミット時に自動的にフックが実行されます。以下の点を確認してください：

- フックのインストールが完了していること
- `.pre-commit-config.yaml` に必要なフックが設定されていること
- Gitが正しく設定されていること

```
$ git commit -m "コードの修正"
black....................................................................Passed
flake8...................................................................Passed
[ブランチ名] コミットメッセージ
```

## トラブルシューティング

pre-commitの設定や実行中に問題が発生した場合、以下の手順で解決を試みてください。

- キャッシュをクリアする:

**  **

```python
pre-commit clean
```

- フックを再インストールする:

**  **

```python
pre-commit install
```

- フックを手動で実行する:

**  **

```python
pre-commit run --all-files
```

- ログを確認してエラーメッセージを解析する

これらの手順を通じて、pre-commitの問題を解決し、スムーズな開発プロセスを維持することができます。

## まとめ

pre-commitを導入することで、Django+PythonプロジェクトにおいてもReact同様に効率的なコードフォーマットと静的解析を自動化できます。これにより、コード品質の維持とバグの早期発見が可能となり、開発プロセスが大幅に改善されます。

- pre-commitのインストールと設定
- 自動化されたコードフォーマットと静的解析の実行
- 継続的なコード品質の維持
