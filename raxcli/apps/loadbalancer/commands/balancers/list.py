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

from raxcli.models import Collection
from raxcli.commands import BaseListCommand
from raxcli.apps.loadbalancer.resources import Balancer
from raxcli.apps.loadbalancer.utils import LoadBalancerCommand
from raxcli.apps.loadbalancer.utils import for_all_regions


class ListCommand(LoadBalancerCommand, BaseListCommand):
    """
    Output Balancers list.
    """
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        def get_balancers(client):
            return [Balancer(b) for b in client.list_balancers()]

        balancers = for_all_regions(action_func=get_balancers,
                                    parsed_args=parsed_args)
        collection = Collection(balancers)

        return collection.generate_output()
