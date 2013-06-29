linksender
==========

Sends a link to Amazon S3 from the command line.

Installation::

    $ pip install boto

Also, add this to the end of your ~/.bashrc (or ~/.profile or similar) and source it:

    # For ~/code/linksender
    export LINKSENDER_BUCKET="some-new-bucket"

Usage:

    $ python linksender.py <url>

Credits:

* http://stackoverflow.com/questions/14317243/boto-uploading-file-to-a-specific-location-on-amazon-s3