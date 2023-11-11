#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/11 21:33:19
@Author  :   yuqibing 
@Desc    :   
'''
from sqlalchemy.orm import Session

from apps.models.user import User
from apps.schemas.login_schema import LoginEmailReq
from apps.core.security import gen_hashed_password, gen_jwt_token
from apps.core.config import settings


async def login_service(body: LoginEmailReq, db: Session, account_id: int):
    """
    处理login逻辑
    """
    # 检测用户是否存在
    account = User.get_user_by_email(db=db, email=body.email)
    if not account:
        return None
    # 校验密码hash
    password_hash = gen_hashed_password(password=body.password, password_salt=settings.PASSWORD_SALT)
    if password_hash != account.password:
        return "PASSWORD_ERROR"
    # 生成token
    token = gen_jwt_token(account_id=account_id)

    resp = {
        'accountId': account.id,
        'username': account.username,
        'email': account.email,
        'token': token,
    }
    return resp
