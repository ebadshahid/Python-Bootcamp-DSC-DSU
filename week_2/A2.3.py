import requests as r
link = "https://directory.ntschools.net/#/schools"
page = r.get(link)
page.content

# Stuck on JsonDecoderError