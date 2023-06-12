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

import sys
import signal
import rclpy
from rclpy.executors import MultiThreadedExecutor

from ros2_comm.comm import Comm

SIGNALS_TO_HANDLE = [signal.SIGINT, signal.SIGTERM]


def _signal_handler(signal, frame):

    rclpy.shutdown()
    sys.exit()


def register_signals(signals):
    for sig in signals:
        signal.signal(sig, _signal_handler)


def main():
    register_signals(SIGNALS_TO_HANDLE)

    rclpy.init()
    executor = MultiThreadedExecutor()

    comm = Comm()

    executor.add_node(comm.node)
    executor.spin()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
