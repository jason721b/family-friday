#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import DocType, Keyword
from elasticsearch.helpers import scan


# TODO: Hardcoded Elasticsearch client connecting to localhost instance
es = Elasticsearch()


class Member(DocType):

    class Meta:
        index = 'member'
        doc_type = 'docs'
        using = es

    first_name = Keyword()
    last_name = Keyword()

    @classmethod
    def all(cls):
        """

        Returns
        -------
        iterator<Member>

        """

        # NOTE: `scan` is usually not suitable for customer-facing web app
        #   However, as this web app is for internal use and there are less than one thousand records
        #   it should be OK to use
        for member in scan(es, index='member', size=10):
            yield Member(**member['_source'])

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

