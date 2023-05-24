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

from setuptools import find_packages
from setuptools import setup

package_name = "ros2commcli"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/" + package_name, ["package.xml"]),
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
    ],
    install_requires=["ros2cli"],
    zip_safe=True,
    author="ClobotPaul",
    author_email="paul@clobot.co.kr",
    maintainer="ClobotPaul",
    maintainer_email="paul@clobot.co.kr",
    url="https://github.com/CLOBOT-Co-Ltd/ros2_comm",
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description="ROS2 Comm command line interface.",
    license="Apache License, Version 2.0",
    tests_require=["pytest"],
    entry_points={
        "ros2cli.command": [
            "comm = ros2commcli.command.comm:CommCommand",
        ],
        "ros2commcli.verb": [
            "info = ros2commcli.verb.info:InfoVerb",
            "list = ros2commcli.verb.list:ListVerb",
            "add = ros2commcli.verb.add:AddVerb",
            "remove = ros2commcli.verb.remove:RemoveVerb",
            "set = ros2commcli.verb.set:SetVerb",
            "pub = ros2commcli.verb.pub:PubVerb",
            "sub = ros2commcli.verb.sub:SubVerb",
            "req = ros2commcli.verb.req:ReqVerb",
            "res = ros2commcli.verb.res:ResVerb",
            "load = ros2commcli.verb.load:LoadVerb",
            "unload = ros2commcli.verb.unload:UnloadVerb",
        ],
    },
)
