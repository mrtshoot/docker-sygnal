# Copyright 2015 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class InvalidNotificationException(Exception):
    pass


class PushkinSetupException(Exception):
    pass


class NotificationDispatchException(Exception):
    pass


class TemporaryNotificationDispatchException(Exception):
    """
    To be used by pushkins for errors that are not our fault and are
    hopefully temporary, so the request should possibly be retried soon.
    """

    def __init__(self, *args: object, custom_retry_delay=None) -> None:
        super().__init__(*args)
        self.custom_retry_delay = custom_retry_delay