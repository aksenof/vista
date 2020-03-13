# hi vista
from mysql import connector

db = connector.connect(
	host="localhost", 
	user="admin", 
	passwd="admin",
	database="newdatabase"
)
db_cursor = db.cursor()

def sql_select():
    db_cursor.execute("SELECT * FROM wishlist")
    fetch_all = db_cursor.fetchall()
    return fetch_all

def sql_delete(del_id):
    sql = "DELETE FROM wishlist WHERE id = {}".format(del_id)
    db_cursor.execute(sql)
    db.commit()

def sql_update(update_id, name, price, link, note):
    sql = "UPDATE wishlist SET name = '{}', price = '{}', link = '{}', note = '{}' WHERE id = {}".format(
        name, price, link, note, update_id
    )
    db_cursor.execute(sql)
    db.commit()

def sql_insert(name, price, link, note):
    db_cursor.execute("SELECT * FROM wishlist")
    result = db_cursor.fetchall()
    new_id = len(result) + 1
    sql = "INSERT INTO wishlist (id, name, price, link, note) VALUES (%s, %s, %s, %s, %s)"
    values = (new_id, name, price, link, note)
    db_cursor.execute(sql, values)
    db.commit()

def auto_inc():
    db_cursor.execute("SELECT * FROM wishlist")
    result = db_cursor.fetchall()
    old_ids = list(i[0] for i in result)
    new_ids = list(range(1, len(result)+1))
    for i in range(len(old_ids)):
        sql_update_ids = "UPDATE wishlist SET id = {} WHERE id = {}".format(
            new_ids[i],
            old_ids[i]
        )
        db_cursor.execute(sql_update_ids)
        db.commit()
