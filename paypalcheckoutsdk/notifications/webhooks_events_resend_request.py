import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksEventsResendRequest:
    """
    Resends a webhook event notification, by ID. Any pending notifications are not resent.
    """
    def __init__(self, event_id):
        self.verb = "POST"
        self.path = "/v1/notifications/webhooks-events/{event_id}/resend?".replace("{event_id}", quote(str(event_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None
    
    def request_body(self, webhooks):
        self.body = webhooks
        return self