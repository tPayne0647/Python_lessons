import requests

# Nautobot Demo API sandbox

# Demo URL and Token
sites_url = "https://demo.nautobot.com/api/dcim/sites/"
api_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


# Set Headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Token {api_token}",
}


# Creates a list of all site names and prints them
def get_sites():
    data = requests.get(
        sites_url,
        headers=headers,
    )
    sites_data = data.json()

    sites = [site["name"] for site in sites_data["results"]]
    print(f"Total sites: {len(sites)} \n {sites}")
    return sites


all_sites = get_sites()


# Asks user to select site need to fix different case input
def user_site_selection():
    while True:
        ask_site = input("Please select a site: ")
        selected_site = ask_site.upper()
        if selected_site in all_sites:
            print("******************************************")
            return selected_site.lower()
        else:
            print("Name misspelled, please try again:  ")


selected_site = user_site_selection()


# Get total number and name of devices in selected site, then prints them
def get_device_count():
    api_url_devices = "https://demo.nautobot.com/api/dcim/devices/"
    test_parameters = {"site": selected_site}
    device_data = requests.get(
        api_url_devices,
        headers=headers,
        params=test_parameters,
    )
    total_site_devices = device_data.json()["count"]
    name_list = device_data.json()
    device_names = [device["name"] for device in name_list["results"]]

    print(
        f"Total number of devices in [{selected_site.upper()}]: {total_site_devices}\n{device_names}"
    )
    return total_site_devices


get_device_count()
