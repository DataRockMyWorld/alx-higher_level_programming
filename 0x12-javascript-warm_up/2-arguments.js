#!/usr/bin/node

const myArray = process.argv;

const arrayLength = myArray.length;

if (arrayLength === 2) {
  console.log('No argument');
} else if (arrayLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
