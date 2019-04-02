import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksEventsGetRequest:
    """
    Shows details for a webhook event notification, by ID.
    """
    def __init__(self, event_id):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks-events/{event_id}?".replace("{event_id}", quote(str(event_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
