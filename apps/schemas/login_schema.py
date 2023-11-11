#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/11 21:37:23
@Author  :   yuqibing 
@Desc    :   
'''
from pydantic import BaseModel, EmailStr

class LoginEmailReq(BaseModel):
    """
    邮箱登陆请求体
    """
    email: EmailStr
    password: str
