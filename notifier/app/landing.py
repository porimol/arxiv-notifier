# coding=utf-8
from flask import jsonify
from flask import render_template
from notifier.app.form import SubscribeForm, ContactForm


def landing_page():
    page_title="Welcome to Arxiv Notifier"
    subscribe_form = SubscribeForm()
    contact_form = ContactForm()

    return render_template('notifier.html', subscribe_form=subscribe_form, contact_form=contact_form, page_title=page_title)
