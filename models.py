import sqlite3 as sql
from datetime import datetime

def insertUser(email,password,is_driver):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,password,is_driver) VALUES (?,?,?)", (email,password,is_driver))
    con.commit()
    con.close()

def selectUserByEmail(email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, email, password, is_driver FROM users WHERE email = ?", [email])
    user = cur.fetchone()
    con.close()
    return user

def selectUserById(user_id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, email,password,is_driver FROM users WHERE id = ?", [user_id])
    user = cur.fetchone()
    con.close()
    return user

def insertCall(passenger, address):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO calls (passenger, address) VALUES (?, ?)", (passenger, address))
    con.commit()
    con.close()

def updateCall(call_id, driver):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("UPDATE calls SET driver = ?, dispatch_time = ? WHERE id = ?", (driver, datetime.now().strftime("%B %d, %Y %I:%M%p"), call_id))
    #cur.execute("UPDATE calls SET driver = ? WHERE id = ?", (driver, call_id))
    con.commit()
    con.close()

def selectCallList():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, passenger, address, driver, request_time, dispatch_time FROM calls ORDER BY id DESC")
    user = cur.fetchall()
    con.close()
    return user

def selectCallById(call_id):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT id, passenger, address, driver, request_time, dispatch_time FROM calls WHERE id = ?", [call_id])
    user = cur.fetchone()
    con.close()
    return user
