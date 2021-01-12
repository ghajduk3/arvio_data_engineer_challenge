from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import requests
import sys

class Downloader:

    def download(self,url,baseUrl):
        try:
            r = requests.get(baseUrl + url, timeout=3.0)
            if r.headers.get('content-type') != 'application/pdf':
                sys.exit()
                # log error
            return r.content
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
            print(e)
