# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import precision_target_pb2, precision_target_pb2_grpc
from enum import Enum


class ObservationFrame(Enum):
    """
     Target Observation Frame type.

     Values
     ------
     LOCAL_NED
          NED local tangent frame (x: North, y: East, z: Down) with origin fixed relative to earth.

     BODY_FRD
          FRD local frame aligned to the vehicle's attitude (x: Forward, y: Right, z: Down) with an origin that travels with vehicle.

     """

    
    LOCAL_NED = 0
    BODY_FRD = 1

    def translate_to_rpc(self):
        if self == ObservationFrame.LOCAL_NED:
            return precision_target_pb2.OBSERVATION_FRAME_LOCAL_NED
        if self == ObservationFrame.BODY_FRD:
            return precision_target_pb2.OBSERVATION_FRAME_BODY_FRD

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == precision_target_pb2.OBSERVATION_FRAME_LOCAL_NED:
            return ObservationFrame.LOCAL_NED
        if rpc_enum_value == precision_target_pb2.OBSERVATION_FRAME_BODY_FRD:
            return ObservationFrame.BODY_FRD

    def __str__(self):
        return self.name


class PositionLocal:
    """
     Position type in sensor frame coordinates

     Parameters
     ----------
     x : float
          Coordinate of precision target

     y : float
          Coordinate of precision target

     z : float
          Coordinate of precision target

     """

    

    def __init__(
            self,
            x,
            y,
            z):
        """ Initializes the PositionLocal object """
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, to_compare):
        """ Checks if two PositionLocal are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PositionLocal object
            return \
                (self.x == to_compare.x) and \
                (self.y == to_compare.y) and \
                (self.z == to_compare.z)

        except AttributeError:
            return False

    def __str__(self):
        """ PositionLocal in string representation """
        struct_repr = ", ".join([
                "x: " + str(self.x),
                "y: " + str(self.y),
                "z: " + str(self.z)
                ])

        return f"PositionLocal: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPositionLocal):
        """ Translates a gRPC struct to the SDK equivalent """
        return PositionLocal(
                
                rpcPositionLocal.x,
                
                
                rpcPositionLocal.y,
                
                
                rpcPositionLocal.z
                )

    def translate_to_rpc(self, rpcPositionLocal):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPositionLocal.x = self.x
            
        
        
        
            
        rpcPositionLocal.y = self.y
            
        
        
        
            
        rpcPositionLocal.z = self.z
            
        
        


class PrecisionTargetResult:
    """
     Result type.

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for PrecisionTarget publish requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Success

         NO_SYSTEM
              No system is connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2

        def translate_to_rpc(self):
            if self == PrecisionTargetResult.Result.UNKNOWN:
                return precision_target_pb2.PrecisionTargetResult.RESULT_UNKNOWN
            if self == PrecisionTargetResult.Result.SUCCESS:
                return precision_target_pb2.PrecisionTargetResult.RESULT_SUCCESS
            if self == PrecisionTargetResult.Result.NO_SYSTEM:
                return precision_target_pb2.PrecisionTargetResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == precision_target_pb2.PrecisionTargetResult.RESULT_UNKNOWN:
                return PrecisionTargetResult.Result.UNKNOWN
            if rpc_enum_value == precision_target_pb2.PrecisionTargetResult.RESULT_SUCCESS:
                return PrecisionTargetResult.Result.SUCCESS
            if rpc_enum_value == precision_target_pb2.PrecisionTargetResult.RESULT_NO_SYSTEM:
                return PrecisionTargetResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the PrecisionTargetResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two PrecisionTargetResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PrecisionTargetResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ PrecisionTargetResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"PrecisionTargetResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPrecisionTargetResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return PrecisionTargetResult(
                
                PrecisionTargetResult.Result.translate_from_rpc(rpcPrecisionTargetResult.result),
                
                
                rpcPrecisionTargetResult.result_str
                )

    def translate_to_rpc(self, rpcPrecisionTargetResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPrecisionTargetResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcPrecisionTargetResult.result_str = self.result_str
            
        
        



class PrecisionTargetError(Exception):
    """ Raised when a PrecisionTargetResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class PrecisionTarget(AsyncBase):
    """
     Allows developers to stream the position of a precision target for the drone to land on.

     Generated by dcsdkgen - MAVSDK PrecisionTarget API
    """

    # Plugin name
    name = "PrecisionTarget"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = precision_target_pb2_grpc.PrecisionTargetServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return PrecisionTargetResult.translate_from_rpc(response.precision_target_result)
    

    async def publish_position_relative(self, position_local, observation_frame):
        """
         Publish precision target measurement recorded by a sensor onboard the drone

         Parameters
         ----------
         position_local : PositionLocal
              The next precision target position

         observation_frame : ObservationFrame
              The coordinate frame of the local position

         Raises
         ------
         PrecisionTargetError
             If the request fails. The error contains the reason for the failure.
        """

        request = precision_target_pb2.PublishPositionRelativeRequest()
        
        position_local.translate_to_rpc(request.position_local)
                
            
        
        request.observation_frame = observation_frame.translate_to_rpc()
                
            
        response = await self._stub.PublishPositionRelative(request)

        
        result = self._extract_result(response)

        if result.result != PrecisionTargetResult.Result.SUCCESS:
            raise PrecisionTargetError(result, "publish_position_relative()", position_local, observation_frame)
        