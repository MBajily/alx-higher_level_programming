#!/bin/bash
# takes URL as an argument, sends GET request to URL
curl -sH "X-School-User-Id: 98" "${1}"
