#!/usr/bin/node

const args = process.argv;
const firstArgument = parseInt(args[2]);

if (!isNaN(firstArgument)) {
  console.log('My number:', firstArgument);
} else {
  console.log('Not a number');
}
