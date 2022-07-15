from grpc_tools import protoc

protoc.main([
    'grpc_tools.protoc',
    '--python_out',
    'udls/generated',
    '--grpc_python_out',
    'udls/generated',
    'udls/interfaces/audio_example.proto',
])
