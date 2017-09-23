from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup


setup(
    name='toto',
    version='0.1.0.dev0',
    description='Toto',
    long_description="Bla bla bla",
    keywords='example',
    url='https://example.com/',
    author='Toto',
    author_email='toto@example.com',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',
    install_requires=[
    ],
    zip_safe=False,
)
