#!/usr/bin/env python3
"""
Function tha changes all topics of a doc based on name
"""


def update_topics(mongo_collection, name, topics):
    """ Returns topics. """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}})
