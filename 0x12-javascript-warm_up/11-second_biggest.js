#!/usr/bin/node
// searches the second biggest integer in the list of arguments.
if (process.argv.length > 3) {
  let i = 2
  let big = process.argv[i]
  for (; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i]);
    if (num > big) {
      big = num;
    }
  }
  console.log(big);
} else {
  console.log(0);
}
