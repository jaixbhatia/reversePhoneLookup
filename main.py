import json
import gplaces, yelp_fusion, consts

def reverse_phone_lookup(yelp_fusion_api_key, gplaces_api_key, country_code, phone_number): 
    """
    1) Format phone number (formatted_phone_number should have the form 1650380386)
    2) Check cache
    3) Call each function of the pipeline (with error checking)
    4) Cache results
    5) Return list of business names associated with the formatted_phone_number
    """
    # 1)
    phone_number_formatted = str(country_code) + str(phone_number)
    # 2)
    try:
        with open('cache.json', 'r') as file:
            cache_json = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        cache_json = {}
    if phone_number_formatted in cache_json:
        return cache_json[phone_number_formatted]
    # 3)
    try:
        names = gplaces.filter(gplaces_api_key, phone_number_formatted)
        if not names: # if nothing found from gplaces API, run yelp fusion API
            names = yelp_fusion.filter(yelp_fusion_api_key, phone_number_formatted)
    except PermissionError as e:
        print(f"Permission error occurred: {e}")
        names = []
    # 4)
    consts.cache(names, phone_number_formatted)
    # 5)
    return names

# test
user_inputted_country_code = input("Enter country code (ex. 1): ")
user_inputted_number = input("Enter phone # (ex. 6503860386): ")
lookup = reverse_phone_lookup(consts.FUSION_API_KEY, consts.GPLACES_API_KEY, user_inputted_country_code, user_inputted_number)
print('*' * 50, '\n')
print("Results: " + str(lookup))
print("Temp Cache: ", str(consts.temp_cache))
