import requests, random, string
from requests_oauthlib import OAuth2Session

class GoogleOauth2Session:

    def __init__(self, client_id:str, secret_key:str, redirect_uri:str, scope:list=None):
        self.client_id = client_id
        self.secret_key = secret_key
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.oauth2 = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri, scope=self.scope)

    def get_auth_url(self):
        return self.oauth2.authorization_url('https://accounts.google.com/o/oauth2/auth')
    
    def get_token(self, code:str):
        return self.oauth2.fetch_token('https://accounts.google.com/o/oauth2/token',\
                                       code=code, client_secret=self.secret_key)
    def get_user_info(self):
        return self.oauth2.get('https://www.googleapis.com/oauth2/v2/userinfo').json()

gg_client_id = 'YOUR_GOOGLE_CLIENT_ID'
gg_secret_key = 'YOUR_GOOGLE_SECRET_KEY'
gg_redirect_uri = 'http://localhost:5000/users/auth/google/callback/' # Change this to your domain
gg_scopes=[
        "openid", 
        "https://www.googleapis.com/auth/userinfo.profile", 
        "https://www.googleapis.com/auth/userinfo.email"
    ]
google_oauth2 = GoogleOauth2Session(gg_client_id, gg_secret_key, gg_redirect_uri, gg_scopes)

class GithubOauth2:
    def __init__(self, client_id:str, secret_key:str, redirect_uri:str, scope:list=None):
        self.client_id = client_id
        self.secret_key = secret_key
        self.redirect_uri = redirect_uri
        self.scope = scope

    def get_auth_url(self):
        state = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        auth_url = f"https://github.com/login/oauth/authorize?client_id={self.client_id}&state={state}"
        return auth_url, state
    
    def get_token(self, code:str):
        try:
            headers = {
                'Accept': 'application/json'
            }
            token_url = f'https://github.com/login/oauth/access_token?client_id={self.client_id}&client_secret={self.secret_key}&code={code}'
            response = requests.post(token_url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            return None
    
    def get_user_info(self, token:str):
        try:
            headers = {
                'Accept': 'application/json',
                'Authorization': f'token {token}',
            }
            user_url = 'https://api.github.com/user'
            response = requests.get(user_url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            return None
    
gh_client_id = 'YOUR_GITHUB_CLIENT_ID'
gh_secret_key = 'YOUR_GITHUB_SECRET_KEY'
gh_redirect_uri = 'http://localhost:5000/users/auth/github/callback/' # Change this to your domain  
gh_scopes = None
github_oauth2 = GithubOauth2(gh_client_id, gh_secret_key, gh_redirect_uri, gh_scopes)

class LinkedinOauth2:
    def __init__(self, client_id:str, secret_key:str, redirect_uri:str, scope:list=None):
        self.client_id = client_id
        self.secret_key = secret_key
        self.redirect_uri = redirect_uri
        self.scope = ','.join(scope) if scope else None

    def get_auth_url(self):
        state = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        auth_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={self.client_id}&redirect_uri={self.redirect_uri}&state={state}&scope=openid,profile,email"
        return auth_url, state
    
    def get_token(self, code:str):
        try:
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            token_url = f'https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code={code}&redirect_uri={self.redirect_uri}&client_id={self.client_id}&client_secret={self.secret_key}'
            response = requests.post(token_url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            return None
    
    def get_user_info(self, token:str):
        try:
            headers = {
                'Authorization': f'Bearer {token}',
            }
            user_url = 'https://api.linkedin.com/v2/me' #https://api.linkedin.com/v2/userinfo
            response = requests.get(user_url, headers=headers)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            return None
        
lk_client_id = 'LINKEDIN_CLIENT_ID'
lk_secret_key = 'LINKEDIN_SECRET_KEY'
lk_redirect_uri = 'http://localhost:5000/users/auth/linkedin/callback/' # Change this to your domain
lk_scopes = ['openid','profile','email']
linkedin_oauth2 = LinkedinOauth2(lk_client_id, lk_secret_key, lk_redirect_uri, lk_scopes)