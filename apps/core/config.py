#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 20:21:58
@Author  :   yuqibing 
@Desc    :   
'''
import os

from pydantic_settings import BaseSettings

path = os.getcwd()

class Setting(BaseSettings):
    """
    config
    """
    # jwt
    JWT_SECRET: str
    JWT_ALGORITHM: str

    # pg
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    # password
    PASSWORD_SALT: str

    class Config:
        """
        config path
        """
        env_file = path + "/.env"





settings = Setting()
