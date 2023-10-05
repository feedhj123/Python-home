import pymysql

host = '3.34.98.157'
user ='root'
port=3306
password = 'pythonmysql'
database = 'mycompany'
conn = pymysql.connect(port=port,host=host,user=user,
                       password=password,database=database)
cursor = conn.cursor()
sql = "SELECT EMPNO, ENAME, JOB ,SAL ,DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor.execute(sql)
results = cursor.fetchall()
for emp in results :
    print(emp[1],emp[3],sep=',\t') 
cursor.close()
conn.close()