import os

from app import create_app

# app 参数配置
flask_env = os.getenv("FLASK_ENV")
app_options = {"env":flask_env}

app = create_app(app_options)

if __name__ == '__main__':
    app.run()
