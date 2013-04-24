import requests

class MailgunApi(object):
    def __init__(self, domain, api_key):
        self.domain = domain
        self.api_key = api_key

    def send_email(self, **kwargs):
        response = requests.post(self.endpoint, data=kwargs, auth=self.auth)
        response.raise_for_status()
        return response

    @property
    def endpoint(self):
        return 'https://api.mailgun.net/v2/{}/messages'.format(self.domain)

    @property
    def auth(self):
        return ('api', self.api_key)
