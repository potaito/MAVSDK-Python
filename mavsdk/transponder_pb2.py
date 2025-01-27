# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transponder/transponder.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transponder/transponder.proto',
  package='mavsdk.rpc.transponder',
  syntax='proto3',
  serialized_options=b'\n\025io.mavsdk.transponderB\020TransponderProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dtransponder/transponder.proto\x12\x16mavsdk.rpc.transponder\x1a\x14mavsdk_options.proto\"\x1d\n\x1bSubscribeTransponderRequest\"O\n\x13TransponderResponse\x12\x38\n\x0btransponder\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.transponder.AdsbVehicle\",\n\x19SetRateTransponderRequest\x12\x0f\n\x07rate_hz\x18\x01 \x01(\x01\"c\n\x1aSetRateTransponderResponse\x12\x45\n\x12transponder_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.transponder.TransponderResult\"\xa3\x02\n\x0b\x41\x64sbVehicle\x12\x14\n\x0cicao_address\x18\x01 \x01(\r\x12\x14\n\x0clatitude_deg\x18\x02 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x03 \x01(\x01\x12\x1b\n\x13\x61\x62solute_altitude_m\x18\x05 \x01(\x02\x12\x13\n\x0bheading_deg\x18\x06 \x01(\x02\x12\x1f\n\x17horizontal_velocity_m_s\x18\x07 \x01(\x02\x12\x1d\n\x15vertical_velocity_m_s\x18\x08 \x01(\x02\x12\x10\n\x08\x63\x61llsign\x18\t \x01(\t\x12=\n\x0c\x65mitter_type\x18\n \x01(\x0e\x32\'.mavsdk.rpc.transponder.AdsbEmitterType\x12\x0e\n\x06squawk\x18\r \x01(\r\"\x8f\x02\n\x11TransponderResult\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.mavsdk.rpc.transponder.TransponderResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xa3\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06*\xad\x05\n\x0f\x41\x64sbEmitterType\x12\x1d\n\x19\x41\x44SB_EMITTER_TYPE_NO_INFO\x10\x00\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_LIGHT\x10\x01\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_SMALL\x10\x02\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_LARGE\x10\x03\x12\'\n#ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE\x10\x04\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_HEAVY\x10\x05\x12\"\n\x1e\x41\x44SB_EMITTER_TYPE_HIGHLY_MANUV\x10\x06\x12\x1f\n\x1b\x41\x44SB_EMITTER_TYPE_ROTOCRAFT\x10\x07\x12 \n\x1c\x41\x44SB_EMITTER_TYPE_UNASSIGNED\x10\x08\x12\x1c\n\x18\x41\x44SB_EMITTER_TYPE_GLIDER\x10\t\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_LIGHTER_AIR\x10\n\x12\x1f\n\x1b\x41\x44SB_EMITTER_TYPE_PARACHUTE\x10\x0b\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_ULTRA_LIGHT\x10\x0c\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_UNASSIGNED2\x10\r\x12\x19\n\x15\x41\x44SB_EMITTER_TYPE_UAV\x10\x0e\x12\x1b\n\x17\x41\x44SB_EMITTER_TYPE_SPACE\x10\x0f\x12!\n\x1d\x41\x44SB_EMITTER_TYPE_UNASSGINED3\x10\x10\x12\'\n#ADSB_EMITTER_TYPE_EMERGENCY_SURFACE\x10\x11\x12%\n!ADSB_EMITTER_TYPE_SERVICE_SURFACE\x10\x12\x12$\n ADSB_EMITTER_TYPE_POINT_OBSTACLE\x10\x13\x32\x91\x02\n\x12TransponderService\x12|\n\x14SubscribeTransponder\x12\x33.mavsdk.rpc.transponder.SubscribeTransponderRequest\x1a+.mavsdk.rpc.transponder.TransponderResponse\"\x00\x30\x01\x12}\n\x12SetRateTransponder\x12\x31.mavsdk.rpc.transponder.SetRateTransponderRequest\x1a\x32.mavsdk.rpc.transponder.SetRateTransponderResponse\"\x00\x42)\n\x15io.mavsdk.transponderB\x10TransponderProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])

_ADSBEMITTERTYPE = _descriptor.EnumDescriptor(
  name='AdsbEmitterType',
  full_name='mavsdk.rpc.transponder.AdsbEmitterType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_NO_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_LIGHT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_SMALL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_LARGE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_HEAVY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_HIGHLY_MANUV', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_ROTOCRAFT', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_UNASSIGNED', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_GLIDER', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_LIGHTER_AIR', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_PARACHUTE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_ULTRA_LIGHT', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_UNASSIGNED2', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_UAV', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_SPACE', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_UNASSGINED3', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_EMERGENCY_SURFACE', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_SERVICE_SURFACE', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADSB_EMITTER_TYPE_POINT_OBSTACLE', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=907,
  serialized_end=1592,
)
_sym_db.RegisterEnumDescriptor(_ADSBEMITTERTYPE)

AdsbEmitterType = enum_type_wrapper.EnumTypeWrapper(_ADSBEMITTERTYPE)
ADSB_EMITTER_TYPE_NO_INFO = 0
ADSB_EMITTER_TYPE_LIGHT = 1
ADSB_EMITTER_TYPE_SMALL = 2
ADSB_EMITTER_TYPE_LARGE = 3
ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE = 4
ADSB_EMITTER_TYPE_HEAVY = 5
ADSB_EMITTER_TYPE_HIGHLY_MANUV = 6
ADSB_EMITTER_TYPE_ROTOCRAFT = 7
ADSB_EMITTER_TYPE_UNASSIGNED = 8
ADSB_EMITTER_TYPE_GLIDER = 9
ADSB_EMITTER_TYPE_LIGHTER_AIR = 10
ADSB_EMITTER_TYPE_PARACHUTE = 11
ADSB_EMITTER_TYPE_ULTRA_LIGHT = 12
ADSB_EMITTER_TYPE_UNASSIGNED2 = 13
ADSB_EMITTER_TYPE_UAV = 14
ADSB_EMITTER_TYPE_SPACE = 15
ADSB_EMITTER_TYPE_UNASSGINED3 = 16
ADSB_EMITTER_TYPE_EMERGENCY_SURFACE = 17
ADSB_EMITTER_TYPE_SERVICE_SURFACE = 18
ADSB_EMITTER_TYPE_POINT_OBSTACLE = 19


_TRANSPONDERRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.transponder.TransponderResult.Result',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_BUSY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_COMMAND_DENIED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=741,
  serialized_end=904,
)
_sym_db.RegisterEnumDescriptor(_TRANSPONDERRESULT_RESULT)


_SUBSCRIBETRANSPONDERREQUEST = _descriptor.Descriptor(
  name='SubscribeTransponderRequest',
  full_name='mavsdk.rpc.transponder.SubscribeTransponderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=108,
)


_TRANSPONDERRESPONSE = _descriptor.Descriptor(
  name='TransponderResponse',
  full_name='mavsdk.rpc.transponder.TransponderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transponder', full_name='mavsdk.rpc.transponder.TransponderResponse.transponder', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=189,
)


_SETRATETRANSPONDERREQUEST = _descriptor.Descriptor(
  name='SetRateTransponderRequest',
  full_name='mavsdk.rpc.transponder.SetRateTransponderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate_hz', full_name='mavsdk.rpc.transponder.SetRateTransponderRequest.rate_hz', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=235,
)


_SETRATETRANSPONDERRESPONSE = _descriptor.Descriptor(
  name='SetRateTransponderResponse',
  full_name='mavsdk.rpc.transponder.SetRateTransponderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transponder_result', full_name='mavsdk.rpc.transponder.SetRateTransponderResponse.transponder_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=336,
)


_ADSBVEHICLE = _descriptor.Descriptor(
  name='AdsbVehicle',
  full_name='mavsdk.rpc.transponder.AdsbVehicle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='icao_address', full_name='mavsdk.rpc.transponder.AdsbVehicle.icao_address', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude_deg', full_name='mavsdk.rpc.transponder.AdsbVehicle.latitude_deg', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude_deg', full_name='mavsdk.rpc.transponder.AdsbVehicle.longitude_deg', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='absolute_altitude_m', full_name='mavsdk.rpc.transponder.AdsbVehicle.absolute_altitude_m', index=3,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading_deg', full_name='mavsdk.rpc.transponder.AdsbVehicle.heading_deg', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='horizontal_velocity_m_s', full_name='mavsdk.rpc.transponder.AdsbVehicle.horizontal_velocity_m_s', index=5,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vertical_velocity_m_s', full_name='mavsdk.rpc.transponder.AdsbVehicle.vertical_velocity_m_s', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='callsign', full_name='mavsdk.rpc.transponder.AdsbVehicle.callsign', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='emitter_type', full_name='mavsdk.rpc.transponder.AdsbVehicle.emitter_type', index=8,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='squawk', full_name='mavsdk.rpc.transponder.AdsbVehicle.squawk', index=9,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=630,
)


_TRANSPONDERRESULT = _descriptor.Descriptor(
  name='TransponderResult',
  full_name='mavsdk.rpc.transponder.TransponderResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.transponder.TransponderResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.transponder.TransponderResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSPONDERRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=904,
)

_TRANSPONDERRESPONSE.fields_by_name['transponder'].message_type = _ADSBVEHICLE
_SETRATETRANSPONDERRESPONSE.fields_by_name['transponder_result'].message_type = _TRANSPONDERRESULT
_ADSBVEHICLE.fields_by_name['emitter_type'].enum_type = _ADSBEMITTERTYPE
_TRANSPONDERRESULT.fields_by_name['result'].enum_type = _TRANSPONDERRESULT_RESULT
_TRANSPONDERRESULT_RESULT.containing_type = _TRANSPONDERRESULT
DESCRIPTOR.message_types_by_name['SubscribeTransponderRequest'] = _SUBSCRIBETRANSPONDERREQUEST
DESCRIPTOR.message_types_by_name['TransponderResponse'] = _TRANSPONDERRESPONSE
DESCRIPTOR.message_types_by_name['SetRateTransponderRequest'] = _SETRATETRANSPONDERREQUEST
DESCRIPTOR.message_types_by_name['SetRateTransponderResponse'] = _SETRATETRANSPONDERRESPONSE
DESCRIPTOR.message_types_by_name['AdsbVehicle'] = _ADSBVEHICLE
DESCRIPTOR.message_types_by_name['TransponderResult'] = _TRANSPONDERRESULT
DESCRIPTOR.enum_types_by_name['AdsbEmitterType'] = _ADSBEMITTERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeTransponderRequest = _reflection.GeneratedProtocolMessageType('SubscribeTransponderRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBETRANSPONDERREQUEST,
  '__module__' : 'transponder.transponder_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.transponder.SubscribeTransponderRequest)
  })
_sym_db.RegisterMessage(SubscribeTransponderRequest)

TransponderResponse = _reflection.GeneratedProtocolMessageType('TransponderResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSPONDERRESPONSE,
  '__module__' : 'transponder.transponder_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.transponder.TransponderResponse)
  })
_sym_db.RegisterMessage(TransponderResponse)

SetRateTransponderRequest = _reflection.GeneratedProtocolMessageType('SetRateTransponderRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETRATETRANSPONDERREQUEST,
  '__module__' : 'transponder.transponder_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.transponder.SetRateTransponderRequest)
  })
_sym_db.RegisterMessage(SetRateTransponderRequest)

SetRateTransponderResponse = _reflection.GeneratedProtocolMessageType('SetRateTransponderResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETRATETRANSPONDERRESPONSE,
  '__module__' : 'transponder.transponder_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.transponder.SetRateTransponderResponse)
  })
_sym_db.RegisterMessage(SetRateTransponderResponse)

AdsbVehicle = _reflection.GeneratedProtocolMessageType('AdsbVehicle', (_message.Message,), {
  'DESCRIPTOR' : _ADSBVEHICLE,
  '__module__' : 'transponder.transponder_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.transponder.AdsbVehicle)
  })
_sym_db.RegisterMessage(AdsbVehicle)

TransponderResult = _reflection.GeneratedProtocolMessageType('TransponderResult', (_message.Message,), {
  'DESCRIPTOR' : _TRANSPONDERRESULT,
  '__module__' : 'transponder.transponder_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.transponder.TransponderResult)
  })
_sym_db.RegisterMessage(TransponderResult)


DESCRIPTOR._options = None

_TRANSPONDERSERVICE = _descriptor.ServiceDescriptor(
  name='TransponderService',
  full_name='mavsdk.rpc.transponder.TransponderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1595,
  serialized_end=1868,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeTransponder',
    full_name='mavsdk.rpc.transponder.TransponderService.SubscribeTransponder',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBETRANSPONDERREQUEST,
    output_type=_TRANSPONDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetRateTransponder',
    full_name='mavsdk.rpc.transponder.TransponderService.SetRateTransponder',
    index=1,
    containing_service=None,
    input_type=_SETRATETRANSPONDERREQUEST,
    output_type=_SETRATETRANSPONDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSPONDERSERVICE)

DESCRIPTOR.services_by_name['TransponderService'] = _TRANSPONDERSERVICE

# @@protoc_insertion_point(module_scope)
