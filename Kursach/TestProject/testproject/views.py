# coding: utf8

from pyramid.response import Response
from pyramid_mailer.message import Message
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Good,
    Category
    )

@view_config(route_name='good', renderer='templates/good.jinja2')
def good_view(request):
    good_id = request.matchdict['id']
    good = DBSession.query(Good).filter_by(id=good_id).first()
    if not good:
        return Response('Not found')
    return {'good' : good}


@view_config(route_name='all_good', renderer='templates/all_good.jinja2')
def goods_view(request):
    categories = DBSession.query(Category)
    goods = DBSession.query(Good)
    category = None
    if 'category_filter' in request.GET:
        category_id = request.GET['category_filter']
        category = categories.filter_by(id=category_id).first()
    if category:
        goods = goods.filter_by(category=category).all()
    else:
        goods = goods.all()
    return {'goods': goods,
            'categories': categories,
            'selected_category': category}


@view_config(route_name='feedback', request_method='GET',
             renderer='templates/feedback.jinja2')
def feedback_get(request):
    return {}

@view_config(route_name='feedback', request_method='POST',
             renderer='templates/feedback_report.jinja2')
def feedback_post(request):
    try:
        support_mail = request.registry.settings['mail.username']
        subject = request.POST['subject']
        email = request.POST['email']
        body = request.POST['message']
        if not (subject and email and body):
            return {'error_report': 'Не все поля заполнены'}
        mailer = request.registry['mailer']
        message = Message(subject=subject,
                          sender=support_mail,
                          recipients=[support_mail],
                          body=body,
                          extra_headers={'From': email})

        mailer.send(message)
        return {'success_report': 'Письмо отправлено успешно'}
    except Exception as ex:
        return {'error_report': ex}
