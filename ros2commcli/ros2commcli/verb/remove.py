# Copyright 2023 CLOBOT Co., Ltd
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

from ros2cli.verb import VerbExtension

from ros2commcli.api import test_completer, list_completer, SelectCompleter

class RemoveVerb(VerbExtension):
    """Remove the comm's Subscription Informations"""

    def add_arguments(self, parser, cli_name):
        arg = parser.add_argument(
            '--group', type=str,
            help="Remove the Group to belong to")
        arg.completer = test_completer
        
        arg = parser.add_argument(
            '--id', type=str,
            help="Remove the ID to subscribe")
        arg.completer = test_completer

        arg = parser.add_argument(
            '--all-id', action='store_true',
            help="Remove all the ids that exist within the group to which you belong")
        
        arg = parser.add_argument(
            '--belong-to', type=str,
            help="Remove all the ids that exist within this group")
        arg.completer = test_completer
        
    def main(self, *, args):
        ...