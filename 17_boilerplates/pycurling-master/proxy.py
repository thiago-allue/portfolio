import pycurl

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

_proxy_url = 'proxy.com:80'
_proxy_port = 80


def fetch_url(url):
    buf = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH)
    c.setopt(pycurl.PROXY, _proxy_url)
    c.setopt(pycurl.PROXYPORT, _proxy_port)
    c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
    c.setopt(pycurl.PROXYAUTH, pycurl.HTTPAUTH_NTLM)
    c.setopt(pycurl.PROXYUSERNAME, '')
    c.setopt(pycurl.PROXYPASSWORD, '')

    c.setopt(c.WRITEDATA, buf)
    c.perform()
    c.close()

    body = buf.getvalue()
    return body


def fetch_file(url, save_path):
    with open(save_path, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH)
        c.setopt(pycurl.PROXY, _proxy_url)
        c.setopt(pycurl.PROXYPORT, _proxy_port)
        c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
        c.setopt(pycurl.PROXYAUTH, pycurl.HTTPAUTH_NTLM)
        c.setopt(pycurl.PROXYUSERNAME, '')
        c.setopt(pycurl.PROXYPASSWORD, '')
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()


def fetch_url_ntlm(url):
    buf = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)

    user = ''
    password = ''

    c.setopt(pycurl.PROXY, _proxy_url)
    c.setopt(pycurl.PROXYPORT, _proxy_port)

    c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_NEGOTIATE)
    c.setopt(pycurl.USERPWD, "{}:{}".format(user, password))

    c.setopt(c.WRITEDATA, buf)
    c.perform()
    c.close()

    return buf.getvalue().decode()
