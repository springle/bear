""" utils.py

This file provides a set of utilities for managing the search app. Primarily,
these tools will be used to interact with the Berkeley APIs and populate /
maintain the database.
"""

import os
import json
import requests

from search import constants

CLASSES_APP_ID = os.environ.get("CLASSES_APP_ID")
CLASSES_APP_KEY = os.environ.get("CLASSES_APP_KEY")

class QueryDict(dict):
    """
    Helper class for safe, nested queries.
    """
    def get(self, path, default=None):
        keys = path.split("/")
        val = None
        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)
            if not val:
                break
        return val

class BerkeleyAPI:
    def __init__(self, url, params, headers):
        self.url = url
        self.params = params
        self.headers = headers

    def query(self, process_batch=print):
        """
        process_batch...
            input: response from Berkeley API request
            output: boolean (whether or not to query for another page)
        """
        for subject in constants.SUBJECTS:
            should_continue = True
            self.params["page-number"] = 1
            while should_continue:
                self.params["subject-area-code"] = subject
                response = requests.get(self.url,
                                        params=self.params,
                                        headers=self.headers)
                if response:
                    should_continue = process_batch(response)
                    self.params["page-number"] += 1
                else:
                    should_continue = False
                    print("No response for query:\n url:{}\n params:{}\n headers:{}\n".format(self.url,
                                                                                            self.params,
                                                                                            self.headers))

class ClassesAPI:
    def __init__(self, term=2178):
        url = "https://apis.berkeley.edu/uat/sis/v1/classes"
        params = {
            "term-id": term,
            "page-size": 10
        }
        headers = {
            "app_id": CLASSES_APP_ID,
            "app_key": CLASSES_APP_KEY,
            "Accept": "application/json"
        }
        self.berkeley_api = BerkeleyAPI(url, params, headers)

    def query(self):
        self.berkeley_api.query(self.process_batch)

    def process_batch(self, response):
        d = json.loads(response.text)
        q = QueryDict(d)
        classes = q.get("apiResponse/response/classes")
        for c in classes:
            self.generate_model(QueryDict(c))
            display_name = c.get("displayName")
            component_code = c.get("primaryComponent/description")
        return len(classes) > 0

    def generate_model(self, data):
        
