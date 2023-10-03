#!/bin/bash
echo "Package: $1";
pip download --dest ./downloaded_packages --prefer-binary $1
