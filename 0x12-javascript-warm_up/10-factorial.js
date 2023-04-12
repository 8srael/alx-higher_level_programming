#!/usr/bin/node

function factoriel (x) {
  if (x === 0 || Number.isNaN(x)) {
    return 1;
  } else {
    return x * factoriel(x - 1);
  }
}

const argNum = parseInt(process.argv[2]);
console.log(factoriel(argNum));
