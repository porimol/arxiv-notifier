# coding=utf-8
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import url_for
from notifier.app.form import ContactForm


def contact_us():
    page_title='Contact Us'
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        full_name = contact_form.full_name.data
        email_address = contact_form.email_address.data
        subject = contact_form.subject.data
        message = contact_form.message.data
        
        return render_template('contact_followup.html', page_title=page_title, full_name=full_name)

    else:
        # return redirect(url_for('arxiv_notifier.landing_page'))
        return {'sss': 89}
    
