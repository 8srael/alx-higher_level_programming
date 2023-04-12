#!/usr/bin/node

const SecondSquare = require('./5-square');

class Square extends SecondSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let ch = '';
        for (let j = 0; j < this.width; j++) {
          ch += c;
        }
        console.log(ch);
      }
    }
  }
}

module.exports = Square;
