#  Куда пойти — Москва глазами Артёма

Интерактивная карта Москвы с локациями, описаниями и фотографиями.  
Проект разработан на Django, и предназначен для демонстрации достопримечательностей в формате, удобном для контент-менеджеров и пользователей.
Ссылка на сайт - https://caker.pythonanywhere.com


---

##  Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/yourusername/where-to-go.git
cd where-to-go
```

### 2. Установите зависимости
```
pip install -r requirements.txt
```

### 3. Создайте .env файл
Пример содержимого:
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
```
- SECRET_KEY -
A secret key for a particular Django installation.
Используется для криптографической подписи и должна быть уникальной и непредсказуемой.
- ALLOWED_HOSTS -
Список доменных имён или IP-адресов, на которых разрешён запуск сайта.
Например: 127.0.0.1,localhost,caker.pythonanywhere.com
- DEBUG -
Включает или отключает режим отладки.
При DEBUG=True показываются подробные ошибки и трассировки.
Документация

### 4. Примените миграции и создайте суперпользователя
```
python manage.py migrate
python manage.py createsuperuser
```

### 5. Запустите сервер
```
python manage.py runserver
```
Откройте сайт на - http://127.0.0.1:8000
Админка: http://127.0.0.1:8000/admin/

## Как редактировать контент

В админке вы можете добавлять локации с:
- названием
- координатами
- кратким и длинным описанием (с HTML-редактором)
- фото (можно сортировать drag&drop)

## Пример запуска команды загрузки данных

После запуска проекта вы можете загрузить места из JSON-файла с помощью встроенной команды Django:

```bash
python manage.py load_place путь_до_json_файла
```
Примеры:
- Загрузка из файла:
```
python manage.py load_place places/json_sources/moscow_legends.json
```
- Загрузка с URL:
```
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/moscow_legends.json
```
После выполнения команды в консоли появится лог загрузки:
```
Загружаю: Экскурсионная компания «Легенды Москвы»
Добавлено 5 изображений
```
### Формат JSON-файла:
```
{
  "title": "Экскурсионная компания «Легенды Москвы»",
  "imgs": [
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/example1.jpg",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/example2.jpg"
  ],
  "description_short": "Краткое описание места...",
  "description_long": "<p>Полное описание с <b>HTML</b>-разметкой.</p>",
  "coordinates": {
    "lat": 55.753676,
    "lng": 37.620795
  }
}
```

