from random import choice

from app_users.models import User


def create_code():
    code = ''
    for x in range(4):
        code += choice(list('1234567890'))
    return code


def create_invite_code():
    invite_code = ''
    for x in range(6):
        invite_code += choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return invite_code
