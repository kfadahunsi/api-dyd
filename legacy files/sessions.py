import requests

# Start a session to persist cookies
session = requests.Session()

# Step 1: Get CSRF token by visiting the login page
login_page_url = 'https://users.premierleague.com/accounts/login/'
headers = {
    'User-Agent': 'Mozilla/5.0',
}
response = session.get(login_page_url, headers=headers)

# Step 2: Extract CSRF token from cookies
csrf_token = session.cookies.get('csrftoken')

# Step 3: Prepare login credentials and headers
login_data = {
    'csrfmiddlewaretoken': csrf_token,
    'login': 'fyguy1@yahoo.co.uk',
    'password': 'Mjolnir2me!',
    'redirect_uri': 'https://draft.premierleague.com/',
}

login_headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': login_page_url,
    'Origin': 'https://users.premierleague.com',
}

# Step 4: Post login data
login_response = session.post(login_page_url, data=login_data, headers=login_headers)

# Step 5: Use the session to access protected endpoint
team_id = 224216  # Replace with your team ID
api_url = f'https://draft.premierleague.com/api/entry/{team_id}/my-team'
api_response = session.get(api_url)

print("this is the response: ",api_response.json())  # or api_response.text if debugging
