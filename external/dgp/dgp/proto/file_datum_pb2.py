# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgp/proto/file_datum.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dgp/proto/file_datum.proto',
  package='dgp.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x64gp/proto/file_datum.proto\x12\tdgp.proto\x1a\x19google/protobuf/any.proto\"\xc8\x01\n\tFileDatum\x12,\n\x05\x64\x61tum\x18\x01 \x01(\x0b\x32\x1d.dgp.proto.SelfDescribingFile\x12:\n\x0b\x61nnotations\x18\x02 \x03(\x0b\x32%.dgp.proto.FileDatum.AnnotationsEntry\x1aQ\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.dgp.proto.SelfDescribingFile:\x02\x38\x01\"L\n\x12SelfDescribingFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12$\n\x06schema\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_FILEDATUM_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='dgp.proto.FileDatum.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dgp.proto.FileDatum.AnnotationsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dgp.proto.FileDatum.AnnotationsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=269,
)

_FILEDATUM = _descriptor.Descriptor(
  name='FileDatum',
  full_name='dgp.proto.FileDatum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datum', full_name='dgp.proto.FileDatum.datum', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='dgp.proto.FileDatum.annotations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FILEDATUM_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=269,
)


_SELFDESCRIBINGFILE = _descriptor.Descriptor(
  name='SelfDescribingFile',
  full_name='dgp.proto.SelfDescribingFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='dgp.proto.SelfDescribingFile.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='dgp.proto.SelfDescribingFile.schema', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=271,
  serialized_end=347,
)

_FILEDATUM_ANNOTATIONSENTRY.fields_by_name['value'].message_type = _SELFDESCRIBINGFILE
_FILEDATUM_ANNOTATIONSENTRY.containing_type = _FILEDATUM
_FILEDATUM.fields_by_name['datum'].message_type = _SELFDESCRIBINGFILE
_FILEDATUM.fields_by_name['annotations'].message_type = _FILEDATUM_ANNOTATIONSENTRY
_SELFDESCRIBINGFILE.fields_by_name['schema'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['FileDatum'] = _FILEDATUM
DESCRIPTOR.message_types_by_name['SelfDescribingFile'] = _SELFDESCRIBINGFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileDatum = _reflection.GeneratedProtocolMessageType('FileDatum', (_message.Message,), {

  'AnnotationsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FILEDATUM_ANNOTATIONSENTRY,
    '__module__' : 'dgp.proto.file_datum_pb2'
    # @@protoc_insertion_point(class_scope:dgp.proto.FileDatum.AnnotationsEntry)
    })
  ,
  'DESCRIPTOR' : _FILEDATUM,
  '__module__' : 'dgp.proto.file_datum_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.FileDatum)
  })
_sym_db.RegisterMessage(FileDatum)
_sym_db.RegisterMessage(FileDatum.AnnotationsEntry)

SelfDescribingFile = _reflection.GeneratedProtocolMessageType('SelfDescribingFile', (_message.Message,), {
  'DESCRIPTOR' : _SELFDESCRIBINGFILE,
  '__module__' : 'dgp.proto.file_datum_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.SelfDescribingFile)
  })
_sym_db.RegisterMessage(SelfDescribingFile)


_FILEDATUM_ANNOTATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
