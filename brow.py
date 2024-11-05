from gpt4all import GPT4All

# model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
# with model.chat_session():
#     print(model.generate("How can I run LLMs efficiently on my laptop", max_tokens=1024))

from datetime import datetime, timedelta


yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
print(yesterday.split('-')[-1])


yesterday_date = datetime.strptime(yesterday, "%Y-%m-%d").strftime("%d-%b-%Y")
print(yesterday_date)



import json
import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt import MultipartEncoder

# Your API credentials
client_id = 'c26130bf85354b859d66152b3608c501'
client_secret = 'f4942c50-bff2-46d0-9ebf-0ec1d0ed3a44'
access_token_url = 'https://gdi.centralbank.go.ke/oauth2/v1/token'  # Replace with actual token URL
scope = 'https://8C80E3C8CFCF45EBB272C5478F767122.ke1.s7071808.oraclecloudatcustomer.com:443urn:opc:resource:consumer::all'


# # Requesting the access token
# response = requests.post(
#     access_token_url,
#     data={
#         'grant_type': 'client_credentials',
#         'scope': scope
#     },
#     auth=HTTPBasicAuth(client_id, client_secret)
# )

# # Check if the request was successful
# if response.status_code == 200:
#     access_token = response.json().get('access_token')
#     print('Access token:', access_token)
# else:
#     print(f"Failed to obtain access token: {response.status_code}")

api_url = 'https://gdi.centralbank.go.ke/test/api/v1/flows/rest/API_PSPCUSTOMERINFOSYNC/1.0/PSPs_Customer_Info'  # Replace with the actual API endpoint

# Data you want to send (JSON)
payload = {
    "INSTITUTION_CODE": "0800009",
    "REQUEST_ID": "",
    "REPORTING_DATE": "2024-10-15",
    "IS_ATTACHED": "N",
    "PSP_CUSTOMER_INFO": [
    {
      "ROW ID": "13101",
      "PSP ID": "0800033",
      "REPORTING DATE": "16-Oct-2024",
      "SUB COUNTY CODE": "1402",
      "GENDER": "O",
      "AGE CODE": "19",
      "WALLET CODE": "W02",
      "NO OF CUSTOMERS REGISTERED": "550",
      "NO OF CUSTOMERS ACTIVE": "41",
      "NO OF CUSTOMERS INACTIVE": "1111",
      "NO OF CUSTOMERS DORMANT": "2996",
      "BALANCES IN CUSTOMER ACCTS": "1072518671.03",
      "VOLUME OF TRANSACTIONS": "9660",
      "VALUE OF TRANSACTIONS": "9237038956.48"
    }
    ]
}


def get_access_token():
    """
    Function to request and retrieve an OAuth 2.0 access token.
    """
    try:
        response = requests.post(
            access_token_url,
            data={
                'grant_type': 'client_credentials',
                'scope': scope
            },
            auth=HTTPBasicAuth(client_id, client_secret)
        )

        if response.status_code == 200:
            access_token = response.json().get('access_token')
            print("Access token obtained successfully.")
            return access_token
        else:
            print(f"Failed to obtain access token: {response.status_code}, {response.text}")
            return None

    except Exception as e:
        print(f"Error during token retrieval: {str(e)}")
        return None

def post_data(access_token):
    multipart_data = MultipartEncoder(
            fields={
                'json': ('payload', json.dumps(payload), 'application/json')
            }
        )
    try:
        # Make the POST request (or PUT/PATCH if you already changed it)
        response = requests.post(  
            api_url,
            headers={
                'Content-Type': multipart_data.content_type,
                'MIME-Version': '1.0',
                'Authorization': f'Bearer {access_token}',
                'Accept-Encoding': 'gzip,deflate',
                'User-Agent': 'Apache-HttpClient/4.5.5 (Java/16.0.2)'
            },
            data=multipart_data
        )
        print("Response Headers:", response.headers)
        # Print status code to see if there's a server error
        print(f"Status Code: {response.status_code}")

        # Print raw response text to see what the server is sending back
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            try:
                response_json = response.json()
                print("Response JSON:", response_json)
                # Check for success messages in the response
                if "success" in response_json:
                    print("Success Message:", response_json["success"])
                elif "data" in response_json:
                    print("Data:", response_json["data"])
            except json.JSONDecodeError:
                print("Failed to decode JSON from response.")
        else:
            print(f"Failed request: {response.status_code}")

        # Only try to parse as JSON if the content type is JSON
        if 'application/json' in response.headers.get('Content-Type', ''):
            try:
                # Try parsing the response JSON if the content type is JSON
                response_json = response.json()
                print("Response JSON:", response_json)
            except ValueError as e:
                print(f"Failed to parse JSON: {str(e)}")
        else:
            print("Response is not JSON format.")
    
    except Exception as e:
        print(f"Error during data posting: {str(e)}")

if __name__ == "__main__":
    # Step 1: Get the access token
    token = get_access_token()

    # Step 2: Post data if the token was successfully retrieved
    if token:
        post_data(token)
