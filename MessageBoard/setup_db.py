#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Droid-MAX
"""
安装相关数据库的数据
"""

import sqlite3
con = sqlite3.connect('./db/comment.db')

con.execute("CREATE TABLE comments (id INTEGER PRIMARY KEY, name char(40) NOT NULL, comment char(200) NOT NULL, date_time date DEFAULT (datetime('now','localtime')) NOT NULL)")
con.execute("INSERT INTO comments (name,comment,date_time) VALUES ('傻狍子','欢迎来到我的留言板，请在这里写下你想对我说的话！','2017-11-25')")
con.commit()

"""
测试
"""

c = con.cursor()
c.execute("SELECT name,comment,date_time FROM comments ORDER BY id")
result = c.fetchall()
c.close()
print result
