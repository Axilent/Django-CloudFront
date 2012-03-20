Django CloudFront
=================

Django Cloudfront is a django cache backend that uses AWS Cloudfront (an AWS integrated CDN) as a backend.

**Warning: Early stages of development.**

Recently AWS announced they were [reducing the minimum TTL for Cloudfront](http://aws.amazon.com/about-aws/whats-new/2012/03/19/amazon-cloudfront-lowers-minimum-expiration-period/).  This makes CloudFront suitable to be an arbitrary, industrial strength caching mechanism.  Creating a new caching backend means Django apps that use the built-in caching framework will be able to use CloudFront without further modification to Django apps.

Requirements
------------
*	[Boto](https://github.com/boto/boto): A Python interface to AWS.
*	[Django](http://www.djangoproject.com): The Python-based web framework for which this cache plugin is made, thus, the point.
*	[wsgiref](http://pypi.python.org/pypi/wsgiref): The reference implementation of the WSGI standard.

Required Settings
-----------------

*	`CLOUDFRONT_BUCKET`: The name of the AWS CloudFront bucket to use.
*	`AWS_ACCESS_KEY_ID`: The access key id for your AWS account.
*	`AWS_SECRET_ACCESS_KEY`: The secret access key for your AWS account.

Installation
------------

First set up AWS CloudFront.  Have a look at the [AWS Documentation](http://docs.amazonwebservices.com/AmazonCloudFront/latest/GettingStartedGuide/StartingCloudFront.html).  Make sure you have set the required settings (above) appropriately.

In `settings.py`, set your cache backend like so:

	CACHES = {
		'default':{
			'BACKEND':'axilent.cache.cloudfront.CloudFrontCache'
		},
	}

