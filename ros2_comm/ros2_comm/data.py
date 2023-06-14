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

from ros2_comm.zyre._zyre_ctypes import *
from ros2_comm.zyre._czmq_ctypes import *

from ros2_comm_msgs.msg import *


class CommData(object):
    def __init__(self, id, type, groups):

        self.info = RobotInfo()
        self.info.id = id
        self.info.type = type
        self.info.groups = groups

        self.list = list()
        self.list.append(self.info)

        self.pub = list()
        self.sub = list()
        self.req = list()
        self.res = list()

    def get_info(self):
        return self.info

    def get_info(self, id):
        info = next((item for item in self.list if item.id == id), None)
        return info

    def get_list(self):
        return self.list

    def get_pub(self):
        return self.pub

    def get_pub(self, id):
        # Get the information of topic that id's publishing
        ...
        return list()

    def get_sub(self):
        return self.sub

    def get_req(self):
        return self.req

    def get_res(self):
        return self.res

    def get_res(self, id):
        # Get the information of service that id's responable
        ...
        return list()

    def get_list(self, all):
        if all:
            # Query all robot info in my groups
            ...
        else:
            # Query robot info that you're not subscribing in your groups
            ...
        return list()  # RobotInfo list

    def get_group_list(self):
        # Query the group list
        ...
        return list()

    def get_group_info(self, group):
        # Query the robot list in the group
        ...
        return list()

    def get_type_list(self):
        # Query the type list
        ...
        return list()

    def get_type_info(self, type):
        # Query the robot list in type
        ...
        return list()

    def add_id(self, id):
        # Query the robot id's info
        # info =
        # self.list.append(info)
        ...
        return True

    def add_group(self, group):
        # Request add new group
        self.info.groups.append(group)
        return True

    def add_id_in_group(self, group):
        # Query all robot info in the group
        ...
        return True

    def add_all_id_in_groups(self):
        # Query all robot info in all groups
        ...
        return True

    def remove_id(self, id):
        self.list.remove(id)
        ...
        return True

    def remove_group(self, group):
        self.info.groups.remove(group)
        return True

    def remove_id_in_group(self, group):
        # Remove all robot info in the group
        ...
        return True

    def remove_all_id_in_groups(self):
        # Remove all robot info in all groups
        ...
        return True

    def set_type(self, type):
        self.info.type = type
        return True

    def load_pub(self, pub):
        # Make new converter(ros->zyre)
        self.pub.append(pub)
        return True

    def load_sub(self, sub):
        # Make new converter(zyre->ros)
        self.sub.append(sub)
        return True

    def load_req(self, req):
        # Make new converter service(ros->zyre->ros)
        self.req.append(req)
        return True

    def load_res(self, res):
        # Make new converter service(zyre->ros->zyre)
        self.res.append(res)
        return True

    def unload_pub(self, pub):
        # Delete new converter(ros->zyre)
        self.pub.remove(pub)
        return True

    def unload_sub(self, sub):
        # Delete new converter(zyre->ros)
        self.sub.remove(sub)
        return True

    def unload_req(self, req):
        # Delete new converter service(ros->zyre->ros)
        self.req.remove(req)
        return True

    def unload_res(self, res):
        # Delete new converter service(zyre->ros->zyre)
        self.res.remove(res)
        return True

    def load_topic(self, id):
        # Query robot id's info
        # Register all topic
        # Make new converter
        return True

    def load_service(self, id):
        # Query robot id's info
        # Register all topic
        # Make new converter
        return True

    def unload_topic(self, id):
        # Register all topic
        # Make new converter
        return True

    def unload_service(self, id):
        # Register all topic
        # Make new converter
        return True
