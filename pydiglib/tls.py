import ssl, socket, struct

from .util import *


def get_ssl_context(hostname):
    """Return SSL context object"""
    try:
        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    except:
        if hostname:
            print("Warning: Hostname checking unavailable in ssl module.")
        return None
    else:
        ctx.options |= ssl.OP_NO_SSLv2
        ctx.options |= ssl.OP_NO_SSLv3
        ctx.options |= ssl.OP_NO_TLSv1

        ctx.load_default_certs()
        ctx.verify_mode = ssl.CERT_REQUIRED

        if hostname:
            try:
                ctx.check_hostname = True
            except AttributeError:
                print("Warning: Hostname checking unavailable in ssl module.")

        return ctx


def get_ssl_connection(ctx, s, hostname):
    """Return SSL/TLS connection object"""
    if ctx:
        return ctx.wrap_socket(s, server_hostname=hostname)
    else:
        return ssl.wrap_socket(s)

