import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksEventSubscriptionsRequest:
    """
    Lists event subscriptions for a webhook, by ID.
    """
    def __init__(self, webhook_id):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks/{webhook_id}/event-types?".replace("{webhook_id}", quote(str(webhook_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    