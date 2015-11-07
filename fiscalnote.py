import requests

from pprint import pprint


class FiscalNoteClient(object):
    _BASE_URL = 'https://api.fiscalnote.com'
    _API_PARAMS = (
        'q',
        'legislature',
        'chamber',
        'party',
    )

    def __init__(self, api_key):
        self._api_key = api_key

    def legislators(self, **kwargs):
        query = '{}/legislators?'.format(self._BASE_URL)
        query_args = ['apikey={}'.format(self._api_key)]
        for param in self._API_PARAMS:
            if param in kwargs:
                query_args.append('{}={}'.format(param, kwargs[param]))
        query += '&'.join(query_args)
        # print(query)
        return requests.get(query).json()
    
    def getPersonFromID(self, mem_id):
        query = '{}/legislators?'.format(self._BASE_URL)
        query_args = ['apikey={}'.format(self._api_key)]
        query_args.append('{}={}'.format("id", mem_id))
        query += '&'.join(query_args)
        ll = requests.get(query).json()
        return ll

    def getFriends(self, mem_id):
        query = '{}/legislators?'.format(self._BASE_URL)
        query_args = ['apikey={}'.format(self._api_key)]
        query_args.append('{}={}'.format("id", mem_id))
        query += '&'.join(query_args)
        #print(query)
        flist = [i['friends'] for i in requests.get(query).json() if i is not None and i["friends"] is not None]
        retlist = [(i["legislator_id"], i["voting_similarity_score"]) for i in flist[0]["overall"]]
        return retlist

    def bill(self, **kwargs):
        query = '{}/bill?'.format(self._BASE_URL)
        query_args = ['apikey={}'.format(self._api_key)]
        for param in self._API_PARAMS:
            if param in kwargs:
                query_args.append('{}={}'.format(param, kwargs[param]))
        query += '&'.join(query_args)
        # print(query)
        return requests.get(query).json()
