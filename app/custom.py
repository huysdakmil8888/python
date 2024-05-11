from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
import requests
import logging

logger = logging.getLogger(__name__)

class CustomFacebookOAuth2Adapter(FacebookOAuth2Adapter):
    def complete_login(self, request, app, token, **kwargs):
        print('complete login')
        # Custom method to send POST request
        def exchange_code_for_token(code):
            payload = {
                'client_id': app.client_id,
                'redirect_uri': self.get_callback_url(request, app),
                'client_secret': app.secret,
                'code': code,
            }
            response = requests.post('https://graph.facebook.com/v12.0/oauth/access_token', data=payload)
            logger.debug('Facebook response: %s', response.text)
            response.raise_for_status()
            return response.json()['access_token']

        try:
            access_token = exchange_code_for_token(request.GET['code'])
            token.token = access_token
        except requests.exceptions.HTTPError as e:
            raise OAuth2Error('Error exchanging code for token: %s' % str(e))

        return super().complete_login(request, app, token, **kwargs)