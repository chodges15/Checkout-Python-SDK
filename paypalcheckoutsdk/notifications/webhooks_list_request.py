import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksListRequest:
    """
    Lists all webhooks for an app.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks/"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
