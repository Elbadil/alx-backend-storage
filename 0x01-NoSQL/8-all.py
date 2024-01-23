#!/usr/bin/env python3
"""Defining a function list_all"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    all_docs = []
    for doc in mongo_collection.find():
        all_docs.append(doc)

    return all_docs
