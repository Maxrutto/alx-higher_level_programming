#!/usr/bin/node

if (typeof process.argv[2] === 'undefined') {
  console.log('No argument');
}
console.log(process.argv[2]);
