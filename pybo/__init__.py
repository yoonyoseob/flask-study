from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# db 객체를 블루프린트 같은 다른 모듈에서 불러올 수 있도록 create_app함수 밖에서 선언

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    # create_app안에서 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루 프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
