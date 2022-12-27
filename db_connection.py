import pymysql


# Make Connection by DataBase
class DBConn:

    def __init__(self, conn_info):

        kind_of_db = conn_info['kind']
        host_ip = conn_info['hostIp']
        port = int(conn_info['port'])
        username = conn_info['userNm']
        password = conn_info['passWd']
        dbname = conn_info['dbName']

        # mysql and mariadb
        if kind_of_db == 'mysql':
            self.conn = pymysql.connect(host=host_ip, port=port, user=username, password=password,
                                        db=dbname, charset='utf8mb4')
        else:
            self.conn = None
