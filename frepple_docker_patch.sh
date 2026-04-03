#!/bin/bash
# Build step 1: Install system deps + Python deps
# (already done in existing image layer)

# Build step 2: Build C++ solver from source
cd /workspace/build || (mkdir -p /workspace/build && cd /workspace/build && cmake ..)
make -j$(nproc)
make install

# Build step 3: Install freppledb Python package
cd /workspace
pip3 install --break-system-packages -e .
