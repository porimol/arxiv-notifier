# coding=utf-8
from flask import Blueprint
from notifier.app.landing import landing_page
from notifier.app.subscribe import subscriber
from notifier.app.contact import contact_us


# Routes Register
notify_routers = Blueprint(
    "arxiv_notifier",
    __name__)

notify_routers.add_url_rule(
    "/",
    strict_slashes=False,
    endpoint="landing_page",
    view_func=landing_page,
    methods=['GET'])

notify_routers.add_url_rule(
    "/contact-us",
    strict_slashes=False,
    endpoint="contact_us",
    view_func=contact_us,
    methods=['POST'])


notify_routers.add_url_rule(
    "/subscribe",
    strict_slashes=False,
    endpoint="subscriber",
    view_func=subscriber,
    methods=['POST'])
