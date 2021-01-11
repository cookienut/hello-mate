#!/usr/bin/env python

from datetime import datetime
from collections import Counter, defaultdict
from py.models.objects.base import MongoBaseClass


class UserHistory(MongoBaseClass):

    fields = ['uuid', 'url', 'time']

    def __init__(self, uuid):
        self.uuid = uuid
        self.collection = 'browsing_history'
        self.records = getattr(self.db_client_obj, self.collection)

    def get_all(self, start=None, end=None):
        """ Get browsing history for a user from Mongo Atlas DB """
        query = defaultdict(dict)
        query['uuid'] = self.uuid
        if start:
            query['time']['$gte'] = start
        if end:
            query['time']['$lte'] = end

        history_set = self.records.find(query)
        return UserHistory._from_db_object_list(
            history_set,
            fields=UserHistory.fields
            )

    def generate_insights(self, user_db_obj, count=10, start_time=None, end_time=None):
        """ Generates insights from user browsing history """
        # Retrieve user browsing data
        user_info = user_db_obj.get()
        history_set = self.get_all(start_time, end_time)

        # Generate insights
        insights = dict()
        for field in ["uuid", "name", "email"]:
            insights[field] = user_info[field]

        # Response entities
        url_visits = dict()
        url_tags = defaultdict(set)
        insights["history"] = list()

        for each_surf in history_set:
            splits = each_surf["url"].split("/")
            tag, url = splits[0], splits[2]
            url_visits[url] = url_visits.get(url, 0) + 1
            url_tags[url].add(tag)

        # Find top n visited websites by the user
        top_insights = dict(Counter(url_visits).most_common(count))
        for url in sorted(top_insights, key=top_insights.get, reverse=True):
            insights["history"].append({
                "url": url,
                "tags": list(url_tags[url]),
                "visits": url_visits[url]
            })

        return insights
