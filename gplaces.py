import requests
# get all associated names from a given phone number using GPlaces API
def filter(api_key, phonenumber):
    place_ids = place_ids_from_phone_number(api_key, phonenumber)
    return [name_from_place_id(api_key, place_id) for place_id in place_ids]

# API Call 1: find place from text
def place_ids_from_phone_number(api_key, phonenumber):
    # get call
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=%2B{phonenumber}&inputtype=phonenumber&key={api_key}"
    response = requests.get(url)
    response_json = response.json()

    # error handling
    status = response_json.get("status")
    if status != "OK" and status != "ZERO_RESULTS":
        error_message = response_json.get("error_message")
        raise PermissionError(f"Request failed with status: {response_json.get('status')}, Error message: {error_message}")
    
    # store and return place_ids
    place_ids = []
    if 'candidates' in response_json:
        for candidate in response_json['candidates']:
            place_id = candidate.get('place_id')
            if place_id: place_ids.append(place_id)
    return place_ids

# API Call 2: place details
def name_from_place_id(api_key, place_id):
    # get call
    url = f"https://maps.googleapis.com/maps/api/place/details/json?fields=name&place_id={place_id}&key={api_key}"
    response = requests.get(url)
    response_json = response.json()
    
    # error handling
    status = response_json.get("status")
    if status != "OK" and status != "ZERO_RESULTS":
        error_message = response_json.get("error_message")
        raise PermissionError(f"Request failed with status: {response_json.get('status')}, Error message: {error_message}")
    
    return response_json.get('result').get('name') 