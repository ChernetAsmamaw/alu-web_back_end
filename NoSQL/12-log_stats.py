#!/usr/bin/env python3
''' Python script that provides some stats about Nginx logs stored in MongoDB '''

from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    ''' Log Nginx stats from collection '''
    item = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    total = mongo_collection.count_documents(item)
    print(f"{total} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)
    stat_check = mongo_collection.count_documents(
        {"path": {"$regex": "/status"}})
    print(f"{stat_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
