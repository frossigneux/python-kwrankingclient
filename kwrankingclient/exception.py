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


from kwrankingclient.openstack.common.gettextutils import _  # noqa


class KwrankingClientException(Exception):
    """Base exception class."""
    message = _("An unknown exception occurred %s.")
    code = 500

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass

        if not message:
            message = self.message % kwargs

        super(KwrankingClientException, self).__init__(message)


class CommandError(KwrankingClientException):
    """Occurs if not all authentication vital options are set."""
    message = _("You have to provide all options like user name or tenant "
                "id to make authentication possible.")
    code = 401


class NotAuthorized(KwrankingClientException):
    """HTTP 401 - Not authorized.

    User have no enough rights to perform action.
    """
    code = 401
    message = _("Not authorized request.")


class NoKwrankingEndpoint(KwrankingClientException):
    """Occurs if no endpoint for Kwranking set in the Keystone."""
    message = _("No publicURL endpoint for Kwranking found. Set endpoint "
                "for Kwranking in the Keystone.")
    code = 404


class NoUniqueMatch(KwrankingClientException):
    """Occurs if there are more than one appropriate resources."""
    message = _("There is no unique requested resource.")
    code = 409


class UnsupportedVersion(KwrankingClientException):
    """Occurs if unsupported client version was requested."""
    message = _("Unsupported client version requested.")
    code = 406


class IncorrectLease(KwrankingClientException):
    """Occurs if lease parameters are incorrect."""
    message = _("The lease parameters are incorrect.")
    code = 409
