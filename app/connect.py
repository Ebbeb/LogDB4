import cx_Oracle


class Connect:
    def connectdb(self):
            conn = cx_Oracle.connect('u1/adminhh@10.242.0.75:1521/xe')
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM log')
            count = cursor.fetchone()[0]

            return print('Count = %d\n', count)
