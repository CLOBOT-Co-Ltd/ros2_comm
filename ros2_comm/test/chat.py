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

from _zyre_ctypes import *
from _czmq_ctypes import *

zsys = Zsys()
zstr = Zstr()

# Define the chat_actor function callback


def chat_actor(pipe, args):
    node = Zyre(c_char_p(args))
    if not node:
        return  # Could not create new node

    zsys.info(b"Create Zyre node, uuid=%s, name=%s", node.uuid(), node.name())
    node.start()
    node.join(b"CHAT")

    zsock = Zsock(pipe, True)
    zsock.signal(0)   # Signal "ready" to caller

    terminated = False
    poller = Zpoller(pipe, node.socket(), None)
    while not terminated:
        which = poller.wait(-1)
        if which == pipe:
            print("1111")
            msg = Zmsg.recv(which)

            if not msg:
                break   # Interrupted

            command = msg.popstr()
            if command == b"$TERM":
                terminated = True
            elif command == b"SHOUT":
                string = msg.popstr()
                node.shouts(b"CHAT", "%s", string)
            else:
                zsys.info(b"E: invalid message to actor")
                assert False

        elif which == node.socket():
            msg = Zmsg.recv(which)
            print(msg.size())
            event = msg.popstr()
            print(event)
            peer = msg.popstr()
            print(peer)
            name = msg.popstr()
            print(name)
            # group = msg.popstr()
            # print(group)
            # message = msg.popstr()
            # print(message)
            print("3333")
            if event == b"ENTER":
                zsys.info(b"%s has joined the chat", name)
            elif event == b"EXIT":
                zsys.info(b"%s has left the chat", name)
            elif event == b"SHOUT":
                ...
                # zsys.info(b"%s: %s", name, message)
            elif event == b"EVASIVE":
                zsys.info(b"%s is being evasive", name)
            elif event == b"SILENT":
                zsys.info(b"%s is being silent", name)

    node.stop()
    zclock = Zclock()
    zclock.sleep(100)


def main():
    import sys

    if len(sys.argv) < 2:
        print("syntax: ./chat myname")
        return

    actor = Zactor(zactor_fn(chat_actor), sys.argv[1].encode())
    assert actor

    while not zsys.is_interrupted():
        message = input().rstrip('\n')
        zstr.sendx(actor, b"SHOUT", message, None)


if __name__ == "__main__":
    main()
