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

from kwrankingclient import base
from kwrankingclient.openstack.common.gettextutils import _  # noqa


class NodeClientManager(base.BaseClientManager):
    """Manager for the Node connected requests."""

    def rank_hosts_list(self, hosts):
        """Rank hosts list."""
        return self._create('/hosts/get-rank/', hosts, 'nodes_status')

    def add_hosts_list(self, host):
        """Add a host in list."""
        return self._create('/hosts/set/', host, 'nodes_status')

    def get(self, host):
        """Get node status."""
        return self._get('/hosts/get/%s/' % host, 'nodes_status')

    def list(self, sort_by=None):
        """List node status."""
        hosts = self._get('/hosts/get/', 'nodes_status')
        if sort_by:
            hosts = sorted(hosts, key=lambda l: l[sort_by])
        return hosts

    def list_ids(self, sort_by=None):
        """List node status."""
        hosts = self._get('/hosts/get-id/', 'nodes_status')
        if sort_by:
            hosts = sorted(hosts, key=lambda l: l[sort_by])
        return hosts
