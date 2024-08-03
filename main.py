import requests
from send_email import send_email

api_key = "4ee2a7884a3041a2a66662555795b698"
url = ("https://newsapi.org/v2/everything?q=tesla&" 
       "from=2024-07-03&sortBy=publishedAt&apiKey="
       "4ee2a7884a3041a2a66662555795b698")

# Make a request
req = requests.get(url)

# Get a dictionary with data
content = req.json()
print(content)
print(type(content["articles"]))

body = ""

# Print title and author's name
for article in content["articles"]:
       body = body + article["title"] + "\n" + article["content"] + "\n" + str(article["author"]) + 2*"\n"
print(body)

body = body.encode("utf-8")
send_email(body)