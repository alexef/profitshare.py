from time import strftime, gmtime
from urllib import urlencode
from hashlib import sha1
import hmac
import requests


SERVER_URL = 'http://api.profitshare.ro/'
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
# Padding is needed for empty query string.
PADDING = 'padding'
CONTENT_TYPE = 'application/x-www-form-urlencoded'


class ProfitShare(object):
    def __init__(self, user, key):
        self.user = user
        self.key = key

    def _post(self, url, data=None):
        data = data or {}
        req_url = SERVER_URL + url + '/?' + PADDING
        date = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
        signature_string = (
            'POST{url}/?{PADDING}/{user}{date}'
        ).format(url=url, user=self.user, date=date, PADDING=PADDING)
        auth = hmac.new(self.key, signature_string, sha1).hexdigest()
        headers = {
            'Date': date,
            'User-Agent': USER_AGENT,
            'X-PS-Client': self.user,
            'X-PS-Accept': 'json',
            'X-PS-Auth': auth,
            'Content-Type': CONTENT_TYPE,
        }
        r = requests.post(req_url, data=urlencode(data), headers=headers)
        return r.text

    def affiliate_links(self, name, url):
        URL = 'affiliate-links'
        data = {'0[name]': name, '0[url]': url}
        return self._post(URL, data)
