"""
HTTP (Hyper text transfer protocol)
"""

# other protocols
# ip, tcp, udp, smtp. ftp, httpa, https

# HTTP - request
# Method URI HTTP/version
# Starting line
# Get /Category HTTP/1.1


# starting line:
#     method -> one of (POST, GET, PUT, PATCH, DELETE)
#     URI -> (uniform resource identifier) -> path to resource (/., /shop, /category)
#     HTTP version (which version of http used to create request) (1.1, 2 ...)

# HTTP methods
# GET -> getting resource
# POST -> sending data (creating resource)
# PUT -> full replace of resource
# PATCH -> partial replace of resource
# DELETE -> delete resource

# Header of request:
# HOST: makers.kg -> address resource

# GET / HTTP/1.1
# Host: makers.kg

# Body: body of request -> data, which we want to pass
# Accept -> resource format list
# Accept-Encoding -> encoding type list
# Accept-Language
# Authorization
# User-Agent

# HTTP response structure:
#     Beginning line: HTTP/version code
#     Header

# Response header:
#     Content-Type: ...
#     Content-Length: ...
#     Content-Encoding: ...
#     Expires: date when response will expire
#     Location: URI

# URL -> uniform resource locator
# URN -> uniform resource name
# URI -> uniform resource identifier

