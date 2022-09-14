import io
import json

from pprint import pprint

import pycurl


def post(url, data):
    buffer = io.BytesIO()

    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.HTTPAUTH, c.HTTPAUTH_GSSNEGOTIATE)
    c.setopt(c.USERPWD, ':')
    c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(c.USERAGENT, 'Python Client')
    c.setopt(c.POSTFIELDS, json.dumps(data).encode())
    c.setopt(c.POST, 1)
    # c.setopt(c.HTTPPOST, data)
    # c.setopt(c.READFUNCTION, f)
    # c.setopt(c.READDATA, data)
    # c.setopt(c.VERBOSE, True)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    print(c.getinfo(c.RESPONSE_CODE))
    print('Elapsed time: {}'.format(c.getinfo(c.TOTAL_TIME)))
    c.close()
    pprint(json.loads(buffer.getvalue().decode()))


if __name__ == '__main__':
    post()
