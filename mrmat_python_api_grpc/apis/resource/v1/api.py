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
Implementation of the Resource API over gRPC
"""

import typing
from mrmat_python_api_grpc import mrmat_grpc, mrmat_grpc_model


class ResourceV1API(mrmat_grpc.ResourceV1ProtoServicer):
    """
    Implementation of the Resource API over gRPC
    """

    _resources: typing.List[mrmat_grpc_model.ResourceV1]

    def __init__(self):
        self._resources = []

    def List(self, request, context):   # pylint: disable=W0613
        return mrmat_grpc_model.ResourcesV1(
            status=mrmat_grpc_model.StatusOutput(code=200, message='OK'),
            resources=self._resources)

    def Get(self, request: mrmat_grpc_model.ResourceV1IdInput, context): # pylint: disable=W0613
        resource = list(filter(lambda _: _.id == request.id, self._resources))
        if resource and len(resource) > 0:
            return mrmat_grpc_model.ResourceV1Output(
                status=mrmat_grpc_model.StatusOutput(code=200, message='OK'),
                resource=resource[0])
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=404, message='Not Found'))

    def Create(self, request: mrmat_grpc_model.ResourceV1, context):  # pylint: disable=W0613
        request.id = len(self._resources)
        self._resources.append(request)
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=201, message='Created'),
            resource=request)

    def Modify(self, request: mrmat_grpc_model.ResourceV1, context):  # pylint: disable=W0613
        resource = list(filter(lambda _: _.id == request.id, self._resources))
        if not resource or len(resource) != 1:
            return mrmat_grpc_model.ResourceV1Output(
                status=mrmat_grpc_model.StatusOutput(code=404, message='Not Found'))
        resource[0].name = request.name
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=200, message='OK'),
            resource=resource[0])

    def Remove(self, request: mrmat_grpc_model.ResourceV1, context):  # pylint: disable=W0613
        resource = list(filter(lambda _: _.id == request.id, self._resources))
        if not resource or len(resource) != 1:
            return mrmat_grpc_model.StatusOutput(code=410, message='Gone')
        self._resources.remove(resource[0])
        return mrmat_grpc_model.StatusOutput(code=401, message='Removed')
