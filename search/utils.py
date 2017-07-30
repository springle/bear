""" utils.py

This file provides a set of utilities for managing the search app. Primarily,
these tools will be used to interact with the Berkeley APIs and populate /
maintain the database.
"""

import os
import json
import django
import requests

from search import constants
from search import models

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
        self.term = term
        self.berkeley_api = BerkeleyAPI(url, params, headers)

    def query(self):
        self.berkeley_api.query(self.process_batch)

    def process_batch(self, response):
        d = json.loads(response.text)
        q = QueryDict(d)
        classes = q.get("apiResponse/response/classes")
        for c in classes:
            self.generate_model_instance(QueryDict(c))
            display_name = c.get("displayName")
            component_code = c.get("primaryComponent/description")
        return len(classes) > 0

    def generate_model_instance(self, data):
        m = models.BerkeleyClass()
        m.display_name = data.get("displayName")
        m.term = self.term
        m.term_name = data.get("session/term/name")
        m.title = data.get("course/title")
        m.number = data.get("number")
        m.offering_number = data.get("offeringNumber")
        m.description = data.get("classDescription", default="n/a")
        m.subject_code = data.get("course/subjectArea/code")
        m.subject = data.get("course/subjectArea/description")
        m.enrolled_count = data.get("aggregateEnrollmentStatus/enrolledCount")
        m.waitlisted_count = data.get("aggregateEnrollmentStatus/waitlistedCount")
        m.min_enroll = data.get("aggregateEnrollmentStatus/minEnroll")
        m.max_enroll = data.get("aggregateEnrollmentStatus/maxEnroll")
        m.max_waitlist = data.get("aggregateEnrollmentStatus/maxWaitlist")
        m.enrollment_status_code = data.get("aggregateEnrollmentStatus/status/code")
        m.enrollment_status = data.get("aggregateEnrollmentStatus/status/description")
        m.component_code = data.get("primaryComponent/code")
        m.component = data.get("primaryComponent/description")
        try:
            m.save()
        except django.db.utils.IntegrityError:
            pass
        except ValueError as e:
            print(e)
