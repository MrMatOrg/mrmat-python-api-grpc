
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
from concurrent import futures
import grpc

from mrmat_python_api_grpc.apis.greeting.v1 import GreetingV1Api
from mrmat_python_api_grpc.apis.greeting.v2 import GreetingV2Api
from mrmat_python_api_grpc.apis.healthz import HealthzAPI
from mrmat_python_api_grpc.apis.resource.v1 import ResourceV1API
from mrmat_python_api_grpc import mrmat_grpc


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mrmat_grpc.add_GreetingV1Servicer_to_server(GreetingV1Api(), server)
    mrmat_grpc.add_GreetingV2Servicer_to_server(GreetingV2Api(), server)
    mrmat_grpc.add_HealthzServicer_to_server(HealthzAPI(), server)
    mrmat_grpc.add_ResourceV1ProtocolServicer_to_server(ResourceV1API(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print('Waiting for connection...')
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print('Shutting down...')
    return 0


if __name__ == '__main__':
    sys.exit(main())
