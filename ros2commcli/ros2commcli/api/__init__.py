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

# from ros2cli.node.direct import DirectNode

# class LoadCompleter:  
#     def __call__(self, prefix, pasred_args, **kwargs):
#         with DirectNode(pasred_args) as node:
#             return ["TEST1", "TEST2"]

def test_completer(**kwargs):
    return ["TEST1", "TEST2"]

def test_select_completer(key=None):
    if key == "id":
        return ["ID1", "ID2"]
    elif key == "type":
        return ["Type1", "Type2"]
    elif key == "group":
        return ["Group1", "Group2"]
    elif key == None:
        return ["NONE"]
    
    return ["TEST"]

class SelectCompleter:
    def __init__(self, *, key=None):
        self.key = key

    def __call__(self, prefix, parsed_args, **kwargs):
        get_key = getattr(parsed_args, self.key)
        if get_key == "id":
            return ["ID1", "ID2"]
        elif get_key == "type":
            return ["Type1", "Type2"]
        elif get_key == "group":
            return ["Group1", "Group2"]
        elif get_key == None:
            return ["NONE"]
        
        if self.key == 'topic_name':
            return ["TopicType1", "TopicType2"]
        
        if self.key == 'publisher':
            return ["Topic1", "Topic2"]
        
        if self.key == 'service_name':
            return ["ServiceType1", "ServiceType2"]
        
        if self.key == 'server':
            return ["Service1", "Service2"]
        
        return [get_key]