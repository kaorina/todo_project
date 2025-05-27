# Django Todo API

DjangoとDjango REST Frameworkを使用したTodo管理アプリケーションです。

## 機能

- Todoの作成、読み取り、更新、削除（CRUD）
- ユーザー認証（ログイン/ログアウト）
- RESTful API
- フロントエンド（SPA）

## 技術スタック

- Python 3.12
- Django 5.2
- Django REST Framework
- SQLite（開発環境）/ PostgreSQL（本番環境）
- Heroku（デプロイ）

## セットアップ手順

### 開発環境

1. リポジトリのクローン
```bash
git clone git@github.com:kaorina/todo_project.git
cd todo_project
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

3. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
```bash
# シークレットキーの生成
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

`.env`ファイルを作成し、以下の内容を設定：
```
DJANGO_SECRET_KEY='generate-a-secure-secret-key'  # 上記で生成したキーを使用
DJANGO_ENV='development'
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1  # 開発環境でのアクセスを許可するホスト
DEBUG=True  # 開発環境ではTrue、本番環境では必ずFalseに設定
```

5. データベースのマイグレーション
```bash
python manage.py migrate
```

6. 開発サーバーの起動
```bash
python manage.py runserver
```

### 本番環境（Heroku）

1. Heroku CLIのインストール
```bash
brew install heroku/brew/heroku
```

2. Herokuにログイン
```bash
heroku login
```

3. Herokuアプリの作成
```bash
heroku create todo-project
```

4. 環境変数の設定
```bash
# 環境変数の設定
heroku config:set DJANGO_ENV=production
heroku config:set DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') # シークレットキーを生成してセット
heroku config:set DJANGO_ALLOWED_HOSTS=todo-project-0d99ba5e08f9.herokuapp.com
heroku config:set DEBUG=False  # 本番環境では必ずFalseに設定
```

5. PostgreSQLデータベースの追加
```bash
heroku addons:create heroku-postgresql:essential-0
```

6. デプロイ
```bash
git push heroku main
```

7. データベースのマイグレーション
```bash
heroku run python manage.py migrate
```

8. 管理者ユーザーの作成
```bash
heroku run python manage.py createsuperuser
```

## ユーザー管理

### 管理者ユーザーの作成
```bash
python manage.py createsuperuser  # 開発環境
heroku run python manage.py createsuperuser  # 本番環境
```

### 一般ユーザーの作成
```bash
python manage.py shell  # 開発環境
heroku run python manage.py shell  # 本番環境
```

シェルで以下のコードを実行：
```python
from django.contrib.auth.models import User
User.objects.create_user(username='username', password='password', email='email@example.com')
```

## APIエンドポイント

- `GET /api/todos/` - Todo一覧の取得
- `POST /api/todos/` - 新規Todoの作成
- `GET /api/todos/{id}/` - 特定のTodoの取得
- `PUT /api/todos/{id}/` - 特定のTodoの更新
- `DELETE /api/todos/{id}/` - 特定のTodoの削除

## 認証

- セッション認証を使用
- ログイン: `/login/`
- ログアウト: `/logout/`

## 注意事項

- 本番環境では必ず`DEBUG=False`を設定
- 本番環境では新しい`SECRET_KEY`を生成して使用（Djangoの`get_random_secret_key()`を使用）
- 本番環境では`ALLOWED_HOSTS`を適切に設定
- 環境変数は`.env`ファイルで管理（Gitにコミットしない）
- シークレットキーは絶対にGitにコミットしない 