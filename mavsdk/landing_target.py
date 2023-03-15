# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import landing_target_pb2, landing_target_pb2_grpc
from enum import Enum


class PositionLocal:
    """
     Position type in sensor frame coordinates

     Parameters
     ----------
     x : float
          Coordinate of landing target

     y : float
          Coordinate of landing target

     z : float
          Coordinate of landing target

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
            
        
        


class LandingTargetResult:
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
         Possible results returned for LandingTarget publish requests.

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
            if self == LandingTargetResult.Result.UNKNOWN:
                return landing_target_pb2.LandingTargetResult.RESULT_UNKNOWN
            if self == LandingTargetResult.Result.SUCCESS:
                return landing_target_pb2.LandingTargetResult.RESULT_SUCCESS
            if self == LandingTargetResult.Result.NO_SYSTEM:
                return landing_target_pb2.LandingTargetResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == landing_target_pb2.LandingTargetResult.RESULT_UNKNOWN:
                return LandingTargetResult.Result.UNKNOWN
            if rpc_enum_value == landing_target_pb2.LandingTargetResult.RESULT_SUCCESS:
                return LandingTargetResult.Result.SUCCESS
            if rpc_enum_value == landing_target_pb2.LandingTargetResult.RESULT_NO_SYSTEM:
                return LandingTargetResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the LandingTargetResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two LandingTargetResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LandingTargetResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ LandingTargetResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"LandingTargetResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLandingTargetResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return LandingTargetResult(
                
                LandingTargetResult.Result.translate_from_rpc(rpcLandingTargetResult.result),
                
                
                rpcLandingTargetResult.result_str
                )

    def translate_to_rpc(self, rpcLandingTargetResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcLandingTargetResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcLandingTargetResult.result_str = self.result_str
            
        
        



class LandingTargetError(Exception):
    """ Raised when a LandingTargetResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class LandingTarget(AsyncBase):
    """
     Allows developers to stream the position of a landing target for the drone to land on.

     Generated by dcsdkgen - MAVSDK LandingTarget API
    """

    # Plugin name
    name = "LandingTarget"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = landing_target_pb2_grpc.LandingTargetServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return LandingTargetResult.translate_from_rpc(response.landing_target_result)
    

    async def publish_position_relative(self, position_local):
        """
         Publish landing target measurement recorded by a sensor onboard the drone

         Parameters
         ----------
         position_local : PositionLocal
              The next landing position

         Raises
         ------
         LandingTargetError
             If the request fails. The error contains the reason for the failure.
        """

        request = landing_target_pb2.PublishPositionRelativeRequest()
        
        position_local.translate_to_rpc(request.position_local)
                
            
        response = await self._stub.PublishPositionRelative(request)

        
        result = self._extract_result(response)

        if result.result != LandingTargetResult.Result.SUCCESS:
            raise LandingTargetError(result, "publish_position_relative()", position_local)
        