#!/usr/bin/env python
# -*- coding: utf-8 -*-


class School:
    def __init__(self, grades: int, classes: int) -> None:
        self.table = []
        for i in range(1, grades + 1):
            self.table.append({'type': 'grade', 'name': f'{i}', 'classes': {}})
            for j in range(1, classes + 1):
                self.table[i]['classes'][f'{i}0{j}'] = {'type': 'class', 'name': f'{i}0{j}', 'students': []}


    def add(self, _grade: int, _class: str, _name: str) -> None:
        self.table[_grade - 1]['classes'][_class]['students'].append(_name)


    def remove(self, _grade: int, _class: str, _name: str) -> None:
        del self.table[_grade - 1]['classes'][_class]['students'][self.table[_grade - 1]['classes'][_class]['student'].index(_name)]


    def list_(self, _grade: int, _class: str) -> None:
        print(self.table[_grade - 1]['classes'][_class]['students'])
