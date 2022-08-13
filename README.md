# 关于

用 python 实现的轻量级学生管理系统 (Student Management System)

实现了：

- 登录系统
- 增删查学生
- 以 JSON 格式保存、导入（还原）

# 详细介绍

## 登录

初次登录须修改 `password.txt` 文件以注册账户，添加一行文字，格式如`<User Name> <Password>`，密码不能包含空格。请注意，中间只能有一个空格！

启动程序后按提示登录即可。

## 命令手册

目前程序支持的命令有：

增删查类

- 1 ： 在指定班级添加学生
- 2 ： 在指定班级删除学生
- 3 ： 查询指定班级的学生

文件类

- save ： 保存数据
- load ： 导入（还原）数据

- help ： 在程序里查看命令帮助

## 保存和导入

程序的保存功能使用了 python 内置的 `json` 模块，保存时数据通过文件流被写入，导入时同理。