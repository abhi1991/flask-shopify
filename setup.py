"""
Flask-Shopify
-------------

Links
`````

* `documentation <http://packages.python.org/Flask-Shopify>`_
* `development version
  <http://github.com/lateshowlabs/flask-shopify/zipball/master#egg=Flask-Shopify-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-Shopify',
    version='0.1',
    url='code.lateshowlabs.com',
    license='BSD',
    author='David Caplan',
    author_email='dcaplan@lateshowlabs.com',
    description='Flask extension for the Shopify API',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
