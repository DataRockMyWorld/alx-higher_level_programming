#!/usr/bin/node

const myArray = process.argv;
const arrayLength = myArray.length;

if (arrayLength < 3) {
  console.log(0);
  process.exit(1);
}
if (arrayLength === 3) {
  console.log(0);
  process.exit(1);
}

const sorted = myArray.sort(function (a, b) {
  return a - b;
});

console.log(sorted[arrayLength - 2]);
