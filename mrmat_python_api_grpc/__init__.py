#  MIT License
#
#  Copyright (c) 2022 Mathieu Imfeld
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

"""
Main entry point for the mrmat_python_api_grpc package
"""

import os
import importlib.metadata

import mrmat_python_api_grpc.grpc_api_pb2_grpc as mrmat_grpc
import mrmat_python_api_grpc.grpc_api_pb2 as mrmat_grpc_model

#
# Determine the version we're at and a version header we add to each response

try:
    __version__ = importlib.metadata.version('mrmat-python-api-grpc')
except importlib.metadata.PackageNotFoundError:
    # You have not actually installed the wheel yet. We may be within CI so pick that version or fall back
    __version__ = os.environ.get('MRMAT_VERSION', '0.0.0.dev0')
