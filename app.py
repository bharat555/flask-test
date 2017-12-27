# -*- coding: utf-8 -*-

"""A basic (single function) API written using hug"""
import hug


@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())
