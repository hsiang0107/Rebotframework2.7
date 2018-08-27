from lib.db import db_utilities

conn = db_utilities.make_connection()
cur = conn.cursor()
sel_sql = 'select AddressLine1 from Person.Address where AddressID = ?'
data = cur.execute(sel_sql, 1).fetchone()

# print(cur.description)
print(data)
# print(data[0])
# print(data.AddressLine1)


# sql_file = '..//resource//db//sql_script.sql'
# cur = db_utilities.exec_sql_file(cur, sql_file)
# data = cur.execute("select ProductCategoryID, Name, rowguid from Production.ProductCategory where Name = 'test7'").fetchone()
# print(data)


cur.close()
