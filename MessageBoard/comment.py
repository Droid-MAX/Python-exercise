#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# by Droid-MAX
"""
使用Python的Web框架，做一个Web版本的留言板
"""

import sqlite3, sys
from bottle import route, run, debug, template, request, static_file, error, redirect

# 强制编码
reload(sys)
sys.setdefaultencoding('utf8')

# 全局连接数据库
conn = sqlite3.connect('db/comment.db')

# 中文编码hack
conn.text_factory = str


# ----------------------------------------------------
# 首页
@route('/')
def comments_list():
    c = conn.cursor()
    c.execute("SELECT id,name,comment,date_time FROM comments ORDER BY id DESC")
    result = c.fetchall()
    c.close()
    output = template("tpl/comment_list", rows=result)
    return output

# ----------------------------------------------------
# 新建任务
@route('/new', method='GET')
def new_item():
    if request.GET.get('save','').strip():
        name = request.GET.get('name', '').strip()
        comment = request.GET.get('comment', '').strip()
        c = conn.cursor()
        c.execute("INSERT INTO comments (name,comment) VALUES (?,?)", (name,comment))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return "<script>window.location.replace('/');</script>"

# ----------------------------------------------------
# 编辑
@route('/edit/:no', method='GET')
def edit_item(no):
    if request.GET.get('save','').strip():
        name_r = request.GET.get('name', '').strip()
        comment_r = request.GET.get('comment', '').strip()
        c = conn.cursor()
        c.execute("UPDATE comments SET name = ?, comment = ? WHERE id LIKE ?" ,(name_r, comment_r, no))
        conn.commit()
        return "<script>window.location.replace('/');</script>"
    else:
        c = conn.cursor()
        c.execute("SELECT name, comment FROM comments WHERE id LIKE ?" ,[str(no)])
        cur_data = c.fetchone()
        #print cur_data
        return template('tpl/edit', old=cur_data, no=no)

# ----------------------------------------------------
# 删除留言
@route('/delete/:no', method='GET')
def delete_item(no):
    if request.GET.get('delete','').strip():
        name = request.GET.get('name', '').strip()
        comment = request.GET.get('comment', '').strip()
        c = conn.cursor()
        c.execute("DELETE FROM comments WHERE id LIKE ?" ,[str(no)])
        conn.commit()
        return "<script>window.location.replace('/');</script>"


@error(403)
def mistake403(code):
    return '参数格式错误！'

@error(404)
def mistake404(code):
    return '该页面不存在！'

@route('/static/:filename')
def serve_static(filename):
    return static_file(filename, root='./static/')

debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
