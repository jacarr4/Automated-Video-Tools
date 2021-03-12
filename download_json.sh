# STEPS TO REPRODUCE: 
# load the twitch page with the clips you are looking for
# click 'inspect element'
# go to the network tab
# reload the page
# look through the requests until you find the one with the URLs
# right click -> copy -> copy as cURL
curl 'https://gql.twitch.tv/gql' \
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
  --compressed > clips_file.json
