import requests
import auth


def get_lat_lng(address):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    request_url = f'{base_url}address={address}&key={auth.DYSRUP_GOOGLE_API_KEY}'
    response = requests.get(request_url)
    if response.ok:
        json = response.json()
        try:
            location = json.get('results')[0].get('geometry').get('location')
            lat, lng = location.values()
            return lat, lng
        except Exception:
            return None
    return None


def get_address_from_coordinates(lat, lng):
    reverse_url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={auth.DYSRUP_GOOGLE_API_KEY}'
    response = requests.get(reverse_url)
    if response.ok:
        json = response.json()
        try:
            address = json.get('results')[0].get('address_components')
            return address
        except Exception:
            return None
    return None
