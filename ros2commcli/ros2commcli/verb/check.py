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

from ros2commcli.api import test_completer

class CheckVerb(VerbExtension):
    """Prints the comm's Check Informations"""

    def add_arguments(self, parser, cli_name):
        arg = parser.add_argument("robot_id", help="ID of the robot you want to check")
        arg.completer = test_completer

        arg = parser.add_argument(
            'state',
            choices=['topic', 'service', 'all'],
            help="State of what kind of interface to print")

    def main(self, *, args):
        ...