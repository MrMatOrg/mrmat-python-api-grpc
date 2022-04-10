#  MIT License
#
#  Copyright (c) 2022 Mathieu Imfeld
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

"""
Implementation of the client for the demonstration APIs
"""

import sys
import argparse

import grpc

from mrmat_python_api_grpc import __version__, mrmat_grpc, mrmat_grpc_model


def greeting_v1(channel, args: argparse.Namespace) -> int:      # pylint: disable=unused-argument
    stub = mrmat_grpc.GreetingV1ProtoStub(channel)
    greeting = stub.GetGreeting(mrmat_grpc_model.GreetingV1Input())
    print(greeting.message)
    return 0


def greeting_v2(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.GreetingV2ProtoStub(channel)
    greeting = stub.GetGreeting(mrmat_grpc_model.GreetingV2Input(name=args.name))
    print(greeting.message)
    return 0


def healthz(channel, args: argparse.Namespace) -> int:          # pylint: disable=unused-argument
    stub = mrmat_grpc.HealthzProtoStub(channel)
    health = stub.GetHealth(mrmat_grpc_model.HealthzInput())
    print(f'[{health.code}] {health.message}')
    return 0


def resource_v1_list(channel, args: argparse.Namespace) -> int:     # pylint: disable=unused-argument
    stub = mrmat_grpc.ResourceV1ProtoStub(channel)
    response = stub.List(mrmat_grpc_model.google_dot_protobuf_dot_empty__pb2.Empty())
    print(f'[{response.status.code}] {response.status.message}')
    print('Resources:')
    for resource in response.resources:
        print(f'- id: {resource.id}, owner_id: {resource.owner_id}, name: {resource.name}')
    return 0


def resource_v1_get(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.ResourceV1ProtoStub(channel)
    response = stub.Get(mrmat_grpc_model.ResourceV1IdInput(id=args.id))
    print(f'[{response.status.code}] {response.status.message}')
    if response.status.code == 200:
        resource = response.resource
        print(f'- id: {resource.id}, owner_id: {resource.owner_id}, name: {resource.name}')
    return 0


def resource_v1_create(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.ResourceV1ProtoStub(channel)
    response = stub.Create(mrmat_grpc_model.ResourceV1(owner_id=args.owner_id,
                                                       name=args.name))
    print(f'[{response.status.code}] {response.status.message}')
    return 0


def resource_v1_modify(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.ResourceV1ProtoStub(channel)
    response = stub.Modify(mrmat_grpc_model.ResourceV1(id=args.id,
                                                       owner_id=args.owner_id,
                                                       name=args.name))
    print(f'[{response.status.code}] {response.status.message}')
    return 0


def resource_v1_remove(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.ResourceV1ProtoStub(channel)
    response = stub.Remove(mrmat_grpc_model.ResourceV1IdInput(id=args.id))
    print(f'[{response.code}] {response.message}')
    return 0


def main():
    parser = argparse.ArgumentParser(description=f'mrmat-python-api-grpc - {__version__}')
    subparsers = parser.add_subparsers(dest='group')

    greeting_parser = subparsers.add_parser(name='greeting', help='Be greeted')
    greeting_subparser = greeting_parser.add_subparsers()
    greeting_v1_parser = greeting_subparser.add_parser(name='v1', help='Get a generic greeting')
    greeting_v1_parser.set_defaults(cmd=greeting_v1)
    greeting_v2_parser = greeting_subparser.add_parser(name='v2', help='Get a customisable greeting')
    greeting_v2_parser.set_defaults(cmd=greeting_v2)
    greeting_v2_parser.add_argument('--name', '-n',
                                    type=str,
                                    dest='name',
                                    required=False,
                                    default='Stranger',
                                    help='The name to greet')

    healthz_parser = subparsers.add_parser(name='healthz')
    healthz_parser.set_defaults(cmd=healthz)

    resource_parser = subparsers.add_parser(name='resource', help='Resource related commands')
    resource_subparser = resource_parser.add_subparsers()
    resource_v1_parser = resource_subparser.add_parser(name='v1', help='Resource v1 commands')
    resource_v1_subparser = resource_v1_parser.add_subparsers()
    resource_v1_list_parser = resource_v1_subparser.add_parser(name='list', help='List resources')
    resource_v1_list_parser.set_defaults(cmd=resource_v1_list)
    resource_v1_get_parser = resource_v1_subparser.add_parser(name='get', help='Get a resource')
    resource_v1_get_parser.set_defaults(cmd=resource_v1_get)
    resource_v1_get_parser.add_argument('--id',
                                        dest='id',
                                        type=int,
                                        required=True,
                                        help='Resource id')
    resource_v1_create_parser = resource_v1_subparser.add_parser(name='create', help='Create a resource')
    resource_v1_create_parser.set_defaults(cmd=resource_v1_create)
    resource_v1_create_parser.add_argument('--owner-id',
                                           dest='owner_id',
                                           type=int,
                                           required=True,
                                           help='Resource owner id')
    resource_v1_create_parser.add_argument('--name',
                                           dest='name',
                                           type=str,
                                           required=True,
                                           help='Resource name')
    resource_v1_modify_parser = resource_v1_subparser.add_parser(name='modify', help='Modify a resource')
    resource_v1_modify_parser.set_defaults(cmd=resource_v1_modify)
    resource_v1_modify_parser.add_argument('--id',
                                           dest='id',
                                           type=int,
                                           required=True,
                                           help='Resource id')
    resource_v1_modify_parser.add_argument('--owner-id',
                                           dest='owner_id',
                                           type=int,
                                           required=True,
                                           help='Resource owner id')
    resource_v1_modify_parser.add_argument('--name',
                                           dest='name',
                                           type=str,
                                           required=True,
                                           help='Resource name')
    resource_v1_remove_parser = resource_v1_subparser.add_parser(name='remove', help='Remove a resource')
    resource_v1_remove_parser.set_defaults(cmd=resource_v1_remove)
    resource_v1_remove_parser.add_argument('--id',
                                           dest='id',
                                           type=int,
                                           required=True,
                                           help='Resource id')

    args = parser.parse_args()

    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            if hasattr(args, 'cmd'):
                return args.cmd(channel, args)
            elif hasattr(args, 'group'):
                subparser = subparsers.choices.get(args.group)
                subparser.print_help() if subparser else parser.print_help()    # pylint: disable=W0106
            else:
                parser.print_help()
    except Exception as e:      # pylint: disable=broad-except
        print(f'Exception {e} occurred')
    return 1


if __name__ == '__main__':
    sys.exit(main())
