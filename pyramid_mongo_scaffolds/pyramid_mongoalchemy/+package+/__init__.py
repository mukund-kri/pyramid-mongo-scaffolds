from pyramid.config import Configurator
from lib.mongo import mongo


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # MongoDB connection configuration
    url_str = settings.get('mongo_uri', 'mongodb://localhost:27017/default')
    mongo.configure(url_str)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
