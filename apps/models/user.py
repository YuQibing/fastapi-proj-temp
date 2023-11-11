#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 20:10:49
@Author  :   yuqibing 
@Desc    :   
'''
from sqlalchemy import Column, String
from sqlalchemy.orm import Session

from apps.db.base_class import Base


class User(Base):
    """
    user
    """
    __tablename__ = "user"

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    password = Column(String, nullable=False)

    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        """根据email获取用户"""
        user = db.query(cls).filter(cls.email==email).first()
        if user:
            return user
        return None