# Copyright (c) 2014 Bull.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from kwrankingclient import command


class ListNodes(command.ListCommand):
    """Print a list of node status."""
    resource = 'node'
    log = logging.getLogger(__name__ + '.ListNodes')
    list_columns = ['node', 'status']

    def get_parser(self, prog_name):
        parser = super(ListNodes, self).get_parser(prog_name)
        parser.add_argument(
            '--sort-by', metavar="<node_column>",
            help='column name used to sort result',
            default='node'
        )
        return parser


class ShowNode(command.ShowCommand):
    """Show node status."""
    resource = 'node'
    json_indent = 4
    allow_names = False
    log = logging.getLogger(__name__ + '.ShowNode')


class UpdateNode(command.UpdateCommand):
    """Update node status."""
    resource = 'node'
    allow_names = False
    log = logging.getLogger(__name__ + '.UpdateNode')

    def get_parser(self, prog_name):
        parser = super(UpdateNode, self).get_parser(prog_name)
        parser.add_argument(
            '--status', metavar='<STATUS>',
            help='New status for the node'
        )
        return parser

    def args2body(self, parsed_args):
        params = {'status': 'ranking'}
        return params
