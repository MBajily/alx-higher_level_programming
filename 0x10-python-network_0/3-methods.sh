#!/bin/bash
# Send HEAD request, extract and display the allowed HTTP methods
curl -sI "$1" | awk '/Allow/{print substr($0, index($0,$2))}'