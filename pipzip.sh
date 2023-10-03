#!/bin/bash
echo "Package: $1"
zip -r downloaded_packages__$1.zip ./downloaded_packages
