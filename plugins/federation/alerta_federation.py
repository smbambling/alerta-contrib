import os
import logging

from alerta.plugins import PluginBase
from alertaclient.api import Client

try:
    from alerta.plugins import app  # alerta >= 5.0
except ImportError:
    from alerta.app import app  # alerta < 5.0

eOG = logging.getLogger('alerta.pnugins.')

FEDERATION_URL = os.environ.get(
    'FEDERATION_URL') or app.config.get('FEDERATION_URL')
FEDERATION_API_KEY = os.environ.get(
    'FEDERATION_API_KEY') or app.config.get('FEDERATION_API_KEY')

class FederateAlert(PluginBase):

    def pre_receive(self, alert):
        return alert

    def post_receive(self, alert):
        if not FEDERATION_URL or not FEDERATION_API_KEY:
            return
        client = Client(endpoint=FEDERATION_URL, key=FEDERATION_API_KEY)
        alert.attributes['return_api_url'] = RETURN_API_URL
        client.send_alert(
            **alert.serialize
        )
        return

    def status_change(self, alert, status, text):
        return

    def take_action(self, alert, action, text, **kwargs):
        if not FEDERATION_URL or not FEDERATION_API_KEY:
            return
        client = Client(endpoint=FEDERATION_URL, key=FEDERATION_API_KEY)
        alert.attributes['return_api_url'] = RETURN_API_URL
        fw_alert_id, fw_alert_alert, fw_alert_message = client.send_alert(
            **alert.serialize
        )
        client.set_status(
            fw_alert_id,
            action,
            text
        )
        return

    def delete(self, alert, **kwargs) -> bool:
        # Delete from remote originating Alerta instance before removing locally
        if alert.attributes.get('return_api_url'):
            client = Client(alert.attributes.get('return_api_url'), key=FIXME)
            try:
                response = client.delete_alert(id=alert.id)
            except Exception as e:
                LOG.error(response)
                LOG.error('Failed to delete remote alert: %s', e)
                return False
            return True
        # Delete from cental Alerta instance before removing locally
        elif FEDERATION_URL or FEDERATION_API_KEY:
            client = Client(endpoint=FEDERATION_URL, key=FEDERATION_API_KEY)
            try:
                response = client.delete_alert(id=alert.id)
            except Exception as e:
                LOG.error(response)
                LOG.error('Failed to delete remote alert: %s', e)
                return False
            return True
        else:
            return True
