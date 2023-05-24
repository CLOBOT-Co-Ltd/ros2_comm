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

from ros2commcli.api import test_completer, SelectCompleter

class LoadVerb(VerbExtension):
    """Load the id's topic and service"""

    def add_arguments(self, parser, cli_name):

        arg = parser.add_argument(
            'publisher',
            help="Publisher's ID")
        arg.completer = test_completer

        parser.add_argument(
            '-t', '--topic', action='store_true',
            help="Load all of the ID's publishing topics")
        
        parser.add_argument(
            '-s', '--service', action='store_true',
            help="Load all of the ID's responsable services")
        
    def main(self, *, args):
        ...