#### Если еще не перешли в папку, переходим:
```bash
cd space_rangers_gjango
```

#### Создаем и активируем виртуальное окружение для linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

#### Обновиляем pip и установим зависимости из req.txt:
```bash
python -m pip install --upgrade pip && pip install -r req.txt
```

#### Выполнить миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Запуск сервера
```bash
python manage.py runserver
```

### Разработчик проекта
- [Смелов Илья](https://github.com/PivnoyFei)