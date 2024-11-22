# from gpt4all import GPT4All

# model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
# with model.chat_session():
#     print(model.generate("How can I run LLMs efficiently on my laptop", max_tokens=1024))

from datetime import datetime, timedelta


yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
print(yesterday.split('-')[-1])


yesterday_date = datetime.strptime(yesterday, "%Y-%m-%d").strftime("%d-%b-%Y")
print(yesterday_date)
print(yesterday)



import json
import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt import MultipartEncoder
import time

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
    "REPORTING_DATE": yesterday,
    "IS_ATTACHED": "N",
    "PSP_CUSTOMER_INFO": [
    {
      "ROW ID": "13101",
      "PSP ID": "0800033",
      "REPORTING DATE": yesterday_date,
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
    try:
        # Print the payload before sending for verification
        print("\nSending Payload:", json.dumps(payload, indent=2))
        
        # Try different multipart field names and formats
        multipart_data = MultipartEncoder(
            fields={
                # Try these different variations:
                # 'request': ('request.json', json.dumps(payload), 'application/json'),
                # 'data': ('payload.json', json.dumps(payload), 'application/json'),
                'json': ('payload.json', json.dumps(payload), 'application/json'),
                # 'file': ('payload.json', json.dumps(payload), 'application/json'),
            },
            boundary='----WebKitFormBoundary7MA4YWxkTrZu0gW'
        )

        # Add more specific headers
        headers = {
            'Content-Type': multipart_data.content_type,
            'MIME-Version': '1.0',
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip,deflate',
            'User-Agent': 'Apache-HttpClient/4.5.5 (Java/16.0.2)'
        }

        response = requests.post(  
            api_url,
            headers=headers,
            data=multipart_data
        )

        print("\nInitial Response:")
        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Text:", response.text)

        if response.status_code == 200:
            try:
                response_json = response.json()
                print("\nResponse JSON:", json.dumps(response_json, indent=2))
                
                event_id = response_json.get('_event_transid')
                if event_id:
                    print(f"\nGot event ID: {event_id}")
                    
                    # Increase wait time significantly
                    wait_time = 30  # increased to 30 seconds
                    print(f"Waiting {wait_time} seconds for processing...")
                    time.sleep(wait_time)
                    
                    callback_url = 'https://gdi.centralbank.go.ke/test/api/v1/flows/rest/COMMON_GET_REQUESTS_STATUS/1.0/getRequestsStatus'
                    callback_payload = {
                        "INSTITUTION_CODE": payload["INSTITUTION_CODE"],
                        "REPORTING_DATE": payload["REPORTING_DATE"],
                        # "REQUEST_ID": str(event_id)  # Add the event_id as REQUEST_ID
                    }
                    
                    print("\nSending callback request...")
                    print("Callback URL:", callback_url)
                    print("Callback payload:", json.dumps(callback_payload, indent=2))
                    
                    callback_headers = {
                        'Authorization': f'Bearer {access_token}',
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    }
                    
                    # Try multiple callback attempts
                    max_attempts = 3
                    for attempt in range(max_attempts):
                        print(f"\nCallback attempt {attempt + 1} of {max_attempts}")
                        
                        callback_response = requests.post(
                            callback_url,
                            json=callback_payload,
                            headers=callback_headers
                        )
                        
                        print(f"Callback Response Status: {callback_response.status_code}")
                        print(f"Callback Content: {callback_response.text}")
                        
                        try:
                            callback_json = callback_response.json()
                            print("Parsed Callback Response:", json.dumps(callback_json, indent=2))
                            
                            if callback_json.get("COUNT", 0) > 0:
                                print("Successfully found records!")
                                break
                            else:
                                print("No records found yet...")
                                if attempt < max_attempts - 1:
                                    wait_time = 15  # Wait between attempts
                                    print(f"Waiting {wait_time} seconds before next attempt...")
                                    time.sleep(wait_time)
                        except json.JSONDecodeError:
                            print("Could not parse callback response as JSON")
                
                else:
                    print("No event_id found in response")
                    print("Full response content:", response.text)
            
            except json.JSONDecodeError as e:
                print(f"\nError decoding JSON response: {str(e)}")
                print("Raw response:", response.text)
        else:
            print(f"\nFailed request: {response.status_code}")
            print("Response content:", response.text)
        
        return response

    except Exception as e:
        print(f"\nError during data posting: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    # Step 1: Get the access token
    token = get_access_token()
    if token:
        print("\nAccess token obtained successfully")
        # Step 2: Post data
        response = post_data(token)
        if response:
            print("\nData posting completed")
        else:
            print("\nData posting failed")