#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.sql

if __name__ == '__main__':
    link = lib.sql.School(grades=6, classes=5)
    path = '/'
    print('欢迎登录学生管理系统')
    while 1:
        print('添加学生请按1')
        print('删除学生请按2')
        print('查询学生请按3')
        _user_input = input('请输入：')
        if _user_input == 'exit':
            break
        elif _user_input == '1':
            _user_input = input('请输入学生的年级班级姓名并用一个空格分开：')
            _grade = int(_user_input.split()[0])
            _class = _user_input.split()[1]
            _name = _user_input.split()[2]
            link.add(_grade=_grade, _class=_class, _name=_name)
        elif _user_input == '2':
            _user_input = input('请输入学生的年级班级姓名并用一个空格分开：')
            _grade = int(_user_input.split()[0])
            _class = _user_input.split()[1]
            _name = _user_input.split()[2]
            link.remove(_grade=_grade, _class=_class, _name=_name)
        elif _user_input == '3':
            _user_input = input('请输入年级和班级：')
            link.list_(*_user_input.strip().split())
        else:
            print('输入错误！')
