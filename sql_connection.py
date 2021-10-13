import mysql.connector

#defining global varibale for connection __cnx
__cnx = None

#modularizing the sql connection
#using global __cnx to ensure that connection only made when it is None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='RAJmama14',
                                        host='127.0.0.1',
                                        database='gs')

    return __cnx