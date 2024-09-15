from setuptools import setup, find_packages


setup(
    name='exchangerates',
    version='0.3.5',
    description="A module to make it easier to handle historical exchange rates",
    long_description="",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
	    'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    author='Mark Brough',
    author_email='mark@brough.io',
    url='http://github.com/exchangerates/exchangerates',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests >= 2.22.0',
        'six >= 1.12.0'
    ],
    entry_points={
    }
)
