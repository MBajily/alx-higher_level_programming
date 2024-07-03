#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];

function add (a, b) {
  return a + b;
}

console.log(add(parseInt(first), parseInt(second)));
