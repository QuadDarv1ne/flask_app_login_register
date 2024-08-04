from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import requests
from flask import request, url_for

# Инициализация Flask-приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Инициализация базы данных
db = SQLAlchemy(app)

# Инициализация менеджера входа
login_manager = LoginManager(app)
login_manager.login_view = 'main.login'  # Указание представления для страницы входа

# Импорт и регистрация Blueprint-ов
from views import main_bp
from analytics.views import analytics_bp

app.register_blueprint(main_bp)
app.register_blueprint(analytics_bp, url_prefix='/analytics')

@app.before_request
def track_page_view():
    if request.endpoint != 'analytics.track':
        data = {'path': request.path}
        requests.post(url_for('analytics.track', _external=True), json=data)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)