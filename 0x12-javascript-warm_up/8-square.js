#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!Number.isNaN(num)) {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
