#!/usr/bin/env python

import os
import sys
import boto

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

# Setup
conn = boto.connect_s3()
bucket_name = os.environ.get('LINKSENDER_BUCKET')
bucket = conn.get_bucket(bucket_name)

# TODO: write command line arg as link

# Create index.html
f = open('index.html', 'w')
f.write('<a href="http://pydanny.com">link</a>')

# TODO: Upload index.html to the bucket as public file

# TODO: Open browser to the URL
