#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
function factorial (n) {
  if (n === 1 || isNaN(n) === true) {
    return (1);
  }
  return (n * (factorial(n - 1)));
}
console.log(factorial(n));
