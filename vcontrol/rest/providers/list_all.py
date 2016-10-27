from ..helpers import get_allowed

import os
import web

class ListProvidersR:
    """
    This endpoint lists all of the providers that have been added.
    """
    allow_origin, rest_url = get_allowed.get_allowed()

    def GET(self):
        """ GET HTTP Request """
        try:
            web.header('Access-Control-Allow-Origin', self.allow_origin)
        except Exception as e:
            print(e.message)
        try:
            providers = {}
            if os.path.isfile('providers.txt'):
                with open('providers.txt', 'r') as f:
                    for line in f:
                        providers[line.split(":")[0]] = line.split(":")[1].strip()
            return providers
        except:
            return "unable to get providers"
