import MySQLdb as db

def create_database():
    con=db.connect(user="root",passwd="Test 2016")
    cur=con.cursor()
    sql='CREATE DATABASE IF NOT EXISTS I430'
    try:
        cur.execute(sql)
    except Exception as e:
        print "Error",e,"occurred.."
    con.close()

def create_table():
    con=db.connect(host="127.0.0.1",database="I430",user="root",passwd="Test 2016")
    cur=con.cursor()
    sql=''' CREATE TABLE IF NOT EXISTS accounts (
            Name CHAR(20),
            URL VARCHAR(50),
            username VARCHAR(25),
            password VARCHAR(20)
            )'''
    cur.execute(sql)
    con.close()

def insert(n,u,un,pw):
    con=db.connect(host="127.0.0.1", database='I430',user="root",passwd="Test 2016")
    cur=con.cursor()
    sql="INSERT INTO accounts VALUES(%s,%s,%s,%s)"
    cur.execute("INSERT INTO accounts(Name,URL,username,password) VALUES(%s,%s,%s,%s)",(n, u, un, pw))
    con.commit()
    print "Info added!"
    con.close()

