#!usr/bin/env python3
''' Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs'''

from pymongo import MongoClient


METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
PIPE = [{'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}]


def log_stats(mongo_collection, option=None):
    ''' Return the top 10 of the most present IPs in the collection nginx of the database logs'''
    if option:
        value = mongo_collection.count_documents(
            {'method': {'$regex': option}})
        print(f"\tmethod {option}: {value}")
        return

    total = mongo_collection.count_documents({})
    print(f"{total} logs")
    print('Methods:')
    for method in METHODS:
        log_stats(mongo_collection, method)
    stat_check = mongo_collection.count_documents(
        {'path': {'$regex': '/status'}})
    print(f"{stat_check} status check")
    print('IPs:')

    for ip in mongo_collection.aggregate(PIPE):
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == '__main__':
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
