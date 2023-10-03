#!/bin/bash
echo "Package: $1";
pip download --dest ./downloaded_packages --only-binary=:all: --python-version 3.8.9 --platform win_amd64 $1
