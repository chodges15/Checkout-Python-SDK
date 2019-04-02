from paypalcheckoutsdk.notifications.verify_webhook_signature_request import VerifyWebhookSignatureRequest

def verify_webhook_signature(
        client, transmission_id, transmission_time, webhook_id, webhook_event,
        cert_url, transmission_sig, auth_algo):
    request = VerifyWebhookSignatureRequest()
    request.request_body({
        "auth_algo": auth_algo,
        "cert_url": cert_url,
        "transmission_id": transmission_id,
        "transmission_sig": transmission_sig,
        "transmission_time": transmission_time,
        "webhook_id": webhook_id,
        "webhook_event": webhook_event
    })
    response = client.execute(request)

    return response.result.verification_status == 'SUCCESS'