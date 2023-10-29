
## **Описание тестового задания file uploader:** 

#### Тестовое задание: Загрузка и обработка файлов

<details>
 <summary>Цель</summary>
    Разработать Django REST API, который позволяет загружать файлы на сервер,
    а затем асинхронно обрабатывать их с использованием Celery.
</details>

<details>
 <summary>Требования</summary> 

+ Создать Django проект и приложение.
+ Использовать Django REST Framework для создания API.
+ Реализовать модель File, которая будет представлять загруженные файлы. Модель должна содержать поля:
  + file: поле типа FileField, используемое для загрузки файла.
  + uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
  + processed: поле типа BooleanField, указывающее, был ли файл обработан.
+ Реализовать сериализатор для модели File.
+ Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.
+ Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.
+ Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.
</details>


<details>
  <summary>Запуск проекта</summary>


**Создать секретный ключ приложения:**
```
Создать файл .env в корневой папке проекта
Сгенерировать секретный ключ с помощью команды:

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

Заполнить файл env по шаблону:
    SECRET_KEY = <ваш секретный ключ>
    ALLOWED_HOSTS=<IP сервера>, <Домен сервера>
    POSTGRES_USER=django_user
    POSTGRES_PASSWORD=django_password
    POSTGRES_DB=django_db
    
    DB_HOST=db
    DB_PORT=5432
```

**Запустить компоус файл:** 
``` 
docker-compose up --build
```

#### После выполнения вышеперечисленных инструкций бэкенд проекта будет доступен по адресу http://127.0.0.1:8000/
</details>



## Технологии: 

+ Python 3.9
+ Django: 3.2.3
+ Django REST framework: 3.12.4
+ Celery 5.3.4


## спецификация OpenAPI
http://127.0.0.1:8000/redoc/

# Автор
+ FilippVasichev
+ ![GitHub](https://img.shields.io/badge/GitHub-FilippVasichev-brightgreen)
+ ![Gmail](https://img.shields.io/badge/Gmail-aciktrasher@gmail.com-red)
+ ![Telegram](https://img.shields.io/badge/Telegram-@zionweeds-blue)


