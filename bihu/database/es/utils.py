#!/usr/bin/env python
# -*-coding:utf-8-*-


from elasticsearch import Elasticsearch


def es_get(uri, index, id, doc_type='doc'):
    """
    get doc based on id
    """
    es = Elasticsearch(uri, timeout=30)
    res = es.get(index=index, doc_type=doc_type, id=id)

    return res


def es_search(uri, index, body):
    """
    get docs based on search
    """
    es = Elasticsearch(uri, timeout=30)

    res = es.search(index=index, body=body, request_cache="false")

    return res