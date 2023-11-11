#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/04 20:53:31
@Author  :   yuqibing 
@Desc    :   
'''
from typing import Any
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn

from apps.core.logs import service_log
from apps.db import session
from apps.core.middlewares import auth_check, add_request_id_dispatch


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]


def create_app() -> Any:
    """
    add middleware
    """
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    # 添加中间件，执行的顺序是添加中间件的相反顺执行
    app.add_middleware(BaseHTTPMiddleware, dispatch=auth_check)
    app.add_middleware(BaseHTTPMiddleware, dispatch=add_request_id_dispatch)
    
    
    return app


app = create_app()

@app.get("/health")
async def index():
    """
    check health
    """
    service_log.info('{"a": 1}')
    print(session.SQLALCHEMY_DATABASE_URL)
    return "ok"


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=5000)

