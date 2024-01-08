#!/usr/bin/node

const myArray = process.argv;

const arrayLength = myArray.length;

if (arrayLength === 2) {
  console.log('No Argument');
} else if (arrayLength === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
