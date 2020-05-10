import hashlib


# mystring = 'asd'
# # Assumes the default UTF-8
# hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())

class URL:
    def __init__(self):
        self.urls = dict()
        self.prefix = 'http://short.pl/'

    def shorten(self, url):
        hash_object = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[hash_object] = url
        return self.prefix + hash_object

    def restore(self, short):
        return self.urls[short.replace(self.prefix, '')]


if __name__ == '__main__':
    url = 'https://www.geeksforgeeks.org/python-strings-decode-method/'
    u = URL()

    shortened_url = u.shorten(url)
    print(shortened_url)
    assert u.restore(shortened_url) == url
