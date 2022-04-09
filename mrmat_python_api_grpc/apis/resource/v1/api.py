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

from typing import List
from mrmat_python_api_grpc import mrmat_grpc, mrmat_grpc_model


class ResourceV1API(mrmat_grpc.ResourceV1ProtoServicer):

    _resources: List[mrmat_grpc_model.ResourceV1]

    def __init__(self):
        self._resources = []

    def GetAll(self, request, context):
        return mrmat_grpc_model.ResourcesV1(
            status=mrmat_grpc_model.StatusOutput(code=200, message='OK'),
            resources=self._resources)

    def GetOne(self, request: mrmat_grpc_model.ResourceV1IdInput, context):
        resource = filter(lambda _: _.id == request.id, self._resources)
        if resource:
            return mrmat_grpc_model.ResourceV1Output(
                status=mrmat_grpc_model.StatusOutput(code=200, message='OK'),
                resource=resource)
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=404, message='Not Found'),
            resource=mrmat_grpc_model.ResourceV1())

    def Create(self, request: mrmat_grpc_model.ResourceV1, context):
        self._resources.append(request)
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=201, message='Created'),
            resource=request)

    def Modify(self, request: mrmat_grpc_model.ResourceV1, context):
        resource = filter(lambda _: _.id == request.id, self._resources)
        if not resource:
            return mrmat_grpc_model.ResourceV1Output(
                status=mrmat_grpc_model.StatusOutput(code=404, message='Not Found'),
                resource=mrmat_grpc_model.ResourceV1())
        resource.name = request.name
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=200, message='OK'),
            resource=resource)

    def Remove(self, request: mrmat_grpc_model.ResourceV1, context):
        resource = filter(lambda _: _.id == request.id, self._resources)
        if not resource:
            return mrmat_grpc_model.ResourceV1Output(
                status=mrmat_grpc_model.StatusOutput(code=410, message='Gone'),
                resource=mrmat_grpc_model.ResourceV1())
        return mrmat_grpc_model.ResourceV1Output(
            status=mrmat_grpc_model.StatusOutput(code=401, message='Removed'),
            resource=mrmat_grpc_model.ResourceV1())
