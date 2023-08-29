import facebook

# Your Facebook Access Token
access_token = 'EAAzrLPJ91c8BO4FiJRpewSOf6TNmZC0UYjhCb4cOOHrNAcZASxfqiOV0ePIJ6ZBTfagfNBNu5zZBavonYodw1sIFG0tNFnJ9Ho2riZCRwHoZCZAu58ZCv2WMiS3HTTJHvZC5DpEM58N4ee02FlP0uOIMHibn4pyZB8VpSvqDkm1BBI7I2PeOS9tOClrTfJNZBuB3ZAEVIDiU91lLFOuzruZAQEPZCFrM247k0tOr7dZB3IhkaZCVAi1n0rpSlGWGU83W0UoZD'

# Create a Facebook Graph API object
graph = facebook.GraphAPI(access_token)

# Retrieve user's friends
friends = graph.get_object('/me/friends')

for friend in friends['data']:
    print(friend['name'])
