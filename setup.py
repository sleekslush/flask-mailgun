from setuptools import setup


setup(
    name='Flask-Mailgun',
    version='0.1',
    url='http://github.com/sleekslush/flask-mailgun',
    license='BSD',
    author='Craig Slusher',
    author_email='cslush@gmail.com',
    description='Adds Mailgun support to Flask applications',
    long_description=__doc__,
    packages=['flask_mailgun'],
    namespace_packages=['flask_mailgun'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'requests'
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
