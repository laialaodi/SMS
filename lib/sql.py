#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os


class School:
    def __init__(self, grades: int, classes: int) -> None:
        self.table = []
        for _i in range(1, grades + 1):
            self.table.append(
                {'type': 'grade', 'name': f'{_i}', 'classes': []})
            for _j in range(1, classes + 1):
                self.table[_i - 1]['classes'].append(
                    {'type': 'class', 'name': f'{_j}', 'students': []})

    def add_student(self, grade: int, class_: int, name: str) -> int:
        '''向指定班级添加学生

        参数
            grade{int} - 年级
            class_{int} - 班级
            name{str} - 姓名

        返回值
            0 - 正常运行
            -1 - IndexError
        '''
        try:
            self.table[grade - 1]['classes'][class_ - 1]['students'].append(name)
            return 0
        except IndexError:
            return -1

    def remove_student(self, grade: int, class_: int, name: str) -> int:
        '''由指定班级删除学生

        参数
            grade{int} - 年级
            class_{int} - 班级
            name{str} - 姓名

        返回值
            0 - 正常运行
            -1 - ValueError
            -2 - IndexError
        '''
        try:
            del self.table[grade - 1]['classes'][class_ - 1]['students'][
                self.table[grade - 1]['classes'][class_ - 1]['students'].index(name)]
            return 0
        except ValueError:
            return -1
        except IndexError:
            return -2

    def list_student(self, grade: int, class_: int) -> int:
        '''列出指定班级的学生

        参数
            grade{int} - 年级
            class_{int} - 班级

        返回值
            0 - 正常运行
        '''
        for students in self.table[grade - 1]['classes'][class_ - 1]['students']:
            print(f'  {students}')
        return 0

    def from_file_load_student(self, filename: str) -> int:
        '''从指定文件加载数据

        参数
            filename{str} - 文件名

        返回值
            0 - 正常运行
            -1 - FileNotFoundError
        '''
        try:
            with open(filename, 'r') as f:
                self.table = json.load(f)
            return 0
        except FileNotFoundError:
            return -1

    def save_student_to_file(self, filename: str) -> int:
        '''向指定文件保存数据

        参数
            filename{str} - 文件名

        返回值
            0 - 正常运行
            -1 - 用户取消覆盖
        '''
        if os.path.exists(filename):
            _user_input = input('文件已存在，是否覆盖？(y/n)：')
            if _user_input == 'y' or _user_input == 'Y':
                with open(filename, 'w') as f:
                    json.dump(self.table, f, skipkeys=True,
                              ensure_ascii=False, indent=2)
            elif _user_input == 'n' or _user_input == 'N':
                return -1
        else:
            with open(filename, 'w') as f:
                json.dump(self.table, f, skipkeys=True,
                          ensure_ascii=False, indent=2)
        return 0
