#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print('欢迎登录学生管理系统')
    while 1:
        print('添加学生请按1')
        print('删除学生请按2')
        print('查询学生请按3')
        user_input = input('请输入：')
        if user_input == 1:
            add()
        elif user_input == 2:
            rmv()
        elif user_input == 3:
            pass
        else:
            print('输入错误！')
