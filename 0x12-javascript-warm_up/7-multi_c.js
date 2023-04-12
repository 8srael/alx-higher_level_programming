#!/usr/bin/node

const arg = process.argv[2];

const num = parseInt(arg);

if (!Number.isNaN(num)) {
  for (let i = 0 ; i < num ; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
