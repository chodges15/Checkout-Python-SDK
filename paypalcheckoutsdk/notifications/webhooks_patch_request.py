import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhooksPatchRequest:
    """
    Replaces webhook fields with new values. Supports only the replace operation. Pass a json_patch object with replace operation and path, which is /url for a URL or /event_types for events. The value is either the URL or a list of events.
    """
    def __init__(self, webhook_id):
        self.verb = "PATCH"
        self.path = "/v1/notifications/webhooks/{webhook_id}?".replace("{webhook_id}", quote(str(webhook_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None


    def request_body(self, patch_request):
        self.body = patch_request
        return self