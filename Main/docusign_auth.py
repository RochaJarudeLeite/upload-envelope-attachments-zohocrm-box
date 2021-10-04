import os


from docusign_esign import ApiException, ApiClient, EnvelopesApi
from docusign_esign.client import api_client
from docusign_esign.client.auth import oauth

ds_private_key = os.getenv('ds_private_key', 'Token Not found')
ds_client_id = os.getenv('ds_client_id', 'Token Not found')
ds_private_key = os.getenv('ds_private_key', 'Token Not found')

api_client = ApiClient()
api_client.host = "https://na3.docusign.net/restapi"

scopes = [
    "signature",
    "impersonation"
]

in_file = open("privateKey.txt", "rb")

private_key = in_file.read()
in_file.close()


def dsauth():
    # client = api_client.(
    #     client_id=DS_JWT[ds_client_id],
    #     user_id=DS_JWT['4081c3f7-6747-40d9-9b32-ecfad7b2c6e5'],
    #     oauth_host_name=DS_JWT['na3.docusign.net'],
    #     private_key_bytes=ds_private_key,
    #     expires_in=3600,
    #     scopes=['signature', 'impersonation']
    # )
    try:
        access_token: oauth.OAuthToken.access_token
        access_token = api_client.request_jwt_user_token(
            client_id=ds_client_id,
            user_id='4081c3f7-6747-40d9-9b32-ecfad7b2c6e5',
            oauth_host_name='account.docusign.com',
            private_key_bytes=private_key,
            expires_in=3600,
            scopes=scopes
        )

        api_client.set_default_header(header_name="Authorization", header_value=f'Bearer {access_token.access_token}')
        return api_client
    except ApiException as err:
        print(err)
