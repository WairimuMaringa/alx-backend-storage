#!/usr/bin/env python3
"""
Function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ Return sorted list."""
    return list(mongo_collection.find())
