#!/bin/bash
# Check if the URL argument is provide
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
