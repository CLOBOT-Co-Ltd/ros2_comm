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

class PubVerb(VerbExtension):
    """Set the publisher to load or unload"""

    def add_arguments(self, parser, cli_name):
        arg = parser.add_argument(
            'topic_name',
            help="Name of the ROS topic")
        arg.completer = test_completer

        arg = parser.add_argument(
            'topic_type',
            help="Type of the ROS topic")
        arg.completer = SelectCompleter(key='topic_name')
        
        arg = parser.add_argument(
            "state",
            choices=["load", "unload"],
            help="State in which to add or remove the topic")


    def main(self, *, args):
        ...