#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 21:49:40
@Author  :   yuqibing 
@Desc    :   
'''
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from apps.core.config import settings




SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db() -> Generator:
    """
    获取db session
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

