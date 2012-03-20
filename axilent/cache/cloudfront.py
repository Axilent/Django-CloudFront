"""
Cache backend for Django that uses AWS Cloudfront.
"""
from django.core.cache.backends.base import BaseCache

# TODO - this is just a copy from DummyCache out of Django with the name changed.
# This illustrates the contract that needs to be implemented.

class CloudFrontCache(BaseCache):
    def __init__(self, host, *args, **kwargs):
        BaseCache.__init__(self, *args, **kwargs)

    def add(self, key, value, timeout=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
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
