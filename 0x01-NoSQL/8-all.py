#!/usr/bin/env python3
"""
Function that lists all docs in a collection
"""


def list_all(mongo_collection):
    """ Return documents or empty list. """
    return [doc for doc in mongo_collection.find()]
