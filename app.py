#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

from flask import Flask
from flask import render_template
from members import Member

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# This creates an Elasticsearch index for Member model
#    Elasticsearch index can be treated as table in SQL database
Member.init()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random_group')
def random_group():
    return render_template('random_group.html')


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')


@app.route('/users/create', methods=['POST'])
def create_user():
    return 'Create New Users'


@app.route('/users/')
def list_user():
    return render_template('list_users.html', members=Member.all())

