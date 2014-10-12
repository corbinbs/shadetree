"""
ShadeTree OBD
-------------

A Python library to help the Shade Tree Mechanic easily interface with OBD-II scanners

ShadeTree OBD is distributed under the MIT License.
"""
from setuptools import setup


setup(
    name="shadetree",
    version="0.1",
    license="MIT",
    author="HUB-OLOGY",
    author_email="corbinbs@hubology.org",
    url="http://hub-ology.org",
    download_url = 'https://github.com/corbinbs/shadetree/tarball/0.1',
    description="ShadeTree OBD",
    long_description=__doc__,
    packages=["shadetree", "shadetree.obd"],
    scripts=["bin/shadetree"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "pyserial>=2.7"
    ],
    tests_require=[
        "nose",
        "tox"
    ],
    test_suite = 'nose.collector',
    keywords = ['obd', 'obdii', 'automotive'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Topic :: Utilities"
    ]
)