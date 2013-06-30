#!/usr/bin/env python

import os
import sys
import boto
from boto.s3.key import Key

# Setup
conn = boto.connect_s3()
bucket_name = os.environ.get('LINKSENDER_BUCKET')
bucket = conn.get_bucket(bucket_name)

# TODO: write command line arg as link

# Upload index.html to the bucket as public file

k = Key(bucket)
k.key = 'index.html'
k.set_metadata("Content-Type", 'text/html')
k.set_contents_from_string('<a href="http://pydanny.com">link</a>')
k.make_public()

# TODO: Open browser to the URL
