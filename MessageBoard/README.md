> 使用 Bottle + SQLite 制作的一个极简留言板。

## 用法

安装好相应的依赖库后，进入目录，生成数据库文件（如果没有）：

	python2 setup_db.py

然后启动：
	
	python2 comment.py

然后登录 `http://localhost:8080/` 即可。

## 目录树
	.
	├── db
	│   └── comment.db （数据库文件）
	├── setup_db.py（初始安装数据库）
	├── static（静态文件目录）
	│   ├── help.html
	│   ├── primer.css
	│   └── style.css
	├── comment.py（核心文件）
	└── tpl（模板文件）
    	├── footer.tpl
    	├── header.tpl
    	├── comment_list.tpl
    	├── edit.tpl

