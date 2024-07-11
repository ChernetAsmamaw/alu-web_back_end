#!/usr/bin/env python3
''' Python function that returns all students sorted by average score '''

import pymongo


def top_students(mongo_collection):
    ''' Return all students sorted by average score

    - Prototype: def top_students(mongo_collection):
    - mongo_collection will be the pymongo collection object
    - The top must be ordered
    - The average score must be part of each item returns with key = averageScore
    '''

    students = mongo_collection.find()
    students = [student for student in students]
    for student in students:
        scores = student.get('topics')
        average_score = sum([score.get('score') for score in scores]) / len(scores)
        student['averageScore'] = average_score
    students = sorted(students, key=lambda x: x['averageScore'], reverse=True)
    return students
