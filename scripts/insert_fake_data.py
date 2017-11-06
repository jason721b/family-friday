#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Usage
#   PYTHONPATH=. python scripts/insert_fake_data.py

import argparse
from faker import Faker
from members import Member


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int, default=100,
                        help='Specify # of fake members record to be inserted')

    args = parser.parse_args()

    fake = Faker()

    Member.init()

    for _ in range(args.count):
        member = Member(first_name=fake.first_name(), last_name=fake.last_name())
        member.save()

if __name__ == '__main__':
    main()

