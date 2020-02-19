import pymysql
class connector():
    def __init__(self, host='localhost', 
                       user='test',
                       password='123456',
                       db='db_test'):
        self.connect = pymysql.connect(host, user, password, db)
        self.cursor = self.connect.cursor()

    def searchByName(self, name):
        command = '''
        SELECT 
            payment.id `id`, 
            customer.name `name`, 
            payment.amount `amount`, 
            payment.paydate `paydate` 
        FROM payment 
            INNER JOIN 
                customer 
            ON 
                customer.id = payment.customer 
                AND 
                customer.name = '%s';
        '''
        self.cursor.execute(command % (name))
        return self.cursor.fetchall()

    def lastTen(self):
        command = '''
        SELECT 
            payment.id `id`, 
            customer.name `name`, 
            payment.amount `amount`, 
            payment.paydate `paydate` 
        FROM payment 
            INNER JOIN 
                customer 
            ON
                customer.id = payment.customer 
            LIMIT 10
        '''
        self.cursor.execute(command)
        return self.cursor.fetchall()