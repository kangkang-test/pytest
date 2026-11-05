import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# 建表
# 用户表：id(主键)、用户名、年龄、城市
cur.execute("""
	create table users (
		id integer primary key,
		username text,
		age integer,
		city text )
""")

# 订单表
# 订单id 、用户id(关联 user.id)、金额、状态
cur.execute("""
	create table orders (
		oid integer primary key,
		user_id integer,
		amount real,
		status text)
""")

# 插入测试数据
users = [
    (1, 'kangkang', 38, '北京'),
    (2, 'test_user', 25, '上海'),
    (3, 'guest', 30, '北京')
]
cur.executemany("insert into users values (?,?,?,?)",users)

orders = [
    (1, 1, 100.0, "paid"),
    (2, 1, 200.0, "paid"),
    (3, 2, 50.0, "pending"),
    (4, 1, 80.0, "refunded")
]
cur.executemany("insert into orders values (?,?,?,?)",orders)
conn.commit()

# 查数据
print("==1. 查所有用户(select *) ==")
cur.execute("select * from users")
for row in cur.fetchall():
    print(row)

print("==2. 查北京的用户（where 条件过滤) ==")
cur.execute("select *from users where city = '北京'")
for row in cur.fetchall():
    print(row)

print("==3. 按年龄从大到小排 （order by) ==")
cur.execute("select * from users order by age desc")
for row in cur.fetchall():
    print(row)

print("==4. 每个用户的订单数 （join + group by ,测试最常用） ==")
cur.execute("""
select u.username, count(o.oid) as order_cnt from users u left join orders o on u.id = o.user_id group by u.username
""")
for row in cur.fetchall():
    print(row)

print(" \n==5. 已支付（paid)订单的总金额（where + sum) ==")
cur.execute("select sum(amount) from orders where status = 'paid'")
print("已支付总额：", cur.fetchone()[0])
conn.close()