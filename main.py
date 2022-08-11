#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.sql
import os

if __name__ == '__main__':
    _user_password = {}
    with open('password.txt', 'r') as _f:
        _files = _f.readlines()
    for _file in _files:
        _user_password[_file.split()[0]] = _file.split()[1]

    print('欢迎进入系统')
    print('请登录')
    while 1:
        _user_input = input('请输入用户名和密码：')
        _user_input = _user_input.strip().split()
        if _user_password[_user_input[0]] == _user_input[1]:
            break
        elif _user_input[0] not in _user_password:
            print('注册用户须得到管理员的许可，请向管理员提出申请')
        else:
            print('用户名或密码错误！')

    if os.path.exists('data'):
        _link = lib.sql.School(grades=-1, classes=-1)
        _link.load_file('data')
    else:
        _link = lib.sql.School(grades=6, classes=5)
    print('登录成功')
    print(f'欢迎您，{_user_input[0]}')
    print('添加学生请按1')
    print('删除学生请按2')
    print('查询学生请按3')
    print('退出系统请输入exit')
    print('保存数据请输入save')
    print('从文件中还原数据请输入load')
    print('再次查看本帮助请输入help')
    while 1:
        _user_input = input('请输入：')
        if _user_input == 'exit':
            break
        elif _user_input == 'save':
            _link.save_file('data')
        elif _user_input == 'load':
            _link.load_file('data')
        elif _user_input == 'help':
            print('添加学生请按1')
            print('删除学生请按2')
            print('查询学生请按3')
            print('退出系统请输入exit（直接退出不会保存！）')
            print('保存数据请输入save')
        elif _user_input == '1':
            print('例子：六年级是6，六（3）班级则是603')
            print('注意，六（10）班仍然是6010')
            _user_input = input('请输入学生的年级班级姓名并用一个空格分开：')
            _user_input = _user_input.strip().split()
            _grade = int(_user_input[0])
            _class = _user_input[1]
            _name = _user_input[2]
            _link.add(_grade=_grade, _class=_class, _name=_name)
        elif _user_input == '2':
            print('例子：六年级是6，六（3）班级则是603')
            print('注意，六（10）班仍然是6010')
            _user_input = input('请输入学生的年级班级姓名并用一个空格分开：')
            _user_input = _user_input.strip().split()
            _grade = int(_user_input[0])
            _class = _user_input[1]
            _name = _user_input[2]
            _link.remove(_grade=_grade, _class=_class, _name=_name)
        elif _user_input == '3':
            print('例子：六年级是6，六（3）班级则是603')
            print('注意，六（10）班仍然是6010')
            _user_input = input('请输入年级和班级：')
            _link.list_(*_user_input.strip().split())
        else:
            print('输入错误！')
    _link.save_file('data')
    print('数据已保存')
