from .mailgun_api import MailgunApi

class Mailgun(object):
    mailgun_api = None

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.mailgun_api = MailgunApi(app.config['MAILGUN_DOMAIN'],
                app.config['MAILGUN_API_KEY'])

    def send_email(self, **kwargs):
        if not self.mailgun_api:
            raise ValueError('A valid app instance has not been provided')

        return self.mailgun_api.send_email(**kwargs)
