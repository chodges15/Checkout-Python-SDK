import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksEventsTypesRequest:
    """
    Lists available events to which any webhook can subscribe. For a list of supported events, see Webhook event names.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks-event-types/"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
