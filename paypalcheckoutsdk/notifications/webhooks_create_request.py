import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksCreateRequest:
    """
    Subscribes your webhook listener to events.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/notifications/webhooks"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def request_body(self, listener):
        self.body = listener
        return self
