import requests
import gplaces, yelp_fusion, consts

def reverse_phone_lookup(yelp_fusion_api_key, gplaces_api_key, country_code, phone_number): 
    """
    1) Check cache
    2) Call each function of the pipeline. Cache when possible. Return business name
    3) If business already with us, add business name
    """
    phone_number_formatted = str(country_code) + str(phone_number)
    names =  gplaces.filter(gplaces_api_key, phone_number_formatted)
    if not names: # nothing found from gplaces API 
        names = yelp_fusion.filter(yelp_fusion_api_key, phone_number_formatted)

    # caching step
    if names:
        if phone_number_formatted in consts.cache:
            consts.cache[phone_number_formatted] += names
        else:
            consts.cache[phone_number_formatted] = names

    return names

# test
user_inputted_country_code = input("Enter country code (ex. 1): ")
user_inputted_number = input("Enter phone # (ex. 6503860386): ")
lookup = reverse_phone_lookup(consts.FUSION_API_KEY, consts.GPLACES_API_KEY, user_inputted_country_code, user_inputted_number)
print('*' * 50, '\n')
print("Results: " + str(lookup))
print("Cache: ", str(consts.cache))
