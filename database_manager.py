import psycopg2
from hash_generator import get_hexdigest

def connect_db():
    try:
        print('Connecting to PostgresSQL db')
        conn = psycopg2.connect(host="localhost", database="adrian",user="adrian",password="password")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def sign_up():
    try:
        conn = connect_db()
        print('Please enter a new username:')
        new_username = input()
        print('Now select a password')
        password = input()
        password = get_hexdigest(new_username, password)[:50]
        with conn.cursor() as cur:
            cur.execute("INSERT INTO master_pwd (name,password) VALUES(%s,%s);",(new_username,password))
            conn.commit()
            cur.execute("SELECT name,password,id FROM master_pwd WHERE name = %s AND password = %s ;",(username, password))
            credentials = cur.fetchall()
        conn.close()
        return credentials[0]        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def login():
    try:
        conn = connect_db()
        print('Enter your username')
        username = input()
        print('Enter your password')
        password = input()
        password = get_hexdigest(username,password)[:50]

        with conn.cursor() as cur:
            cur.execute("SELECT name,password,id FROM master_pwd WHERE name = %s AND password = %s ;",(username, password))
            credentials = cur.fetchall()
           
        conn.close()  
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    if not credentials:
        print('user not registred, quiting...')
        quit()
    else:
        return credentials[0]             

def store_password(pwd, usr, email, app, id):
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO apps_pwd (password,username,email,app_name,id) VALUES(%s,%s,%s,%s,%s);",(pwd,usr,email,app,id))
            conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def select_app(app, id):
    try:
        conn = connect_db()        
        with conn.cursor() as cur:
            cur.execute("SELECT password,username,email FROM apps_pwd WHERE app_name = %s AND id = %s;",(app, id))
            accounts = cur.fetchall()
        conn.close()     
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return accounts

def select_email(email, id):
    try:
        conn = connect_db()        
        with conn.cursor() as cur:
            cur.execute("SELECT password,username,app_name FROM apps_pwd WHERE email = %s AND id = %s;",(email, id))
            accounts = cur.fetchall()
        conn.close()     
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return accounts    

def select_username(username,id):
    try:
        conn = connect_db()        
        with conn.cursor() as cur:
            cur.execute("SELECT password,app_name,email FROM apps_pwd WHERE username = %s AND id = %s;",(username, id))
            accounts = cur.fetchall()
        conn.close()     
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return accounts 
            
               
def select_all_credentials(id):
    try:
        conn = connect_db()        
        with conn.cursor() as cur:
            cur.execute("SELECT username,password,app_name,email FROM apps_pwd WHERE id = %s GROUP BY username,password,app_name,email;",(id,))
            accounts = cur.fetchall()
        conn.close()     
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return accounts


           