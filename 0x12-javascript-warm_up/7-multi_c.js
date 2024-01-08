#!/usr/bin/node

const text = 'C is fun';
const myArray = process.argv;
let x = parseInt(myArray[2]);

if (!isNaN(x)) {
  while (x > 0) {
    console.log(text);
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
