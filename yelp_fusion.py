import requests

# get all names of all businesses returned by a given phone #
# (ex. (408) 720-8586 gives ['Taco Bell', 'KFC'] since they share the same phone_number)
def filter(yelp_fusion_api_key, phone_number):
    url = f'https://api.yelp.com/v3/businesses/search/phone?phone=+{phone_number}'
    response = requests.get(url, headers={'Authorization': f'Bearer {yelp_fusion_api_key}'})
    response_json = response.json()

    business_names = []
    if 'businesses' in response_json:
        for business in response_json['businesses']:
            name = business.get('name')
            if name: business_names.append(name)

    return business_names