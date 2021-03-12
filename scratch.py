from bs4 import BeautifulSoup
import requests

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

URL = "https://www.twitch.tv/directory/game/Just%20Chatting/clips?range=all"

CURL_URL = """curl 'https://gql.twitch.tv/gql' \
  -H 'Connection: keep-alive' \
  -H 'Authorization: OAuth v3sxp8w65fs7e111oofu4hvyyuwukt' \
  -H 'Accept-Language: en-US' \
  -H 'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36' \
  -H 'X-Device-Id: CbHLeGQK5dSUl8DO5f02Fd6drdDwpymj' \
  -H 'Content-Type: text/plain;charset=UTF-8' \
  -H 'Accept: */*' \
  -H 'Sec-GPC: 1' \
  -H 'Origin: https://www.twitch.tv' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://www.twitch.tv/' \
  --data-raw '[{"operationName":"ClipsCards__Game","variables":{"gameName":"Just Chatting","limit":20,"criteria":{"languages":[],"filter":"ALL_TIME"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0d8d0eba9fc7ef77de54a7d933998e21ad7a1274c867ec565ac14ffdce77b1f9"}}}]' \
  --compressed"""

if __name__ == '__main__':
    # soup = BeautifulSoup(html_doc, 'html.parser')
    # print( soup.prettify() )

    # print( URL )
    page = requests.get( CURL_URL )
    soup = BeautifulSoup( page.content, 'html.parser' )
    print( soup.prettify() )
    print( soup.find_all( 'a' ) )
