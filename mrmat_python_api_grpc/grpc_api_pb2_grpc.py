# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import grpc_api_pb2 as grpc__api__pb2


class GreetingV1ProtoStub(object):
    """
    GreetingV1 API

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGreeting = channel.unary_unary(
                '/GreetingV1Proto/GetGreeting',
                request_serializer=grpc__api__pb2.GreetingV1Input.SerializeToString,
                response_deserializer=grpc__api__pb2.GreetingV1Output.FromString,
                )


class GreetingV1ProtoServicer(object):
    """
    GreetingV1 API

    """

    def GetGreeting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingV1ProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGreeting': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGreeting,
                    request_deserializer=grpc__api__pb2.GreetingV1Input.FromString,
                    response_serializer=grpc__api__pb2.GreetingV1Output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GreetingV1Proto', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingV1Proto(object):
    """
    GreetingV1 API

    """

    @staticmethod
    def GetGreeting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GreetingV1Proto/GetGreeting',
            grpc__api__pb2.GreetingV1Input.SerializeToString,
            grpc__api__pb2.GreetingV1Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class GreetingV2ProtoStub(object):
    """
    GreetingV2 API

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGreeting = channel.unary_unary(
                '/GreetingV2Proto/GetGreeting',
                request_serializer=grpc__api__pb2.GreetingV2Input.SerializeToString,
                response_deserializer=grpc__api__pb2.GreetingV2Output.FromString,
                )


class GreetingV2ProtoServicer(object):
    """
    GreetingV2 API

    """

    def GetGreeting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingV2ProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGreeting': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGreeting,
                    request_deserializer=grpc__api__pb2.GreetingV2Input.FromString,
                    response_serializer=grpc__api__pb2.GreetingV2Output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GreetingV2Proto', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingV2Proto(object):
    """
    GreetingV2 API

    """

    @staticmethod
    def GetGreeting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GreetingV2Proto/GetGreeting',
            grpc__api__pb2.GreetingV2Input.SerializeToString,
            grpc__api__pb2.GreetingV2Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class HealthzProtoStub(object):
    """
    Healthz API

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHealth = channel.unary_unary(
                '/HealthzProto/GetHealth',
                request_serializer=grpc__api__pb2.HealthzInput.SerializeToString,
                response_deserializer=grpc__api__pb2.StatusOutput.FromString,
                )


class HealthzProtoServicer(object):
    """
    Healthz API

    """

    def GetHealth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthzProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHealth': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHealth,
                    request_deserializer=grpc__api__pb2.HealthzInput.FromString,
                    response_serializer=grpc__api__pb2.StatusOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'HealthzProto', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HealthzProto(object):
    """
    Healthz API

    """

    @staticmethod
    def GetHealth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/HealthzProto/GetHealth',
            grpc__api__pb2.HealthzInput.SerializeToString,
            grpc__api__pb2.StatusOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ResourceV1ProtoStub(object):
    """
    Resource API

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/ResourceV1Proto/List',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=grpc__api__pb2.ResourcesV1.FromString,
                )
        self.Get = channel.unary_unary(
                '/ResourceV1Proto/Get',
                request_serializer=grpc__api__pb2.ResourceV1IdInput.SerializeToString,
                response_deserializer=grpc__api__pb2.ResourceV1Output.FromString,
                )
        self.Create = channel.unary_unary(
                '/ResourceV1Proto/Create',
                request_serializer=grpc__api__pb2.ResourceV1.SerializeToString,
                response_deserializer=grpc__api__pb2.ResourceV1Output.FromString,
                )
        self.Modify = channel.unary_unary(
                '/ResourceV1Proto/Modify',
                request_serializer=grpc__api__pb2.ResourceV1.SerializeToString,
                response_deserializer=grpc__api__pb2.ResourceV1Output.FromString,
                )
        self.Remove = channel.unary_unary(
                '/ResourceV1Proto/Remove',
                request_serializer=grpc__api__pb2.ResourceV1IdInput.SerializeToString,
                response_deserializer=grpc__api__pb2.StatusOutput.FromString,
                )


class ResourceV1ProtoServicer(object):
    """
    Resource API

    """

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Modify(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceV1ProtoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=grpc__api__pb2.ResourcesV1.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=grpc__api__pb2.ResourceV1IdInput.FromString,
                    response_serializer=grpc__api__pb2.ResourceV1Output.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=grpc__api__pb2.ResourceV1.FromString,
                    response_serializer=grpc__api__pb2.ResourceV1Output.SerializeToString,
            ),
            'Modify': grpc.unary_unary_rpc_method_handler(
                    servicer.Modify,
                    request_deserializer=grpc__api__pb2.ResourceV1.FromString,
                    response_serializer=grpc__api__pb2.ResourceV1Output.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=grpc__api__pb2.ResourceV1IdInput.FromString,
                    response_serializer=grpc__api__pb2.StatusOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ResourceV1Proto', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ResourceV1Proto(object):
    """
    Resource API

    """

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ResourceV1Proto/List',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            grpc__api__pb2.ResourcesV1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ResourceV1Proto/Get',
            grpc__api__pb2.ResourceV1IdInput.SerializeToString,
            grpc__api__pb2.ResourceV1Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ResourceV1Proto/Create',
            grpc__api__pb2.ResourceV1.SerializeToString,
            grpc__api__pb2.ResourceV1Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Modify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ResourceV1Proto/Modify',
            grpc__api__pb2.ResourceV1.SerializeToString,
            grpc__api__pb2.ResourceV1Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ResourceV1Proto/Remove',
            grpc__api__pb2.ResourceV1IdInput.SerializeToString,
            grpc__api__pb2.StatusOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
