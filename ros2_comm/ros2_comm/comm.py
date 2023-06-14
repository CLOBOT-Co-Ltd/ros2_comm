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

import rclpy

from ros2_comm_msgs.srv import *
from data import CommData


class Comm(object):
    def __init__(self):
        self._node = rclpy.create_node("ros2_comm")

        id = "clober_0"
        type = "clober"
        groups = list()
        groups.append("CLOBOT")
        self._data = CommData(id, type, groups)

        self._info_srv = self._node.create_service(
            Info, "/ros2_comm/info", self._info_callback)

        self._info_id_srv = self._node.create_service(
            InfoId, "/ros2_comm/info/id", self._info_id_callback)

        self._info_list_srv = self._node.create_service(
            InfoList, "/ros2_comm/info/list", self._info_list_callback)

        self._list_group_srv = self._node.create_service(
            ListGroup, "/ros2_comm/list/group", self._list_group_callback)

        self._list_group_id_srv = self._node.create_service(
            ListGroupId, "/ros2_comm/list/group/id", self._list_group_id_callback)

        self._list_type_srv = self._node.create_service(
            ListType, "/ros2_comm/list/type", self._list_type_callback)

        self._list_group_id_srv = self._node.create_service(
            ListTypeId, "/ros2_comm/list/type/id", self._list_type_id_callback)

        self._add_id_srv = self._node.create_service(
            ControlId, "/ros2_comm/add/id", self._add_id_callback)

        self._add_id_all_srv = self._node.create_service(
            ControlIdAll, "/ros2_comm/add/id_all", self._add_id_all_callback)

        self._add_id_group_srv = self._node.create_service(
            ControlIdGroup, "/ros2_comm/add/id_group", self._add_id_group_callback)

        self._add_group_srv = self._node.create_service(
            ControlGroup, "/ros2_comm/add/group", self._add_group_callback)

        self._remove_id_srv = self._node.create_service(
            ControlId, "/ros2_comm/remove/id", self._remove_id_callback)

        self._remove_id_all_srv = self._node.create_service(
            ControlIdAll, "/ros2_comm/remove/id_all", self._remove_id_all_callback)

        self._remove_id_group_srv = self._node.create_service(
            ControlIdGroup, "/ros2_comm/remove/id_group", self._remove_id_group_callback)

        self._remove_group_srv = self._node.create_service(
            ControlGroup, "/ros2_comm/remove/group", self._remove_group_callback)

        self._set_type_srv = self._node.create_service(
            SetType, "/ros2_comm/set/type", self._set_type_callback)

        self._load_pub_srv = self._node.create_service(
            LoadPubTopic, "/ros2_comm/load/pub_topic", self._load_pub_callback)

        self._load_sub_srv = self._node.create_service(
            LoadSubTopic, "ros2_comm/load/sub_topic", self._load_sub_callback)

        self._load_req_srv = self._node.create_service(
            LoadReqService, "/ros2_comm/load/req_service", self._load_req_callback)

        self._load_res_sev = self._node.create_service(
            LoadResService, "/ros2_comm/load/res_service", self._load_res_callback)

        self._unload_pub_srv = self._node.create_service(
            LoadPubTopic, "/ros2_comm/unload/pub_topic", self._unload_pub_callback)

        self._unload_sub_srv = self._node.create_service(
            LoadSubTopic, "ros2_comm/unload/sub_topic", self._unload_sub_callback)

        self._unload_req_srv = self._node.create_service(
            LoadReqService, "/ros2_comm/unload/req_service", self._unload_req_callback)

        self._unload_res_sev = self._node.create_service(
            LoadResService, "/ros2_comm/unload/res_service", self._unload_res_callback)

        self._load_topic_srv = self._node.create_service(
            Load, "/ros2_comm/load/topic", self._load_topic_callback)

        self._load_service_srv = self._node.create_service(
            Load, "/ros2_comm/load/service", self._load_service_callback)

        self._unload_topic_srv = self._node.create_service(
            Load, "/ros2_comm/unload/topic", self._unload_topic_callback)

        self._unload_topic_srv = self._node.create_service(
            Load, "/ros2_comm/unload/topic", self._unload_topic_callback)

    def _info_callback(self, request, response):
        response.info = self._data.get_info()
        response.list = self._data.get_list()
        response.pub = self._data.get_pub()
        response.sub = self._data.get_sub()
        response.req = self._data.get_req()
        response.res = self._data.get_res()
        return response

    def _info_id_callback(self, request, response):
        response.info = self._data.get_info(request.id)
        response.pub = self._data.get_pub(request.id)
        response.res = self._data.get_res(request.id)
        return response

    def _info_list_callback(self, request, response):
        response.info = self._data.get_list(request.all)
        return response

    def _list_group_callback(self, request, response):
        response.group = self._data.get_group_list()
        return response

    def _list_group_id_callback(self, request, response):
        response.info = self._data.get_group_info(request -> group)
        return response

    def _list_type_callback(self, request, response):
        response.type = self._data.get_type_list()
        return response

    def _list_type_id_callback(self, request, response):
        response.info = self._data.get_type_info(request -> type)

    def _add_id_callback(self, request, response):
        response.ok = self._data.add_id(request.id)
        return response

    def _add_id_all_callback(self, request, response):
        response.ok = self._data.add_all_id_in_groups()
        return response

    def _add_id_group_callback(self, request, response):
        response.ok = self._data.add_id_in_group(request.group)
        return response

    def _add_group_callback(self, request, response):
        response.ok = self._data.add_group(request.group)
        return response

    def _remove_id_callback(self, request, response):
        response.ok = self._data.remove_id(request.id)
        return response

    def _remove_id_all_callback(self, request, response):
        response.ok = self._data.remove_all_id_in_groups()
        return response

    def _remove_id_group_callback(self, request, response):
        response.ok = self._data.remove_id_in_group(request.group)
        return response

    def _remove_group_callback(self, request, response):
        response.ok = self._data.remove_group(request.group)
        return response

    def _set_type_callback(self, request, response):
        response.ok = self._data.set_type(request.type)
        return True

    def _load_pub_callback(self, request, response):
        response.ok = self._data.load_pub(request.topic)
        return response

    def _load_sub_callback(self, request, response):
        response.ok = self._data.load_sub(request.topic)
        return response

    def _load_req_callback(self, request, response):
        response.ok = self._data.load_req(request.service)
        return response

    def _load_res_callback(self, request, response):
        response.ok = self._data.load_res(request.service)
        return response

    def _unload_pub_callback(self, request, response):
        response.ok = self._data.unload_pub(request.topic)
        return response

    def _unload_sub_callback(self, request, response):
        response.ok = self._data.unload_sub(request.topic)
        return response

    def _unload_req_callback(self, request, response):
        response.ok = self._data.unload_req(request.service)
        return response

    def _unload_res_callback(self, request, response):
        response.ok = self._data.unload_res(request.service)
        return response

    def _load_topic_callback(self, request, response):
        response.ok = self._data.load_topic(request.id)
        return response

    def _load_service_callback(self, request, response):
        response.ok = self._data.load_service(request.id)
        return response

    def _unload_topic_callback(self, request, response):
        response.ok = self._data.unload_topic(request.id)
        return response

    def _unload_topic_callback(self, request, response):
        response.ok = self._data.unload_service(request.id)
        return response

    @ property
    def node(self):
        return self._node
