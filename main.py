# import pandas as pd
# import mysql.connector
# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Ansarbhular53@",
#     database = "hotel"
#
# )
# cursor=db.cursor()
# cursor.execute("Select * from employee where age <=30 ")

from modules_recipe import *

# try:
#     add_order(6,"Pizza and Burger",30)
#     print("The Order has Successfully Placed. ")
#
# except:
#     print("There is Some Error in Order Placing.")


# try:
#     delete_order(3)
#     print("The Order has Successfully Deleted. ")
# except:
#     print("There is Some Error in Order Deletion.")

# try:
#     viewbyid(1)
#     # print("The Order has Successfully Deleted. ")
# except:
#     print("There is Some Error in Results Showing")

try:
    print("The Detail has Shown. ")
    viewbyorder(30)
except:
    print("There is Some Error in Results Showing")


# try:
#
#     update_order(1, "Pizza")
#     print("The Order has been Updated. ")
# except:
#     print("There is Some Error in Order Update. ")