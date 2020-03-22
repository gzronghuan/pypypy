#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class Book:

    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state


# 创建一个Book类的子类 FictionBook

class FictionBook(Book):
    def __init__(self, name, author, comment, state=0, type='虚构类'):
        Book.__init__(self, name, author, comment, state=0)
        self.type = type

    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '类型：%s 名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.type, self.name, self.author, self.comment, status)


book = FictionBook('囚鸟', '冯内古特', '我们都是受困于时代的囚鸟')
print(book)