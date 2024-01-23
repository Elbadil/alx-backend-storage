#!/usr/bin/env python3
"""Defining a function schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """returns a list of school having a specific topic"""
    topic_school_list = []
    collection = mongo_collection.find()
    for doc in collection:
        if 'topics' in doc.keys():
            for tpc in doc['topics']:
                if tpc == topic:
                    topic_school_list.append(doc)

    return topic_school_list
