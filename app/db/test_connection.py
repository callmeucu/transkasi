from app.helper.helper import get_pg_connection


def test_pg_connection():
    try:
        conn = get_pg_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        print ("connection to PostgreSQL Succesful!")
        return True
    except Exception as e:
        print (f"connection to PostgreSQL failed! : {e}")
        return False

if __name__ == "__main__":
    test_pg_connection()