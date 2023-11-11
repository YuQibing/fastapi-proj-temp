#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 20:00:10
@Author  :   yuqibing 
@Desc    :   
'''
from datetime import datetime, timedelta, timezone
import string
import hashlib
import base64
import random
from pydantic import BaseModel
import jwt


from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


from apps.core.config import settings

# jwt默认过期时间
DEFAULT_JWT_EXPIRE_TIMEDELTA = timedelta(days=7)

ALGORITHM = "HS256"
DEFAULT_DECODE = "UTF-8"



class AccountToken(BaseModel):
    """
    account
    """
    account_id: int


def gen_jwt_token(account_id: int, expires_delta: timedelta = None) -> str:
    """
    产生jwt token
    :param account_id: 用户id
    :param expires_delta: 过期时间
    :return:
    """
    expire = datetime.now(timezone.utc)
    expire += expires_delta if expires_delta else DEFAULT_JWT_EXPIRE_TIMEDELTA

    info = {"account_id": account_id, "exp": expire.timestamp()}
    return jwt.encode(
        info, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM
    )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def decode_jwt(token: str = Depends(oauth2_scheme)) -> AccountToken:
    """
    解析jwt_token
    :param token:
    :return:
    """
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        account_id = payload['account_id']

        if account_id is None or datetime.utcnow().timestamp() > payload['exp']:
            return None

        account_token = AccountToken(account_id=account_id)
        
    except Exception as e:
        print(e)
        return None

    return account_token


def gen_hashed_password(password: str, password_salt: str) -> str:
    """
    哈希密码
    :param password: 密码
    :param password_salt: 盐
    :return:
    """
    salted_sha1 = hashlib.sha1((password + password_salt).encode())
    hashed_base64 = base64.b64encode(salted_sha1.digest()).decode(DEFAULT_DECODE)
    return hashed_base64


def gen_random_string(length: int):
    """
    生成指定长度的随机字符串
    :param length: 长度
    :return:
    """
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


