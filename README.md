![mytube_workflow](https://github.com/Seniacat/MyTube/actions/workflows/main.yml/badge.svg)
# MyTube
MyTube - проект социальной сети в которой можно публиковать свои записи и комментировать чужие, подписываться на любимых авторов и ставить лайки.

  Проект реализован на MVT-архитектуре, реализована система регистрации новых пользователей, настройка пользовательского профиля, восстановление паролей пользователей через почту, система тестирования проекта на unittest, пагинация постов и кэширование страниц, структура древовидных комментариев. Проект имеет верстку с адаптацией под размер экрана устройства пользователя.
 Реализовано CI и CD проекта. При push изменений в главную ветку проект автоматические тестируется на соотвествие требованиям PEP8 и проверяется внутренними автотестами (pytest). После успешного прохождения тестов собирается обзраз web-контейнера Docker и автоматически размещается в DockerHub. Размещенный образ автоматически разворачивается на боевом сервере вмете с контейнером веб-сервера nginx и базы данных PostgreSQL.
  Проект находится в активной разработке.

## Системные требования
- Python 3.7+
- Works on Linux, Windows, macOS
- 
## Стек технологий:
- Python 3.7
- Django 3.2
- SQLite3
- Bootstrap 4
- JavaScript
- HTML
- CSS

### Запуск проекта в Docker-контейнере
Клонировать репозиторий и перейти в него в командной строке. Перейти в папку проекта:
```
git clone https://github.com/Seniacat/MyTube.git
cd MyTube/
```
Должен быть свободен порт 8000. PostgreSQL поднимается на 5432 порту, он тоже должен быть свободен.
Cоздать и открыть файл .env с переменными окружения:
```
cd infra/
touch .env
```
Заполнить .env файл с переменными окружения по примеру (SECRET_KEY см. в файле settings.py). 
Необходимые для работы проекта переменные окружения можно найти в файле .env.example в текущей директории:
```
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

echo DB_HOST=db  >> .env

echo DB_PORT=5432  >> .env

echo SECRET_KEY=************ >> .env
```
Установить и запустить приложения в контейнерах (образ для контейнера web загружается из DockerHub):
```
docker-compose up -d
```
Запустить миграции, создать суперюзера, собрать статику и заполнить БД:
```
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 
```
### Развитие проекта
Проект находится в стадии развития, есть планы по расширению функциональности: реализация возможности переписки между пользователями, возможности ставить лайки и выводить данные о количестве просмотров постов 
