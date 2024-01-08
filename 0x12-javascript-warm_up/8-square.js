#!/usr/bin/node
let x;
let y;
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num) || process.argv.length < 3) {
  console.log('Missing size');
} else {
  for (y = 0; y < num; y++) {
    let row = '';
    for (x = 0; x < num; x++) {
      row += 'x';
    }
    console.log(row);
  }
}
