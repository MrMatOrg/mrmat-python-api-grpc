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

import sys
import argparse
import grpc

from mrmat_python_api_grpc import __version__, mrmat_grpc, mrmat_grpc_model


def greeting_v1(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.GreetingV1Stub(channel)
    greeting = stub.GetGreeting(mrmat_grpc_model.GreetingV1Input())
    print(greeting.message)
    return 0


def greeting_v2(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.GreetingV2Stub(channel)
    greeting = stub.GetGreeting(mrmat_grpc_model.GreetingV2Input(name=args.name))
    print(greeting.message)
    return 0


def healthz(channel, args: argparse.Namespace) -> int:
    stub = mrmat_grpc.HealthzStub(channel)
    health = stub.GetHealth(mrmat_grpc_model.HealthzInput())
    print(f'[{health.code}] {health.message}')
    return 0


def main():
    parser = argparse.ArgumentParser(description=f'mrmat-python-api-grpc - {__version__}')
    subparsers = parser.add_subparsers()

    greeting_v1_parser = subparsers.add_parser(name='greeting-v1')
    greeting_v1_parser.set_defaults(func=greeting_v1)

    greeting_v2_parser = subparsers.add_parser(name='greeting-v2')
    greeting_v2_parser.set_defaults(func=greeting_v2)
    greeting_v2_parser.add_argument('--name', '-n',
                                    type=str,
                                    dest='name',
                                    required=False,
                                    default='Stranger',
                                    help='The name to greet')

    healthz_parser = subparsers.add_parser(name='healthz')
    healthz_parser.set_defaults(func=healthz)

    resource_v1_parser = subparsers.add_parser(name='resource-v1')
    resource_v1_parser.set_defaults()

    args = parser.parse_args()

    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            return args.func(channel, args)
    except Exception as e:
        print(f'Exception {e} occurred')
        return 1


if __name__ == '__main__':
    sys.exit(main())
