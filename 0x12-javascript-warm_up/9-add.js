#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

if (process.argv.length === 2) {
  console.log(Number.NaN);
} else {
  console.log(add(x, y));
}
