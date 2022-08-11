#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class School:
    def __init__(self, grades: int, classes: int) -> None:
        self.table = []
        for i in range(1, grades + 1):
            self.table.append({'type': 'grade', 'name': f'{i}', 'classes': {}})
            for j in range(1, classes + 1):
                self.table[i - 1]['classes'][f'{i}0{j}'] = {'type': 'class', 'name': f'{i}0{j}', 'students': []}

    def add(self, _grade: int, _class: str, _name: str) -> None:
        self.table[_grade - 1]['classes'][_class]['students'].append(_name)

    def remove(self, _grade: int, _class: str, _name: str) -> None:
        try:
            del self.table[_grade - 1]['classes'][_class]['students'][
                self.table[_grade - 1]['classes'][_class]['students'].index(_name)]
        except ValueError:
            print('您删除了一个不存在的数值！')

    def list_(self, _grade: str, _class: str) -> None:
        for i in self.table[int(_grade) - 1]['classes'][_class]['students']:
            print(i)

    def load_file(self, file_name: str) -> None:
        with open('data', 'r') as f:
            self.table = json.load(f)

    def save_file(self, file_name: str) -> None:
        with open(file_name, 'w') as f:
            json.dump(self.table, f, skipkeys=True, ensure_ascii=False, indent=2)
