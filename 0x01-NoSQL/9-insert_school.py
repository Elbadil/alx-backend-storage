#!/usr/bin/env python3
"""Defining a function insert_school"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    newDoc = mongo_collection.insert_one(kwargs)
    return newDoc.inserted_id
