import psycopg2

# 建立資料庫連接
conn = psycopg2.connect(
    host="localhost",
    database="handsome66",
    user="postgre",
    password="1234"
)

# 創建一個游標
cur = conn.cursor()

# 执行SQL查询
cur.execute("SELECT gender FROM PATIENTS_6 ")

# 獲取所有行
rows = cur.fetchall()

# 关闭游標和数据库连接
cur.close()
conn.close()

# 输出结果
print(rows)
