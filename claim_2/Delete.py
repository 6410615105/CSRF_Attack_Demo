import requests
import random

# Generate a random contact ID between 1 and 30
contact_id = random.randint(1, 100)

# Define the URL for deleting a contact
url = f'http://127.0.0.1:8000/contact/delete/23'

# Use the actual session ID and CSRF token from your message

# User
#session_id = 'owej5i570es0z1mekb42k6gii8sqzhna'
#csrf_token = 'hMpDxlgsrFWwyOve70RS4XIZoYREejDJ'

# Admin
session_id = 'jftcel8rasex0fevf5xek5fsop87d57r'
csrf_token = '7qWkhnE8gNOSFz3i15fPosPFffEFGIVe'

# Define the headers (include all necessary headers observed in Developer Tools)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'http://127.0.0.1:8000/',
    'X-CSRFToken': csrf_token,
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Define the cookies to include both the session ID and the CSRF token
cookies = {
    'sessionid': session_id,
    'csrftoken': csrf_token
}

# Send the DELETE request
response = requests.delete(url, headers=headers, cookies=cookies)

# Print response details for debugging
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# Check if the contact was deleted successfully
if response.status_code == 200:
    print("Contact deleted successfully!")
else:
    print("Failed to delete contact.")
