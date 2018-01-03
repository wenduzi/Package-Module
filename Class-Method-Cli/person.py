#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1+percent)

    def __str__(self):
        return ('<%s object => %s:%s,%s>'% (self.__class__.__name__, self.name, self.job, self.pay))


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent+bonus)


if __name__ == '__main__':
    wen = Manager('wenduzi', 18, 50000 )
    li = Person('lilei', 16, 30000, 'dev')
    han = Person('hanmeimei', 15, 10000, None)
    for obj in (wen, li, han):
        obj.giveraise(0.1)
        print obj
