### Памятка по выполнению тестового задания

1. ### SQL для создания схемы базы данных.

<p>Создал бд с помощью django models. Так-же знаю как это сделать на языке SQL</p>

    CREATE TABLE calls(
        crime_id int,
        original_crime_type_name datetime,
        report_date datetime,
    )

2. ## Скрипт для загрузки данных

<p>Сделал загрузку данных в админке django. Функционал прописан в /main_app/admin.py класс PoliceCallsAdmin
<img src="https://i.ibb.co/pbBGLYp/Screenshot-4.png" alt="Screenshot-4" border="0" width="500">
<img src="https://i.ibb.co/p45C16s/Screenshot-5.png" alt="Screenshot-5" border="0">
</p>

3. ## Файл с указанием зависимостей

<p>Файл requirements.txt</p>

4. ## LOG-файл с выводом результата работы скрипта

<p>Лог файл importing_log.log выглядит примерно так:</p>

    2022-08-10 02:46:09.203915 загружено 16 записей | 0.6829988956451416 sec

## Разработал API на базе Django REST Framework

Вывод записей из БД:

    http://127.0.0.1:8000/api/v1/calls/

<img src="https://i.ibb.co/Fw0f8V3/image.png" alt="image" border="0">

Сделал пагинацию по 20 записей:

    http://127.0.0.1:8000/api/v1/calls/?page=2

Сделал фильтр по полю report_date:

    http://127.0.0.1:8000/api/v1/calls/?date_after=2016-04-02&date_before=2016-05-02

<p>P.S. Прошу прощения если есть где-то недочеты, старался все сделать по заданию с применением своих знаний.<br>
Готов исправить/доделать если что-то упустил.</p>