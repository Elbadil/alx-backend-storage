#!/usr/bin/env python3
"""Defining a function top_students"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    av_score = 0
    student_scores = []
    for student in mongo_collection.find():
        for topic in student['topics']:
            student_scores.append(topic['score'])
        av_score = sum(student_scores) / len(student_scores)
        mongo_collection.update_one({
            "_id": student['_id']
            }, {
                '$set': {
                    'averageScore': av_score
                }
            })
        student_scores = []
        av_score = 0

    sorted_by_avscore = mongo_collection.find().sort("averageScore", -1)

    return sorted_by_avscore
