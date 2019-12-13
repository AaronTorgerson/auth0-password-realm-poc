import os
from auth0.v3.authentication import GetToken, Users

AUTH0_DOMAIN = os.environ['AUTH0_DOMAIN']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
HC_USER_USERNAME = os.environ['HC_USER_USERNAME']
HC_USER_PASSWORD = os.environ['HC_USER_PASSWORD']

def do_get_token():
    get_token = GetToken(AUTH0_DOMAIN)
    result = get_token.login(
            client_id=CLIENT_ID, 
            client_secret=CLIENT_SECRET, 
            username=HC_USER_USERNAME, 
            password=HC_USER_PASSWORD, 
            scope='openid email profile', 
            realm='healthcheck-users', 
            audience='')

    del result['id_token']  # we don't need this - just mucks up console output
    print("Token result: ", result)
    
    users = Users(AUTH0_DOMAIN)
    user_info = users.userinfo(result['access_token'])
    print("User info: ", user_info)


if __name__ == "__main__":
    do_get_token()


