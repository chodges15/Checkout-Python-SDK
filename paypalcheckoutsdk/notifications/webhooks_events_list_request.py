import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

# TODO - How to handle query parameters?
class WebhooksEventsListRequest:
    """
    Lists webhook event notifications. Use query parameters to filter the response.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks-events?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
