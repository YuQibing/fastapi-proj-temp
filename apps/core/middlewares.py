#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/06 14:48:52
@Author  :   yuqibing 
@Desc    :   
'''
from uuid import uuid4

from fastapi import Request
from fastapi.responses import JSONResponse
from apps.core.logs import service_log

from apps.core.security import decode_jwt, oauth2_scheme


async def add_request_id_dispatch(request, call_next):
    """
    添加请求标识
    :param request: 请求
    :param call_next:
    :return:
    """
    request_uuid = str(uuid4())
    request['headers'].append((b'x-request-id', request_uuid.encode()))
    return await call_next(request)


async def auth_check(request: Request, call_next):
    """
    check auth
    """
    request_id = request.headers.get('x-request-id')
    service_log.info(
        '[%s]:method[%s], url[%s], base_url[%s], path_params[%s], query_params[%s],', 
        request_id, request.method, request.url, request.base_url,request.path_params, request.query_params
    )
    # token 校验
    token = oauth2_scheme(request=request)

    account_token = await decode_jwt(token=token)
    
    if not account_token:
        return 


    # 设置account_id
    setattr(request.state, "account_id", account_token.account_id)
    
    response = await call_next(request)
    return response

