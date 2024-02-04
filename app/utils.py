import requests


def search_location(location):
    url = "https://api.content.tripadvisor.com/api/v1/location/search"
    headers = {'accept': 'application/json'}
    params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91', 'searchQuery': location}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the response status code is 200 (OK) before returning the data.
        if response.status_code == 200:
            return response.json()  # Return the JSON response data
        else:
            return {'error': f'An error occurred: {response.status_code}'}
            
    except requests.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        return {'error': str(e)}
    


# Remember to replace 'YOUR_API_KEY' with your actual API key, and ensure
# that you do not expose your API key in your source code.


import requests

import requests

def show_images(location_id):
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/photos"
    headers = {'accept': 'application/json'}
    params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91'}  # Replace 'YOUR_API_KEY' with your actual API key
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        
        # Check if 'data' key is in the JSON response
        json_response = response.json()
        if 'data' in json_response:
            return json_response
        else:
            return {'error': 'No data key in response'}
    
    except requests.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        return {'error': str(e)}


def location_description(location_id):
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details"
    headers = {'accept': 'application/json'}
    params = {'key': '6A2A0969ED22430DB68AB70E1E89FE91'}
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            # Return the JSON response data
            return response.json()
        else:
            # Return an error message with the status code
            return {'error': f'An error occurred: {response.status_code}'}
    except requests.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        return {'error': str(e)}

