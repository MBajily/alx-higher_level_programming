#!/usr/bin/node

const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If an error occurred, print the error object
    console.log(err);
  }
});
