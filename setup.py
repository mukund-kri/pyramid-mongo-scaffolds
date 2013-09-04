'''
Setup script for pyramid_mongo_scaffolds.
'''

from setuptools import setup, find_packages

requires = [
    # 'pyramid',
    #'mongoengine',
    ]

scaffolds = """
[pyramid.scaffold]
mongoengine = pyramid_mongo_scaffolds:PyramidMongoengineTemplate
mongokit = pyramid_mongo_scaffolds:PyramidMongokitTemplate
"""

classifiers = [
    "Programming Language :: Python",
    "Framework :: Pyramid",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ]

setup(
    name='pyramid_mongo_scaffolds',
    version='0.0.1',
    description='A bunch of scaffolds of pyramid and mongo ODMs',
    
    classifiers=classifiers,

    author='Mukund K',
    author_email='mukund.kri@gmail.com',
    url='My github page',
    keywords='pyramid mongodb mongo scaffold',
    packages=find_packages(),
    include_package_data=True,   
    zip_safe=False,              
    install_requires=requires,
    entry_points=scaffolds,
)
