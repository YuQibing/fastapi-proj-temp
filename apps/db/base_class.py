#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    :   2023/11/05 20:08:22
@Author  :   yuqibing 
@Desc    :   
'''
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, Integer


@as_declarative()
class Base():
    """
    Base Class
    """
    id = Column(Integer, primary_key=True, index=True)
