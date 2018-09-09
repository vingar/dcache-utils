from setuptools import setup, find_packages

setup(
    name='dcache-utils',
    version='0.0.1',
    author="vgaronne@gmail.com",
    description="dCache utilities scripts",
    license="Apache License, Version 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Environment :: No Input/Output (Daemon)'],
    install_requires=['sseclient'],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages())
