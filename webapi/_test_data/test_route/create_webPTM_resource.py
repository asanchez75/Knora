#!/usr/bin/env python3

import requests, json

#
# This script tests the creation of a webPTM resource.
#


try:
    base_url = "http://localhost/v1/"

    params = {
        "restype_id": "http://www.knora.org/ontology/webPTM#webPTMdata",
        "label": "A web PTM data resource with image files",
        "project_id": "http://data.knora.org/projects/RTIproject",
        "properties": {
            "http://www.knora.org/ontology/webPTM#haswebPTMtype": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"LRGBG_PTM"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTM_w_contentSize": [{"int_value":3058}],
            "http://www.knora.org/ontology/webPTM#haswebPTM_h_contentSize": [{"int_value":4368}],
            "http://www.knora.org/ontology/webPTM#haswebPTMscale": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"[2.154948, 1.793018, 2.294132, 1.283200, 1.171154, 1.105553, 4.848146, 1, 1]"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMbias": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"[165, 179, 135, 131, 130, 3, -1, 0, 0]"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMorientation": [{"int_value":3}],
            "http://www.knora.org/ontology/webPTM#haswebPTMimageFormat": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"jpg"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTM_w_maxRes": [{"int_value":8192}],
            "http://www.knora.org/ontology/webPTM#haswebPTM_h_maxRes": [{"int_value":8192}],
            "http://www.knora.org/ontology/webPTM#haswebPTMgeometry": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"PLANE"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMmultiresType": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"IIIF"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTM_w_tileSz": [{"int_value":256}],
            "http://www.knora.org/ontology/webPTM#haswebPTM_h_tileSz": [{"int_value":256}],
            "http://www.knora.org/ontology/webPTM#haswebPTMfShaderURL": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"lib/shaders/LRGBG_PTM_FShader.glsl"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMvShaderURL": [ {"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"lib/shaders/LRGBG_PTM_VShader.glsl"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMutilsShaderURL": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"lib/shaders/PTM_shaderUtils.glsl"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMsupportedGeometries": [ {"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"PLANE"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMmodelDescript": [ {"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"rti phong (plane)"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMdescript": [{"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"webPTM data description"}}],
            "http://www.knora.org/ontology/webPTM#haswebPTMcomment": [ {"richtext_value":{"textattr":"{}","resource_reference" :[],"utf8str":"webPTM data comment"}}]
        }
    }

    filename = '1_1s.tif'
    path = 'images/'
    mimetype = 'image/tiff'


    files = {'file': (filename, open(path + filename, 'rb'), mimetype)}


    props = json.dumps(params)


    r = requests.post(base_url + 'resources',
                      files=files,
                      data={'json': props},
                      headers=None,
                      auth=('root', 'test'),
                      proxies={'http': 'http://localhost:3333'})


#    r = requests.post(base_url + 'resources',
#                      data=props,
#                      files=files,
#                      auth=('root', 'test'),
#                      proxies={'http': 'http://localhost:3333'})

    r.status_code
    r.raise_for_status()

    print(base_url + 'resources')
    print(r.text)
except Exception as e:
    print('Knora API answered with an error:\n')
    print(e)
    print(r.text)