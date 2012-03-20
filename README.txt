Django Cloudfront
=================

Django Cloudfront is a django cache backend that uses AWS Cloudfront (an AWS integrated CDN) as a backend.

Recently AWS announced they were [reducing the minimum TTL for Cloudfront](http://aws.amazon.com/about-aws/whats-new/2012/03/19/amazon-cloudfront-lowers-minimum-expiration-period/).  This makes CloudFront suitable to be an arbitrary, industrial strength caching mechanism.  Creating a new caching backend means Django apps that use the built-in caching framework will be able to use CloudFront without further modification to Django apps.

