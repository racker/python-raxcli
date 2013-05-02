# Copyright 2013 Rackspace
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    'BaseRegistryCommand',
    'BaseRegistryListCommand'
]

from service_registry.client import Client

from raxcli.config import get_config as get_base_config
from raxcli.commands import BaseCommand, BaseShowCommand, BaseListCommand


class BaseRegistryCommand(BaseCommand):
    def get_parser(self, prog_name):
        parser = super(BaseRegistryCommand, self).get_parser(prog_name=prog_name)
        parser.add_argument('--region', dest='region')
        return parser


class BaseRegistryShowCommand(BaseRegistryCommand, BaseShowCommand):
    pass


class BaseRegistryListCommand(BaseRegistryCommand, BaseListCommand):
    def get_parser(self, prog_name):
        parser = super(BaseRegistryListCommand, self).get_parser(prog_name=prog_name)
        parser.add_argument('--limit', dest='limit')
        parser.add_argument('--marker', dest='marker')
        return parser


def get_config():
    return get_base_config()


def get_client(parsed_args):
    config = get_config()

    username = config['username']
    api_key = config['api_key']

    if parsed_args.username:
        username = parsed_args.username

    if parsed_args.api_key:
        api_key = parsed_args.api_key

    api_url = parsed_args.api_url
    region = parsed_args.region

    if not username:
        raise ValueError('Missing required argument: username')

    if not api_key:
        raise ValueError('Missing required argument: api-key')

    kwargs = {}

    if api_url is not None:
        kwargs['base_url'] = api_url

    if region is not None:
        kwargs['region'] = region

    c = Client(username=username, api_key=api_key, **kwargs)
    return c
