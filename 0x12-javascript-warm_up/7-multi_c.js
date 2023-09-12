#!/usr/bin/node
if (process.argv[2]) {
  const x = parseInt(process.argv[2]);

  if (x > 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
