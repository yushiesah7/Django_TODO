from rest_framework import serializers
from .models import Todo

# TodoモデルをJSONに変換したり、JSONからTodoモデルを作成したりするためのクラスだよ！
# Reactでいうと、APIから受け取ったデータをコンポーネントで使いやすい形に変換したり、
# コンポーネントから送るデータをAPIが理解できる形に変換したりするのに近いかな。
class TodoSerializer(serializers.ModelSerializer):
    # このクラスは、どのモデルを扱うかをMetaクラスで定義するよ。
    class Meta:
        # Todoモデルを扱うことを宣言
        model = Todo
        # JSONに含めるフィールドを指定。
        # id, title, completed, created_at, updated_at を含めるよ。
        # これらはTodoモデルの属性（プロパティ）に対応しているんだ。
        fields = ['id', 'title', 'completed', 'created_at', 'updated_at']
        # read_only_fields は、このフィールドが読み取り専用であることを指定します。
        # 例えば、id, created_at, updated_at はAPIから変更されるべきではないので、読み取り専用に設定します。
        # Reactでいうと、コンポーネント内で表示はするけど、ユーザーが直接編集できないフィールドみたいなものです。
        read_only_fields = ['id', 'created_at', 'updated_at']

        # extra_kwargs は、各フィールドに対して追加の設定を行うためのものです。
        # 例えば、titleフィールドに対して、必須であることを指定したり、最大文字数を指定したりできます。
        # Reactでいうと、フォームの入力フィールドに対して、バリデーションルールを設定するようなものです。
        extra_kwargs = {
            'title': {'required': True, 'max_length': 200},
            'completed': {'required': False}, # completed は必須ではない
        }

        # 以下はよく使う設定ではありませんが、知っておくと便利な設定です。

        # depth は、関連するモデルをどれだけ深くシリアライズするかを指定します。
        # 例えば、TodoモデルがUserモデルと関連している場合、depth=1とすると、Userモデルの情報も一緒にJSONに含めることができます。
        # Reactでいうと、親コンポーネントから子コンポーネントにpropsとして渡すデータが、さらに深い階層のデータを含んでいるようなイメージです。
        # depth = 1 # 例

        # validators は、フィールドに対してカスタムのバリデーションルールを設定するためのものです。
        # 例えば、titleフィールドが特定のパターンに一致するかどうかをチェックしたりできます。
        # Reactでいうと、カスタムのバリデーション関数を定義して、フォームの入力値をチェックするようなものです。
        # validators = [validators.UniqueValidator(queryset=Todo.objects.all())] # 例

        # exclude は、JSONに含めたくないフィールドを指定します。
        # 例えば、特定のフィールドをAPIレスポンスから除外したい場合に便利です。
        # Reactでいうと、コンポーネントに渡すpropsから、特定のデータを削除するようなイメージです。
        # exclude = ['created_at'] # 例

        # fields = '__all__' とすると、モデルの全てのフィールドをJSONに含めることができます。
        # fields = '__all__' # 例

        # モデルのフィールド以外に、Serializerに独自のフィールドを追加することもできます。
        # 例えば、Todoモデルにない「is_urgent」というフィールドを追加して、
        # 特定の条件でTrue/Falseを返すようにすることも可能です。
        # Reactでいうと、コンポーネント内で計算された値を表示するようなイメージです。
        # is_urgent = serializers.SerializerMethodField()
        # def get_is_urgent(self, obj):
        #     return obj.completed == False and obj.created_at.day == datetime.now().day

        # SerializerMethodFieldを使う場合は、get_フィールド名 というメソッドを定義する必要があります。
        # この例では、get_is_urgent というメソッドを定義しています。
        # このメソッドは、Todoモデルのインスタンスを引数として受け取り、
        # is_urgentフィールドの値を計算して返します。
        # Reactでいうと、コンポーネント内でpropsやstateを使って計算した値を返す関数のようなものです。
        # def get_is_urgent(self, obj):
        #     return obj.completed == False and obj.created_at.day == datetime.now().day
