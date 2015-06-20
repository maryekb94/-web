# coding: utf8

from pyramid.config import Configurator
from pyramid_mailer.mailer import Mailer
from sqlalchemy import engine_from_config



from .models import (
    DBSession,
    Good,
    Category,
    Manufacturer,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.registry['mailer'] = Mailer.from_settings(settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_mailer')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('all_good', '/')
    config.add_route('good', '/good/{id}')
    config.add_route('feedback', '/feedback')
    config.include('pyramid_sacrud', route_prefix='admin')
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (
        ('Tables', [Good,Category,Manufacturer]),)
    config.scan()
    return config.make_wsgi_app()


