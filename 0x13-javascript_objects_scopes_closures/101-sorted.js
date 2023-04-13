#!/usr/bin/node

const dict = require('./101-data').dict;

const dictArr = Object.entries(dict);
const values = Object.values(dict);
const uValues = values.filter((elt, i, arr) => arr.indexOf(elt) === i);
const newDict = {};
for (const x of uValues) {
  const list = [];
  for (const y in dictArr) {
    if (dictArr[y][1] === x) {
      list.unshift(dictArr[y][0]);
    }
  }

  newDict[x] = list;
}

console.log(newDict);
