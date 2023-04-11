#!/usr/bin/env python3
"""
Function that returns list of school having specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """ Returns list. """
    return mongo_collection.find({'topics': topic})
