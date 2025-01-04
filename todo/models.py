from django.db import models

class Todo(models.Model):
    # title はタスクの名前。CharField は文字列を保存するフィールドで、max_length は最大文字数。
    title = models.CharField(max_length=200)
    # completed はタスクが完了したかどうかを示すフラグ。BooleanField は True か False を保存するフィールドで、default=False は初期値を False に設定。
    completed = models.BooleanField(default=False)
    # created_at はタスクが作成された日時。DateTimeField は日時を保存するフィールドで、auto_now_add=True はレコードが作成された時に自動的に現在日時を設定。
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at はタスクが更新された日時。DateTimeField は日時を保存するフィールドで、auto_now=True はレコードが更新されるたびに自動的に現在日時を設定。
    updated_at = models.DateTimeField(auto_now=True)

    # __str__ は、このモデルのインスタンスを文字列として表現する方法を定義。
    # ここでは、タスクのタイトルを返すように設定。
    def __str__(self):
        return self.title
