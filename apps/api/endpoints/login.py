#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 20:15:52
@Author  :   yuqibing 
@Desc    :   
'''

from fastapi import APIRouter, Request, Depends, Header

from apps.db.session import get_db
from apps.schemas.login_schema import LoginEmailReq
from apps.core.logs import service_log
from apps.service import login_service

login_router = APIRouter()

@login_router.post("/login")
async def login(
    request: Request, 
    body: LoginEmailReq, 
    db: Depends(get_db),
    request_id: Header(None)
    ):
    """
    login
    """
    print(request_id, body.email)
    account_id = request.state.account_id
    resp = await login_service.login_service(body=body, db=db, account_id=account_id)
    return resp