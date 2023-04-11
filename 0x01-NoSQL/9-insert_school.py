#!/usr/bin/env python
"""
Function that inserts a new doc in a collection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """ Return id. """
    return mongo_collection.insert_one(kwargs).inserted_id
