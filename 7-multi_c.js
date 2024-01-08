#!/usr/bin/node
let x;
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num) || process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
