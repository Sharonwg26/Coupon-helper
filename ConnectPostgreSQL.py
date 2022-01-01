import psycopg2


class PostgresBaseManager:

    def __init__(self):
        self.database = 'd7fqnoe9p5est6'
        self.user = 'bsuubhmujsqxtm'
        self.password = '935b5874b7c000f373645f6e7d65d91d4349b7b5e815f7b9919f6a8162eea810'
        self.host = 'ec2-3-213-76-170.compute-1.amazonaws.com'
        self.port = '5432'
        self.conn = self.connectServerPostgresDb()

    def connectServerPostgresDb(self):
        # 連接 Heroku Postgres SQL 認證用
        conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)
        return conn

    def runServerPostgresDb(self):
        #測試是否可以連線到 Heroku Postgres SQL
        cur = self.conn.cursor()
        cur.execute('SELECT VERSION()')
        results = cur.fetchall()
        print("Database version : {0} ".format(results))
        self.conn.commit()
        cur.close()
    
    def SELECT_number(self,choose):
        cur = self.conn.cursor()
        cur.execute('SELECT num FROM '+choose+'_prize_number')
        results = cur.fetchall()
        self.conn.commit()
        cur.close()
        return results

    def SELECT_data(self,choose,city):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM '+choose+'_'+city)
        results = cur.fetchall()
        self.conn.commit()
        cur.close()
        return results
        

    def closePostgresConnection(self):
        self.conn.close()
