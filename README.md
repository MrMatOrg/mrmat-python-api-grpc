# MrMat :: Python :: API :: gRPC

[![Build](https://github.com/MrMatOrg/mrmat-python-api-grpc/actions/workflows/build.yml/badge.svg)](https://github.
com/MrMatOrg/mrmat-python-api-grpc/actions/workflows/build.yml)

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

## How to use this



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
