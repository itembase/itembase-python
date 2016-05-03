import requests

from itembase.version import VERSION


class ItembaseError(Exception):
    pass


class AuthenticationError(ItembaseError):
    pass


class ItembaseAPI(object):
    _requests_session = None
    HOST_SANDBOX = "sandbox.api.itembase.io"
    HOST = "api.itembase.io"

    def __init__(self, access_token, user=None, sandbox=True):
        self.access_token = access_token
        self.sandbox = sandbox
        self.user = user

    @property
    def host(self):
        return self.HOST_SANDBOX if self.sandbox else self.HOST

    @property
    def session(self):
        if not self._requests_session:
            self._requests_session = requests.Session()
        return self._requests_session

    def do_request(self, url, method="GET", params=[], data=[], *args, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token),
                   'User-Agent': 'itembase/v1 PythonBindings/{0}'.format(VERSION)}
        self.response = self.session.request(method, url, params, data, headers, **kwargs)
        if not (200 <= self.response.status_code < 300):
            self.handle_api_error()
        return self.response.json()

    def handle_api_error(self):
        if self.response.status_code == 401:
            raise AuthenticationError(self.response.text)
        raise ItembaseError(self.response.text)

    def do_user_list(self, list_name, user=None, *args, **kwargs):
        user = user if user else self.user
        return self.do_request("https://{0}/v1/users/{1}/{2}".format(self.host, user, list_name), params=kwargs)

    def do_user_single(self, list_name, entity_id, user=None, *args, **kwargs):
        user = user if user else self.user
        return self.do_request("https://{0}/v1/users/{1}/{2}/{3}".format(self.host, user, list_name, entity_id), params=kwargs)

    def profiles(self, user=None, *args, **kwargs):
        return self.do_user_list("profiles", user, *args, **kwargs)

    def transaction(self, entity_id, user=None, *args, **kwargs):
        return self.do_user_single("transaction", entity_id, user, *args, **kwargs)

    def transactions(self, user=None, *args, **kwargs):
        return self.do_user_list("transactions", user, *args, **kwargs)

    def product(self, entity_id, user=None, *args, **kwargs):
        return self.do_user_single("products", entity_id, user, *args, **kwargs)

    def products(self, user=None, *args, **kwargs):
        return self.do_user_list("products", user, *args, **kwargs)

    def buyer(self, entity_id, user=None, *args, **kwargs):
        return self.do_user_single("buyers", entity_id, user, *args, **kwargs)

    def buyers(self, user=None, *args, **kwargs):
        return self.do_user_list("buyers", user, *args, **kwargs)

    def request_pretty(self):
        req = self.response.request
        return '{}\n{}\n\n{}'.format(
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            req.body or "",
        )
