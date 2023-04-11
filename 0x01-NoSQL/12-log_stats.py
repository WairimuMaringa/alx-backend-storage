#!/usr/bin/env python3
"""
Script that gives stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collectionn = client.logs.nginx
    print("{} logs".format(collectionn.estimated_document_count()))
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collectionn.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))
    getstat = collectionn.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(getstat))
