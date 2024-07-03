#!/usr/bin/node
let arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  arg = 1;
}

function factorial (i) {
  if (i === 1) {
    return 1;
  }
  return i * factorial(i - 1);
}

console.log(factorial(arg));
