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

    def add_student(self, grade: int, class_: str, name: str) -> int:
        self.table[grade - 1]['classes'][class_ - 1]['students'].append(name)
        return 0

    def remove_student(self, grade: int, class_: str, name: str) -> int:
        try:
            del self.table[grade - 1]['classes'][class_ - 1]['students'][
                self.table[grade - 1]['classes'][class_ - 1]['students'].index(name)]
            return 0
        except ValueError:
            return -1

    def list_student(self, grade: int, class_: int) -> int:
        for students in self.table[grade - 1]['classes'][class_ - 1]['students']:
            print(f'  {students}')
        return 0

    def from_file_load_student(self, filename: str) -> int:
        try:
            with open(filename, 'r') as f:
                self.table = json.load(f)
            return 0
        except FileNotFoundError:
            return -1

    def save_student_to_file(self, filename: str) -> int:
        if os.path.exists(filename):
            _user_input = input('文件已存在，是否覆盖？(y/n)：')
            if _user_input == 'y' or _user_input == 'Y':
                with open(filename, 'w') as f:
                    json.dump(self.table, f, skipkeys=True,
                            ensure_ascii=False, indent=2)
                return 0
            elif _user_input == 'n' or _user_input == 'N':
                return -1
        else:
            with open(filename, 'w') as f:
                json.dump(self.table, f, skipkeys=True,
                        ensure_ascii=False, indent=2)
            return 0
