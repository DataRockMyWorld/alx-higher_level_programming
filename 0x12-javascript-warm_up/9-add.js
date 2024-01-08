#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const args = process.argv;
const arg1 = parseInt(args[2]);
const arg2 = parseInt(args[3]);

add(arg1, arg2);
