import cx_Oracle


class Connect:
    def connectdb(self):
            conn = cx_Oracle.connect('u1/adminhh@10.242.0.75:1521/xe')
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM log')
            count = cursor.fetchone()[0]

            return print('Count = %d\n', count)

    def searchdb(self):
            conn = cx_Oracle.connect('u1/adminhh@10.242.0.75:1521/xe')
            cursor = conn.cursor()
            statement = "SELECT COUNT(*) FROM log WHERE NAME = 'StatusBrightness'"

            cursor.execute(statement)
            result = cursor.fetchone()[0]
            return result
