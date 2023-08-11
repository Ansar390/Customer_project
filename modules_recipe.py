



import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ansarbhular53@",
    database = "recipe"

)
cursor=db.cursor()
# cursor.execute("")

def add_order(ord_id,ord_items,bill):
    if ord_id and ord_items and bill:
        values=(ord_id,ord_items,bill)
        cursor.execute("insert into orders (ord_id,ord_items,bill) values (%s,%s,%s)",values)
        db.commit()
        cursor.close()

def delete_order(ord_id):
    if ord_id:
        cursor.execute("delete from orders where ord_id = %s",(ord_id,))
        db.commit()
        cursor.close()

def viewbyid(ord_id):
    if ord_id:
        cursor.execute("select * from orders where ord_id = %s",(ord_id,))
        for i in cursor:
            print(i)
        db.commit()
        cursor.close()

def viewbyorder(bill):
    if bill:
        cursor.execute("select * from orders where bill = %s", (bill,))
        for i in cursor:
            print(i)
        db.commit()
        cursor.close()


def update_order(ord_id,order_items):
    if ord_id:
        cursor.execute("update orders set ord_items = %s where ord_id =%s",(order_items,ord_id,))
        db.commit()
        cursor.close()