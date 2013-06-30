#!/usr/bin/env python

import argparse
import os
import sys
import webbrowser

import boto
from boto.s3.key import Key

# Setup
conn = boto.connect_s3()
bucket_name = os.environ.get('LINKSENDER_BUCKET')
bucket = conn.get_bucket(bucket_name)

# Get command line URL argument
parser = argparse.ArgumentParser(description='Turn a URL into a static HTML link, hosted by your favorite Amazon S3 bucket.')
parser.add_argument('url', help='URL to be linked to')
args = parser.parse_args()

# Put together HTML page content as string
content = '<a href="{0}">{0}</a>'.format(args.url)

# Upload index.html to the bucket as public file
k = Key(bucket)
k.key = 'index.html'
k.set_metadata("Content-Type", 'text/html')
k.set_contents_from_string(content)
k.make_public()

# Open browser to the URL
browser_url = 'http://{0}.s3-website-us-east-1.amazonaws.com'.format(bucket_name)
webbrowser.open_new(browser_url)