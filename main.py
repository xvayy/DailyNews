import requests
from send_email import send_email

topic = "tesla"

api_key = "4ee2a7884a3041a2a66662555795b698"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&" 
       "from=2024-07-03&sortBy=publishedAt&"
       "apiKey=4ee2a7884a3041a2a66662555795b698&"
       "language=en")

# Make a request
req = requests.get(url)

# Get a dictionary with data
content = req.json()
print(content)
print(type(content["articles"]))

body = ""

# Print title and author's name
for article in content["articles"][:3]:
       body = "\n" + body + article["title"] + "\n" \
              + article["description"] + "\n" \
              + str(article["author"]) + "\n" \
              + article["url"] + 2*"\n"

letter = f"""\
Subject: Today's News
{body}
"""


print(body)

letter = letter.encode("utf-8")
send_email(letter)