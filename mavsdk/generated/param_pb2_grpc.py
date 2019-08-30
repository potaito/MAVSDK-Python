# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import param_pb2 as param__pb2


class ParamServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetIntParam = channel.unary_unary(
        '/mavsdk.rpc.param.ParamService/GetIntParam',
        request_serializer=param__pb2.GetIntParamRequest.SerializeToString,
        response_deserializer=param__pb2.GetIntParamResponse.FromString,
        )
    self.SetIntParam = channel.unary_unary(
        '/mavsdk.rpc.param.ParamService/SetIntParam',
        request_serializer=param__pb2.SetIntParamRequest.SerializeToString,
        response_deserializer=param__pb2.SetIntParamResponse.FromString,
        )
    self.GetFloatParam = channel.unary_unary(
        '/mavsdk.rpc.param.ParamService/GetFloatParam',
        request_serializer=param__pb2.GetFloatParamRequest.SerializeToString,
        response_deserializer=param__pb2.GetFloatParamResponse.FromString,
        )
    self.SetFloatParam = channel.unary_unary(
        '/mavsdk.rpc.param.ParamService/SetFloatParam',
        request_serializer=param__pb2.SetFloatParamRequest.SerializeToString,
        response_deserializer=param__pb2.SetFloatParamResponse.FromString,
        )


class ParamServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetIntParam(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetIntParam(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFloatParam(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetFloatParam(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ParamServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetIntParam': grpc.unary_unary_rpc_method_handler(
          servicer.GetIntParam,
          request_deserializer=param__pb2.GetIntParamRequest.FromString,
          response_serializer=param__pb2.GetIntParamResponse.SerializeToString,
      ),
      'SetIntParam': grpc.unary_unary_rpc_method_handler(
          servicer.SetIntParam,
          request_deserializer=param__pb2.SetIntParamRequest.FromString,
          response_serializer=param__pb2.SetIntParamResponse.SerializeToString,
      ),
      'GetFloatParam': grpc.unary_unary_rpc_method_handler(
          servicer.GetFloatParam,
          request_deserializer=param__pb2.GetFloatParamRequest.FromString,
          response_serializer=param__pb2.GetFloatParamResponse.SerializeToString,
      ),
      'SetFloatParam': grpc.unary_unary_rpc_method_handler(
          servicer.SetFloatParam,
          request_deserializer=param__pb2.SetFloatParamRequest.FromString,
          response_serializer=param__pb2.SetFloatParamResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mavsdk.rpc.param.ParamService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))