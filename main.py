# import sqlite3

# # Create a SQL connection to our SQLite database
# con = sqlite3.connect("data/portal_mammals.sqlite")

# cur = con.cursor()

# # The result of a "cursor.execute" can be iterated over by row
# for row in cur.execute('SELECT * FROM species;'):
#     print(row)

# # Be sure to close the connection
# con.close()
# # import sqlite3
# # connection = sqlite3.connect('gta.db')

# # release_list = [
# #     (1997,'grand auto','new jersey'),
# #     (1999,'toyota','anywhere','USA'),
# #     (2000,'vice city','vice city'),
# #     (2001,'auto','location','uk'),
# # ]
# # connection.close()