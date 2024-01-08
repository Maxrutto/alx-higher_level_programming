#!/usr/bin/node
const a = Math.floor(Number(process.argv[2]));
const b = Math.floor(Number(process.argv[3]));
function add (a, b) {
  const c = a + b;
  console.log(c);
}
add(a, b);
