# Copyright (c) 2013 Mirantis Inc.
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


from kwrankingclient.v1 import nodes


class Client(object):
    """Top level object to communicate with Kwranking.

    Contains managers to control requests that should be passed to each type of
    resources - nodes, etc.
    """

    def __init__(self, kwranking_url, auth_token):
        self.kwranking_url = kwranking_url
        self.auth_token = auth_token

        self.node = nodes.NodeClientManager(self.kwranking_url,
                                            self.auth_token)
