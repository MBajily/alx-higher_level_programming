#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const arg = Number(process.argv[2]);
  let rep = 0;
  while (rep < arg) {
    console.log('X'.repeat(arg));
    rep++;
  }
}
