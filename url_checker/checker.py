from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url, timeout=10):
    """
    This will return TRUE if the site is online.
    It will raise an exception if the site isn't online
    """

    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]

    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error
