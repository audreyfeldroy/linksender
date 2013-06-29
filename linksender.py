#!/usr/bin/env python

"""
Link sender
"""

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

# TODO...

# Create index.html

# Upload it to the bucket
