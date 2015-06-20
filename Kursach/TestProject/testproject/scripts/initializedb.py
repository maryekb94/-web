
import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Manufacturer,
    Category,
    Good,
    Base,
    )





def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        cat1 = Category(name='Протеин')
        cat2 = Category(name='Креатин')
        cat3 = Category(name='Гейнер')
        man1 = Manufacturer(
            name='ON',
            address='USA',
            info='all good'
        )
        man2 = Manufacturer(
            name='BSN',
            address='USA',
            info='На рынке более 10 лет и зарекомендовал себя как один из лучших брендов'
        )
        good = Good(
            name='Syntha6',
            category=cat1,
            manufacturer=man2,
            taste='Печенье',
            available=True,
            price=4500,
            weight=2500,
            image_name="01.png"
        )

        good2 = Good(
            name='Whey Gold Protein',
            category=cat1,
            manufacturer=man1,
            taste='Шоколад',
            available=True,
            price=3500,
            weight=2000,
            image_name="02.jpg"
        )

        good3 = Good(
            name='Whey Gold Geiner',
            category=cat2,
            manufacturer=man1,
            taste='Ваниль',
            available=True,
            price=3500,
            weight=2000,
            image_name="03.jpg"
        )
        good4 = Good(
            name='CHto to pohojee na geiner',
            category=cat3,
            manufacturer=man1,
            taste='Ваниль',
            available=True,
            price=3500,
            weight=2000,
            image_name="04.jpg"
        )


	
	
        DBSession.add(cat1)
        DBSession.add(cat2)
        DBSession.add(cat3)
        DBSession.add(man1)
        DBSession.add(man2)
        DBSession.add(good)
        DBSession.add(good2)
        DBSession.add(good3)
        DBSession.add(good4)




