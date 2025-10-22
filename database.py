def get_connection():
    import psycopg2
    return psycopg2.connect(host="db_host", database="uhear", user="user", password="pwd")
