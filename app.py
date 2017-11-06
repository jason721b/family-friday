#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

from flask import Flask, url_for
from flask import render_template, request, redirect, flash

from members import Member
from random_group import random_group

app = Flask(__name__)

# TODO: Specify secret_key via env variable
app.secret_key = '28cfe91e907f'

logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# This creates an Elasticsearch index for Member model
#    Elasticsearch index can be treated as table in SQL database
Member.init()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lunch_time')
def lunch_time():
    # NOTE: There may be a performance issue if there are millions of members
    all_members = list(Member.all())
    return render_template('lunch_time.html', groups=random_group(all_members))


@app.route('/members/new')
def new_member():
    return render_template('new_member.html')


@app.route('/members/create', methods=['POST'])
def create_member():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    if not first_name or not last_name:
        flash('Both first name and last name need to be specified', 'error')
        return render_template('new_member.html', first_name=first_name, last_name=last_name)

    member = Member(first_name=first_name.strip(), last_name=last_name.strip())
    try:
        member.save()
        flash('Created new team member %s' % member.name, 'success')
    except Exception:
        flash('Failed to create new team member %s' % member.name, 'error')
    return redirect(url_for('new_member'))


@app.route('/members/')
def list_members():
    return render_template('list_members.html', members=Member.all())


@app.context_processor
def inject_helpers():
    return dict(enumerate=enumerate)
