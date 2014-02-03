from pyramid.config import Configurator
import ming


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # MongoDB connection configuration
    url_str = settings.get('mongo_uri', 'mongodb://localhost:27017/default')
    ming_config = {'ming.default.uri': url_str}
    ming.configure(**ming_config)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
