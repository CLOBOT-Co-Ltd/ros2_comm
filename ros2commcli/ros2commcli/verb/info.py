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

class InfoVerb(VerbExtension):
    """Prints the comm's Informations"""

    def add_arguments(self, parser, cli_name):
        arg = parser.add_argument(
            'id',
            help="""Device ID to request information. There are tree options.   
            1) '.' : my device
            2) '..' : all devices in the group that you are not subscribed to
            3) '<ID>' : The device ID you want to verify""")
        arg.completer = test_completer

        parser.add_argument(
            '--list', action='store_true',
            help="Prints the list of IDs that you subscribe to When use the '.' arguments")

        parser.add_argument(
            '--pub', action='store_true',
            help="Prints the list of topics you are publishing When use the '.', '..' arguments")
        
        parser.add_argument(
            '--sub', action='store_true',
            help="Prints the list of topics you are subscribing When use the '.' arguments")

        parser.add_argument(
            '--req', action='store_true',
            help="Prints the list of services you are requestable When use the '.' arguments")
        
        parser.add_argument(
            '--res', action='store_true',
            help="Prints the list of services you are responsable When use the '.', '..' arguments")

    def main(self, *, args):
        ...