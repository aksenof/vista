# vista
Тестовое задание от ООО "Виста" для вакансии "Junior Python Разработчик"

<b> Инструкция по запуску и работе: </b>

1. Для начала необходимо скачать и установить последнюю версию Python 3:

https://www.python.org

python 3.7.2 (данная версия актуальна на 16.03.19)

2. Скачать и установить MySQL:

https://dev.mysql.com/downloads/installer/

3. Скачать и установить MySQL Connector for Python 3:

https://dev.mysql.com/downloads/connector/python/

Или установить mysql-connector-python с помощью pip:

pip install mysql-connector-python

4. После установки MySQL, запустить MySQL Workbench и добавить пользователя:

user: admin

password: admin

Administrative Roles: All roles and privileges

5. Клонировать/скачать репозиторий vista, используя ssh/http/zip:

ssh: git@github.com:aksenof/vista.git

http: https://github.com/aksenof/vista.git

zip: https://github.com/aksenof/vista/archive/master.zip

6. Запустить файл install_db.py с помощью python для установки БД, таблицы "wishlist" и примера "example" :

python install_db.py

Результат запуска должен содержать следующии строки:

MySQLCursor: DROP DATABASE IF EXISTS newdatabase

MySQLCursor: CREATE DATABASE newdatabase

MySQLCursor: CREATE TABLE wishlist (id INT,name VARCH..

MySQLCursor: INSERT INTO wishlist (id, name, price, l..

7. Запустить файл run.py для запуска интерфейса с таблицей, содержащей пример "example" :

python run.py

8. Пример "example":

![example](https://raw.githubusercontent.com/aksenof/vista/master/example.png)
