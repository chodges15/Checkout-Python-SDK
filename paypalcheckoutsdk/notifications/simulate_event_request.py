import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class SimulateEventRequest:
    """
    Simulates a webhook event. In the JSON request body, specify a sample payload.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/notifications/simulate-event?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def request_body(self, simulated_event):
        self.body = simulated_event
        return self
