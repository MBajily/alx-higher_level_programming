#!/usr/bin/node
const fs = require('fs');
// Get the file path from command line arguments
const filePath = process.argv[2];
// Read the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred, print the error object
    console.log(err);
  } else {
    // If successful, print the content of the file
    console.log(data);
  }
});
