### 💼 Сайт регистрации и авторизации пользователей Flask

```
💻 Команды для запуска приложения
   
   1. Установка необходимых библиотек:
   python -m pip install Flask SQLAlchemy Flask-Login
   
   2. Запуск приложения:
   flask run
```

```
flask_app/
│
├── app.py                        # Основной файл приложения
├── config.py                     # Конфигурационные параметры
├── generate_secret_key.py        # Конфигурация secret_key
├── forms.py                      # Основные формы
├── models.py                     # Основные модели базы данных
├── script.py                     # Создание базы данных (вручную)
├── views.py                      # Основные представления и обработка запросов
├── requirements.txt              # Зависимости проекта
│
├── static/                       # Папка для статических файлов (CSS, JavaScript, изображения)
│   └── styles.css                # Файл с пользовательскими стилями
│
├── templates/                    # Папка для HTML-шаблонов
│   ├── base.html                 # Базовый шаблон (макет)
│   ├── index.html                # Шаблон для главной страницы
│   ├── login.html                # Шаблон для страницы входа
│   └── register.html             # Шаблон для страницы регистрации
│
├── analytics/                    # Модуль аналитики (если применимо)
│   ├── __init__.py               # Инициализация модуля
│   ├── models.py                 # Модели базы данных
│   ├── views.py                  # Представления и обработка запросов
│   └── forms.py                  # Формы для модуля аналитики
│
├── auth/                         # Модуль аутентификации (если применимо)
│   ├── __init__.py               # Инициализация модуля
│   ├── models.py                 # Модели базы данных
│   ├── views.py                  # Представления и обработка запросов
│   └── forms.py                  # Формы для модуля аутентификации
│
└── migrations/                   # Папка для миграций базы данных (если используете Flask-Migrate)
```

🖥️ **Автор:** Дуплей Максим Игоревич

📅 **Дата:** 04.08.2024
