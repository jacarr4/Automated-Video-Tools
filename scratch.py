import json

JSON_FILE = 'clips_file.json' # input
URL_FILE = 'url_file.txt' # output
NUM_CLIPS = 10

def get_urls( json_file ):
    urls = []

    with open( json_file, 'r' ) as f:
        json_data = json.loads( f.read() )
        for clip_object in json_data[ 0 ][ 'data' ][ 'game' ][ 'clips' ][ 'edges' ]:
            urls.append( clip_object[ 'node' ][ 'url' ] )

    return urls

def write_urls( urls, url_file ):
    with open( url_file, 'w' ) as f:
      for url in urls:
          f.write( f'{url}\n' )

if __name__ == '__main__':
    urls = get_urls( JSON_FILE )
    urls = urls[ :NUM_CLIPS ]
    write_urls( urls, URL_FILE )
