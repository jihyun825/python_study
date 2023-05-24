import pymysql
class DaoEmp():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',port=3305, password='python',
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""select * from emp where e_id = {e_id}"""
        self.curs.execute(sql)
        emp = self.curs.fetchall()
        return emp[0]
    
    def insert(self,e_id,e_name,sex,addr):
        sql = f"""INSERT INTO emp VALUES({e_id},{e_name},{sex},{addr})"""
        self.curs.execute(sql)
        self.conn.commit()
        return  self.curs.rowcount
    
    def delete(self,e_id):
        sql = f"""delete from emp where e_id = {e_id}"""
        self.curs.execute(sql)
        self.conn.commit()
        return  self.curs.rowcount
    
    def update(self,e_id,e_name,sex,addr):
        sql = f"""update emp set e_name = {e_name},sex={sex},addr ={addr} where e_id={e_id}"""
        self.curs.execute(sql)
        self.conn.commit()
        return  self.curs.rowcount
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        

if __name__ == '__main__':
    de = DaoEmp()
    res = de.update('4','7','7','7')
    print("res",res)