import json

GPLACES_API_KEY = '' # ask jai for api key
FUSION_API_KEY = 'abc' # ask jai for api key

temp_cache = {}

def save_dict_to_json(file_name, dictionary):
    # Load existing data if file exists
    try:
        with open(file_name, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    # Update existing data with new dictionary
    existing_data.update(dictionary)

    # Write updated data back to file
    with open(file_name, 'w') as file:
        json.dump(existing_data, file)

def cache(names, phone_number_formatted):
    if names:
        if phone_number_formatted in temp_cache:
            temp_cache[phone_number_formatted] += names
        else:
            temp_cache[phone_number_formatted] = names
    save_dict_to_json('cache.json', temp_cache)