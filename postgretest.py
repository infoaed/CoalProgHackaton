import psycopg2

params = {
  'dbname': 'coalprog',
  'user': 'indrek',
  'password': 'korru',
  'host': '172.16.1.245',
  'port': 5432
}


conn = psycopg2.connect(**params)

print 'test'

cur = conn.cursor()

cur.execute("""SELECT *
FROM information_schema.columns
WHERE table_name = 'SYNDMUS'""")
cur.fetchall()

cur.execute("""SELECT * from public.syndmus""")

print cur.fetchone()