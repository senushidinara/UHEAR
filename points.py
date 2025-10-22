import psycopg2

def add_points(user_id, points):
    conn = psycopg2.connect(host="db_host", database="uhear", user="user", password="pwd")
    cur = conn.cursor()
    cur.execute("INSERT INTO points_history(user_id, points) VALUES (%s,%s)", (user_id, points))
    conn.commit()
    cur.close()
    conn.close()
