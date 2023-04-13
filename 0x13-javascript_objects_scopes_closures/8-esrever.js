#!/usr/bin/node

exports.esrever = function (list) {
  const tsil = [];
  for (let i = 0; i < list.length; i++) {
    tsil[i] = list[list.length - (i + 1)];
  }

  return tsil;
};
