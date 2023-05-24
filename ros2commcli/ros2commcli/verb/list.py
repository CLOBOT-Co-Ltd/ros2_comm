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

class ListVerb(VerbExtension):
    """Prints the comm's List Informations"""

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            '-t', '--type', action='store_true',
            help="Print the entire type list")

        parser.add_argument(
            '-g', '--group', action='store_true',
            help="Print the entire group list")
        
        arg = parser.add_argument(
            '--type-name', type=str,
            help="Print the entire ID list corresponding to TYPE_NAME")
        arg.completer = test_completer

        arg = parser.add_argument(
            '--group-name', type=str,
            help="Print the entire ID list belonging to GROUP_NAME")
        arg.completer = test_completer
        
    def main(self, *, args):
        ...