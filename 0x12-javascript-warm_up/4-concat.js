#!/usr/bin/node

const myArray = process.argv;
const arrayLength = myArray.length;

if (arrayLength === 2) {
  console.log('undefined is undefined');
} else if (arrayLength === 3) {
  console.log(myArray[2] + ' is undefined');
} else {
  console.log(myArray[2] + ' is' + ' ' + myArray[3]);
}
