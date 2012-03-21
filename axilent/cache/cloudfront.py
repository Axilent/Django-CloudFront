"""
Cache backend for Django that uses AWS Cloudfront.
"""
from django.core.cache.backends.base import BaseCache

import boto
from cStringIO import StringIO
from django.conf import settings

aws_access_key_id = settings.AWS_ACCESS_KEY_ID
aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
bucket = settings.CLOUDFRONT_BUCKET

class CloudFrontCache(BaseCache):
    def __init__(self, host, *args, **kwargs):
        BaseCache.__init__(self, *args, **kwargs)
        self.conn = boto.connect_cloudfront(aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key) # establish cloudfront connection
        self.distro = self.conn.create_distribution(origin='%s.s3.amazonaws.com' % bucket,enabled=True)

    def add(self, key, value, timeout=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        self.distro.add_object(key,StringIO(value))
        # TODO - make URL?
        return True

    def get(self, key, default=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        return default

    def set(self, key, value, timeout=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)

    def delete(self, key, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)

    def get_many(self, keys, version=None):
        return {}

    def has_key(self, key, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        return False

    def set_many(self, data, version=None):
        pass

    def delete_many(self, keys, version=None):
        pass

    def clear(self):
        pass
