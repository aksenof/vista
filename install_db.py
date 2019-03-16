from mysql import connector


def create_db():
	db = connector.connect(
		host="localhost", 
		user="admin", 
		passwd="admin"
	)
	db_cursor = db.cursor()
	base_name = "newdatabase"
	sql_drop_db = "DROP DATABASE IF EXISTS {}".format(base_name)
	sql_create_db = "CREATE DATABASE {}".format(base_name)
	db_cursor.execute(sql_drop_db)
	print(db_cursor)
	db_cursor.execute(sql_create_db)
	print(db_cursor)
	return base_name


def create_table(data_base):
	db = connector.connect(
		host="localhost", 
		user="admin", 
		passwd="admin",
		database=data_base
	)
	key_id = "id INT"
	name = "name VARCHAR(255)"
	price = "price VARCHAR(255)"
	link = "link VARCHAR(255)"
	note = "note VARCHAR(255)"
	sql_create_table = "CREATE TABLE wishlist ({},{},{},{},{})".format(
		key_id, name, price, link, note)
	db_cursor = db.cursor()
	db_cursor.execute(sql_create_table)
	print(db_cursor)


def create_example():
	name = "Product 1"
	price = "1$"
	link = "https://example1.com"
	note = "Note 1"
	db = connector.connect(
		host="localhost",
		user="admin",
		passwd="admin",
		database="newdatabase"
	)
	db_cursor = db.cursor()
	db_cursor.execute("SELECT * FROM wishlist")
	result = db_cursor.fetchall()
	new_id = len(result) + 1
	sql = "INSERT INTO wishlist (id, name, price, link, note) VALUES (%s, %s, %s, %s, %s)"
	values = (new_id, name, price, link, note)
	db_cursor.execute(sql, values)
	print(db_cursor)
	db.commit()

create_table(create_db())
create_example()
