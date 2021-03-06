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

import logging

from cliff.show import ShowOne

from raxcli.apps.monitoring.utils import (MonitoringEntityCommand,
                                          get_client)
from raxcli.apps.monitoring.resources import Alarm


class ShowCommand(MonitoringEntityCommand, ShowOne):
    """
    Show the details of an alarm.
    """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(ShowCommand, self).get_parser(prog_name=prog_name)
        parser.add_argument('--id', dest='alarm_id', required=True)
        return parser

    def take_action(self, parsed_args):
        client = get_client(parsed_args)
        alarm = Alarm(client.get_alarm(parsed_args.entity_id,
                                       parsed_args.alarm_id))
        return alarm.generate_output()
