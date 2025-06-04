#!/usr/bin/env python3
"""
This project module contains functions to encrypt passwords and
another to check if it is a valid password.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if hashed and unhashed pswds are same
    Returns bool
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

