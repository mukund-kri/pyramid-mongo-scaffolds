from pyramid.scaffolds import PyramidTemplate


class PyramidMongoengineTemplate(PyramidTemplate):
    _template_dir = 'pyramid_mongoengine'
    summary = 'pyramid mongoengine project'

class PyramidMongokitTemplate(PyramidTemplate):
    _template_dir = 'pyramid_mongokit'
    summary = 'pyramid mongokit project template'

