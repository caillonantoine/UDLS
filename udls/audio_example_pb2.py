# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio_example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='audio_example.proto',
  package='audio_example',
  syntax='proto2',
  serialized_pb=_b('\n\x13\x61udio_example.proto\x12\raudio_example\"\xdd\x04\n\x0c\x41udioExample\x12\x39\n\x07\x62uffers\x18\x01 \x03(\x0b\x32(.audio_example.AudioExample.BuffersEntry\x12;\n\x08metadata\x18\x02 \x03(\x0b\x32).audio_example.AudioExample.MetadataEntry\x1a\xf5\x01\n\x0b\x41udioBuffer\x12\r\n\x05shape\x18\x01 \x03(\x05\x12\x15\n\rsampling_rate\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x38\n\tprecision\x18\x04 \x01(\x0e\x32%.audio_example.AudioExample.Precision\x12G\n\x08metadata\x18\x05 \x03(\x0b\x32\x35.audio_example.AudioExample.AudioBuffer.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aW\n\x0c\x42uffersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.audio_example.AudioExample.AudioBuffer:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\tPrecision\x12\x0b\n\x07\x46LOAT16\x10\x00\x12\x0b\n\x07\x46LOAT32\x10\x01\x12\x0b\n\x07\x46LOAT64\x10\x02\x12\t\n\x05INT16\x10\x03\x12\t\n\x05INT32\x10\x04\x12\t\n\x05INT64\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_AUDIOEXAMPLE_PRECISION = _descriptor.EnumDescriptor(
  name='Precision',
  full_name='audio_example.AudioExample.Precision',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOAT16', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT32', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT64', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT16', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=561,
  serialized_end=644,
)
_sym_db.RegisterEnumDescriptor(_AUDIOEXAMPLE_PRECISION)


_AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='audio_example.AudioExample.AudioBuffer.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='audio_example.AudioExample.AudioBuffer.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='audio_example.AudioExample.AudioBuffer.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=421,
)

_AUDIOEXAMPLE_AUDIOBUFFER = _descriptor.Descriptor(
  name='AudioBuffer',
  full_name='audio_example.AudioExample.AudioBuffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='audio_example.AudioExample.AudioBuffer.shape', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sampling_rate', full_name='audio_example.AudioExample.AudioBuffer.sampling_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='audio_example.AudioExample.AudioBuffer.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='audio_example.AudioExample.AudioBuffer.precision', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='audio_example.AudioExample.AudioBuffer.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=421,
)

_AUDIOEXAMPLE_BUFFERSENTRY = _descriptor.Descriptor(
  name='BuffersEntry',
  full_name='audio_example.AudioExample.BuffersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='audio_example.AudioExample.BuffersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='audio_example.AudioExample.BuffersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=510,
)

_AUDIOEXAMPLE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='audio_example.AudioExample.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='audio_example.AudioExample.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='audio_example.AudioExample.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=421,
)

_AUDIOEXAMPLE = _descriptor.Descriptor(
  name='AudioExample',
  full_name='audio_example.AudioExample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffers', full_name='audio_example.AudioExample.buffers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='audio_example.AudioExample.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_AUDIOEXAMPLE_AUDIOBUFFER, _AUDIOEXAMPLE_BUFFERSENTRY, _AUDIOEXAMPLE_METADATAENTRY, ],
  enum_types=[
    _AUDIOEXAMPLE_PRECISION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=644,
)

_AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY.containing_type = _AUDIOEXAMPLE_AUDIOBUFFER
_AUDIOEXAMPLE_AUDIOBUFFER.fields_by_name['precision'].enum_type = _AUDIOEXAMPLE_PRECISION
_AUDIOEXAMPLE_AUDIOBUFFER.fields_by_name['metadata'].message_type = _AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY
_AUDIOEXAMPLE_AUDIOBUFFER.containing_type = _AUDIOEXAMPLE
_AUDIOEXAMPLE_BUFFERSENTRY.fields_by_name['value'].message_type = _AUDIOEXAMPLE_AUDIOBUFFER
_AUDIOEXAMPLE_BUFFERSENTRY.containing_type = _AUDIOEXAMPLE
_AUDIOEXAMPLE_METADATAENTRY.containing_type = _AUDIOEXAMPLE
_AUDIOEXAMPLE.fields_by_name['buffers'].message_type = _AUDIOEXAMPLE_BUFFERSENTRY
_AUDIOEXAMPLE.fields_by_name['metadata'].message_type = _AUDIOEXAMPLE_METADATAENTRY
_AUDIOEXAMPLE_PRECISION.containing_type = _AUDIOEXAMPLE
DESCRIPTOR.message_types_by_name['AudioExample'] = _AUDIOEXAMPLE

AudioExample = _reflection.GeneratedProtocolMessageType('AudioExample', (_message.Message,), dict(

  AudioBuffer = _reflection.GeneratedProtocolMessageType('AudioBuffer', (_message.Message,), dict(

    MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
      DESCRIPTOR = _AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY,
      __module__ = 'audio_example_pb2'
      # @@protoc_insertion_point(class_scope:audio_example.AudioExample.AudioBuffer.MetadataEntry)
      ))
    ,
    DESCRIPTOR = _AUDIOEXAMPLE_AUDIOBUFFER,
    __module__ = 'audio_example_pb2'
    # @@protoc_insertion_point(class_scope:audio_example.AudioExample.AudioBuffer)
    ))
  ,

  BuffersEntry = _reflection.GeneratedProtocolMessageType('BuffersEntry', (_message.Message,), dict(
    DESCRIPTOR = _AUDIOEXAMPLE_BUFFERSENTRY,
    __module__ = 'audio_example_pb2'
    # @@protoc_insertion_point(class_scope:audio_example.AudioExample.BuffersEntry)
    ))
  ,

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _AUDIOEXAMPLE_METADATAENTRY,
    __module__ = 'audio_example_pb2'
    # @@protoc_insertion_point(class_scope:audio_example.AudioExample.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _AUDIOEXAMPLE,
  __module__ = 'audio_example_pb2'
  # @@protoc_insertion_point(class_scope:audio_example.AudioExample)
  ))
_sym_db.RegisterMessage(AudioExample)
_sym_db.RegisterMessage(AudioExample.AudioBuffer)
_sym_db.RegisterMessage(AudioExample.AudioBuffer.MetadataEntry)
_sym_db.RegisterMessage(AudioExample.BuffersEntry)
_sym_db.RegisterMessage(AudioExample.MetadataEntry)


_AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY.has_options = True
_AUDIOEXAMPLE_AUDIOBUFFER_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_AUDIOEXAMPLE_BUFFERSENTRY.has_options = True
_AUDIOEXAMPLE_BUFFERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_AUDIOEXAMPLE_METADATAENTRY.has_options = True
_AUDIOEXAMPLE_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)