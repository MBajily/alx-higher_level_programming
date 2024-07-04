#!/bin/bash
# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "URL argument is missing."
  exit 1
fi

# Set the POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with the parameters
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$1") 

# Display the body of the response
echo "$response"
