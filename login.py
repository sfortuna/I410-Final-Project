import MySQLdb as db

def select(n):
    con=db.connect(host="127.0.0.1", database='I430',user="root",passwd="Denali 2015")
    cur=con.cursor()
    query=("SELECT * FROM accounts"
          "WHERE name = %s")
    cur.execute("SELECT * FROM accounts WHERE name = %s", (n,))
    data=cur.fetchall()
    cur.close()
    return data
