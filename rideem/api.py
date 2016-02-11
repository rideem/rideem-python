import requests
import json

RIDEEM_HOST = 'https://rideem.io'

def API(key = None, host = RIDEEM_HOST):
    return Rideem(key, host)

class Rideem(object):
    def __init__(self, key = None, host = RIDEEM_HOST):
        self._key = key # app private key
        self._host = host

    def create_app(self, name, email = None):
        """ Creates an app with name and email.
        """
        params = { 'email' : email } if email else {}
        return self._op('apps', name, method = 'post', data = params)

    def update_app(self, app):
        """ Updates an app.
        """
        params = {}
        self._add_key_param(params, app)
        return self._op('apps', app, method = 'post', data = app,
               params = params)

    def delete_app(self, app):
        """ Deletes an app.
        """
        params = {}
        self._add_key_param(params, app)
        return self._op('apps', app, method = 'delete', params = params)

    def get_app(self, name):
        """ Gets an app by name.
        """
        params = {}
        self._add_key_param(params)
        return self._op('apps', name, params = params)

    def create_promo_for(self, app, name = None, codes = None, delay = 60,
                         private = False, start = None, end = None):
        """ Creates a promo for the app.
        """
        params = {}
        self._add_key_param(params, app)
        promo = {
            'name' : name,
            'code' : codes if codes else [],
            'delay' : delay,
            'private' : private,
            'start' : start,
            'end' : end,
        }
        return self._op('promos', app, method = 'post', data = promo,
                        params = params)

    def update_promo_for(self, app, promo):
        """ Updates a promo.
        """
        params = {}
        self._add_key_param(params, app)
        p = promo.copy()
        p['code'] = p['codes']
        del p['key']
        del p['codes']
        return self._op('promos', app, method = 'post', data = p,
                        params = params)

    def delete_promo_from(self, app, promo):
        """ Deletes promo for the app.
        """
        params = {}
        self._add_key_param(params, app)
        name = promo['name']
        if name:
            params.update({'name' : name})
        return self._op('promos', app, method = 'delete', params = params)

    def get_promo_from(self, app, name = ''):
        """ Gets promo named name for an app.
        """
        params = {}
        self._add_key_param(params, app)
        if name:
            params.update({'name' : name})
        return self._op('promos', app, params = params)

    def code_from(self, app, promo = None, key = None):
        """ Redeems a code from an app for promo using key.

            Note: app and promo can be strings or dicts.
        """
        params = {}
        suffix = None

        if type(app) is str:
            self._add_key_param(params)
        else:
            self._add_key_param(params, app)

        promo_name = None
        if type(promo) is str:
            promo_name = promo
        elif promo:
            promo_name = promo['name']

        if key:
            params.update({'key' : key})

        if promo_name:
            suffix = '/for/{}'.format(promo_name)

        return self._op('from', app, suffix = suffix, params = params)

    def request(self, app, get = False):
        """ Request codes for an app.

            Note: app can be a string or dict.
        """
        method = 'post' if not get else 'get'
        return self._op('request', app, method = method)

    def verify(self, app, token):
        """ Verifies an app using token.
        """
        params = { 'token' : token } if token else {}
        return self._op('verify', app, params = params)

    def _op(self, endpoint, app, params = None, method = 'get',
            data = None, suffix = None):
        app_name = app if type(app) is str else app['name']
        suffix = suffix if suffix else ''
        endpoint = '/rideem/{}/{}{}'.format(endpoint, app_name, suffix)
        if method == 'post':
            r = self._post(endpoint, data, params = params)
        else:
            r = self._request(method, endpoint, params = params)
        return r

    def _request(self, method, ep, **kwargs):
        url = self._host + ep
        requester = getattr(requests, method)
        response = requester(url, **kwargs)
        r = response.json() if len(response.text) > 0 else {}
        return r, response.status_code

    def _post(self, url, o, params):
        data = json.dumps(o)
        headers = {'Content-type': 'application/json'}
        return self._request('post', url, data = data, headers = headers,
                             params = params)

    def _add_key_param(self, params, o = None):
        key = None
        key = o['key'] if o and 'key' in o else None
        if not key: key = self._key

        if key:
            params.update({ 'key' : key })

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, k):
        self._key = k

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, h):
        self._host = h

