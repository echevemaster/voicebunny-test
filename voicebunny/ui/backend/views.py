# -*- coding=utf-8 -*-
from __future__ import unicode_literals
import flask
import requests
import simplejson
from requests.auth  import HTTPBasicAuth
from voicebunny.app import app
from voicebunny.modules import api

bp = flask.Blueprint('backend', __name__,
                     template_folder='templates')
key = app.config['BUNNY_KEY']
token = app.config['BUNNY_TOKEN']

@bp.route('/', methods=['GET', 'POST'])
def index():
    response = None
    link = None
    form = api.forms.AddVBSpeedyForm()
    if form.validate_on_submit():
        url = 'https://api.voicebunny.com'
        api_id = key
        api_key = token
        req = requests.post(url + '/projects/addSpeedy.json',
            data={
                'title': form.title.data,
                'script': form.script.data,
                'test': '1'
                },
            auth=HTTPBasicAuth(api_id, api_key), verify=False)
        data = simplejson.loads(req.text)
        print data
        response = data['project']['reads']
        for obj in response:
            urls = obj['urls']
            for part_key, part_data in urls.items():
                print part_key
                link =  part_data['default']
                msg = flask.Markup("<a href="+str(link)+">here</a>")
        # response = flask.jsonify(data)
        flask.flash("Your file is here :" + msg)
        return flask.redirect(flask.url_for('backend.file_received'))

    return flask.render_template('backend/index.html',
                                 title='Send your record to Voicebunny',
                                 voice_form=form)


@bp.route('/received_file', methods=['GET', 'POST'])
def file_received():
    return flask.render_template('backend/file_received.html',
                                 title='Download your file')
