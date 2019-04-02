import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class VerifyWebhookSignatureRequest:
    """
    Verifies a webhook signature.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/notifications/verify-webhook-signature?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def request_body(self, webhook_signature):
        self.body = webhook_signature
        return self
