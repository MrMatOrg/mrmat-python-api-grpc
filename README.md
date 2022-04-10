# MrMat :: Python :: API :: gRPC

[![Build](https://github.com/MrMatOrg/mrmat-python-api-grpc/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-api-grpc/actions/workflows/build.yml)

Boilerplate for a gRPC Python API.

## How to build this

We use the [PEP517 build mechanism](https://www.python.org/dev/peps/pep-0517/) and build a wheel as follows:

```bash
$ pip install -r requirements.txt        # Manually install dependencies (see note in requirements.txt!)
$ export PYTHONPATH=`pwd`                # In order to find the build-time ci module
$ export MRMAT_VERSION=1.0.27            # Optional: To influence the version. Normally calculated and set by CI
$ python -m build -n --wheel             # Use -n in an interactive, virtual environment
... lots of output omitted
$ ls dist/
mrmat_python_api_grpc-1.0.27.dev0-py3-none-any.whl
```

### If you need to update the protocol

The protobuf definition is located in the `var/proto/` directory. You can edit the single file currently
there or add new ones. If you add new files, you can import them as we import Googles Empty message, but
you must adjust the command to contain all files containing prototypes below and/or the includes via the
-I option.

```
python -m grpc_tools.protoc \
    -Ivar/proto \
    --python_out=mrmat_python_api_grpc/ \
    --grpc_python_out=mrmat_python_api_grpc/ \
    grpc-api.proto
```

This will update two Python files `mrmat_python_api_grpc/grpc_api_pb2.py` and 
`mrmat_python_api_grpc/grpc_api_pb2_grpc.py`. It is quite annoying that the package option is ignored by the 
protobuf Python compiler because **you must update the latter with the Python package in which they are stored**. I 
currently fail to understand how you would otherwise produce a wheel that can be installed somewhere. These files 
somehow expect to be freestanding.

One could technically argue that its acceptable for just slight modifications of these generated files, but then 
really it's not. You'll forget. Tears will flow. I wish they just allowed us to specify the package for Python as well.

## How to use this

You'll get two executables when you install this:

* mrmat-python-api-grpc-server
* mrmat-python-api-grpc-client

Start the server, it will listen on localhost:50051. Run help on the client, you'll see.

## How this works

gRPC is an interesting alternative to REST when speed counts. A typical example where one might well
consider gRPC over REST is for consuming a central service for validating authentication tokens. Doing
so may reduce complexity within the consuming apps. It is critical, however, to secure the communication
path over which gRPC is made. Google offers ALTS for this (similar to mTLS) but the evaluation in here has not 
progressed far enough to make a statement on this. Alternatives may be Consul or similar secure path
injections by a ServiceMesh.

It may be particularly interesting to use the bi-directional streaming functionality offered by gRPC for
this use-case, since it saves costly handshakes at runtime and instead goes over a persistent open channel.
Provided security and integrity between the two partners can be maintained and that it offers resiliency
when the channel goes down it becomes a very interesting option to do so.
