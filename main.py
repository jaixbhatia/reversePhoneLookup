import sqlite3, json
import gplaces, yelp_fusion, consts
from sqlite_caching import create_connection, create_table, add_to_cache, get_from_cache  # Import necessary functions from sqlite_caching

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
    # 2) Check cache
    conn = create_connection('cache.db')
    if conn is not None:
        create_table(conn)  # Create the table if it doesn't exist
        cached_data = get_from_cache(conn, phone_number_formatted)
        if cached_data:
            conn.close()
            return json.loads(cached_data)
    # 3)
    try:
        names = gplaces.filter(gplaces_api_key, phone_number_formatted)
        if not names: # if nothing found from gplaces API, run yelp fusion API
            names = yelp_fusion.filter(yelp_fusion_api_key, phone_number_formatted)
    except PermissionError as e:
        print(f"Permission error occurred: {e}")
        names = []
    # 4) Cache results using SQLite
    if conn is not None:
        add_to_cache(conn, phone_number_formatted, names)
        conn.close()
    # 5)
    return names

# test
user_inputted_country_code = input("Enter country code (ex. 1): ")
user_inputted_number = input("Enter phone # (ex. 6503860386): ")
lookup = reverse_phone_lookup(consts.FUSION_API_KEY, consts.GPLACES_API_KEY, user_inputted_country_code, user_inputted_number)
print('*' * 50, '\n')
print("Results: " + str(lookup))