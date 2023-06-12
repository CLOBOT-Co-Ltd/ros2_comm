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

import argparse

from _zyre_ctypes import *
from _czmq_ctypes import *


def main():
    parser = argparse.ArgumentParser(
        description='zpinger - ping other peers in a ZRE network')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='verbose test output')
    parser.add_argument('--interface', '-i', help='use this interface')
    parser.add_argument('--ipv6', '-6', action='store_true', help='use IPv6')
    parser.add_argument('--curve', '-c', action='store_true',
                        help='use CURVE encryption')
    parser.add_argument('--name', '-n', help='zyre name')
    parser.add_argument(
        '--group', '-g', help='zyre group')

    args = parser.parse_args()

    zsys = Zsys()
    zsys.set_ipv6(args.ipv6)

    zyre = Zyre(None)

    if args.verbose:
        zyre.set_verbose()
    if args.interface:
        zyre.set_interface(args.interface)

    zyre.start()
    group = ""

    if args.group:
        group = args.group.encode()
    else:
        group = b"GLOBAL"

    if args.name:
        zyre.set_name(args.name.encode())
        zyre.set_header(b"ID", args.name.encode())

    zsys.info(b"Create Zyre node, uuid=%s, name=%s", zyre.uuid(), zyre.name())
    zyre.set_header(b"TYPE", b"0")

    zyre.join(group)

    if args.verbose:
        zyre.print()

    while True:
        event = ZyreEvent(zyre)
        if not event:
            break
        if args.verbose:
            event.print()

        if event.type() == b"ENTER":
            # If new peer, say hello to it and wait for it to answer us
            zsys.info(b"[%s] peer entered", event.peer_name())
            zyre.whispers(event.peer_uuid(), b"Hello")

        elif event.type() == b"EXIT":
            zsys.info(b"[%s] peer exited", event.peer_name())

        elif event.type() == b"WHISPER":
            zsys.info(b"[%s] received ping (WHISPER)", event.peer_name())
            zyre.shouts(group, b"Hello")

        elif event.type() == b"SHOUT":
            zsys.info(b"[%s](%s) received ping (SHOUT)",
                      event.peer_name(), event.group())

        ######################## check peer ########################
        # Return zlist of current peer ids.
        # Caller owns return value and must destroy it when done.
        ############################################################
        # peers = zyre.peers()
        # for i in range(peers.size()):
        #     print(ctypes.cast(peers.first(), ctypes.c_char_p).value.decode())
        #     peers.pop()

        #################### check peer in group ###################
        # Return zlist of current peers of this group.
        # Caller owns return value and must destroy it when done.
        ############################################################
        # peers_in_group = Zlist()
        # peers_in_group.append(zyre.peers_by_group(group))
        # if peers_in_group.size() == 0:  # Check the peers_in_group's size
        #     continue
        # peers_in_group = zyre.peers_by_group(group)
        # for i in range(peers_in_group.size()):
        #     print(ctypes.cast(peers_in_group.first(),
        #           ctypes.c_char_p).value.decode())
        #     peers_in_group.pop()

        ######################## own groups ########################
        # Return zlist of currently joined groups.
        # Caller owns return value and must destroy it when done.
        ############################################################
        # own_groups = zyre.own_groups()
        # for i in range(own_groups.size()):
        #     print(ctypes.cast(own_groups.first(), ctypes.c_char_p).value.decode())
        #     own_groups.pop()

        ######################## peer groups #######################
        # Return zlist of groups known through connected peers.
        # Caller owns return value and must destroy it when done.
        ############################################################
        # peer_groups = zyre.peer_groups()
        # for i in range(peer_groups.size()):
        #     print(ctypes.cast(peer_groups.first(), ctypes.c_char_p).value.decode())
        #     peer_groups.pop()

        ####################### peer address #######################
        # Return the endpoint of a connected peer.
        # Returns empty string if peer does not exist.
        # Caller owns return value and must destroy it when done.
        ############################################################
        # peers = zyre.peers()
        # for i in range(peers.size()):
        #     peer = ctypes.cast(peers.first(), ctypes.c_char_p).value
        #     address = zyre.peer_address(peer)
        #     print(address)
        #     peers.pop()

        #################### peer_header_value #####################
        # Return the value of a header of a conected peer.
        # Returns null if peer or key doesn't exits.
        # Caller owns return value and must destroy it when done.
        ############################################################
        # peers = zyre.peers()
        # for i in range(peers.size()):
        #     peer = ctypes.cast(peers.first(), ctypes.c_char_p).value
        #     id = zyre.peer_header_value(peer, b"ID")
        #     type = zyre.peer_header_value(peer, b"TYPE")
        #     print(id)
        #     print(type)
        #     peers.pop()


if __name__ == "__main__":
    main()
