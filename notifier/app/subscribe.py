# coding=utf-8
from flask import jsonify
from flask import render_template
from flask import redirect
from notifier.app.form import SubscribeForm
from pytz import timezone
from datetime import datetime
from config import db


def subscriber():
    page_title='Congratulations'
    subscribe_form = SubscribeForm()

    if subscribe_form.validate_on_submit():
        asia_timezone = timezone('Asia/Dhaka')
        full_name = subscribe_form.full_name.data

        subscriber_data = {
            'full_name': full_name,
            'email_address': subscribe_form.email_address.data,
            'subscribe_categories': ['CS'],
            'subscribe_at': asia_timezone.localize(datetime.utcnow()),
            'created_at': asia_timezone.localize(datetime.utcnow()),
            'updated_at': asia_timezone.localize(datetime.utcnow())
        }
        rsp = db.subscriber.insert_one(subscriber_data)
        
        return render_template('subscribe_success.html', page_title=page_title, full_name=full_name)

    else:
        page_title='Welcome to Arxiv Notifier'
        return render_template('notifier.html', subscribe_form=subscribe_form, page_title=page_title)
