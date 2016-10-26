#!/usr/bin/env python3

import requests, json

#
# This scripts tests the creation of a PTM resource.
#

try:
    base_url = "http://localhost/v1/"

    params = {
        "restype_id": "http://www.knora.org/ontology/RTIproject#PTM",
        "label": "A PTM resource",
        "project_id": "http://data.knora.org/projects/RTIproject",
        "properties": {
            "http://www.knora.org/ontology/RTIproject#hasPTMCreator": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"Dr. Ptm Creator"}}],
            "http://www.knora.org/ontology/RTIproject#hasPTMlocation": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"Bernoullistrasse 32, 4051 Basel"}}],
            "http://www.knora.org/ontology/RTIproject#hasPTMdate": [{'date_value': 'GREGORIAN:' + "2016-06-01"}],
            "http://www.knora.org/ontology/RTIproject#hasPTMexib": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"Bernoullianum, University of Basel"}}],
            "http://www.knora.org/ontology/RTIproject#setupIs": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"This should be more precise, perhaps make a list?"}}],
            "http://www.knora.org/ontology/RTIproject#hasPermissions": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"Need special licence from University"}}],
            "http://www.knora.org/ontology/RTIproject#hasPTMcomment": [ {"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"This is a test resource creation, for a PTM object"}},
                                                                         {"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"And here is a second comment, just to test cardinality"}}]
        }
    }

    props = json.dumps(params)

    r = requests.post(base_url + 'resources',
                      data=props,
                      headers={'content-type': 'application/json; charset=utf8'},
                      auth=('root', 'test'),
                      proxies={'http': 'http://localhost:3333'})

    r.raise_for_status()
    print(r.text)
except Exception as e:
    print('Knora API answered with an error:\n')
    print(e)
    print(r.text)