#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const x = parseInt(process.argv[2]);

  if (x > 0) {
    for (let i = 0; i < x; i++) {
      const arr = [];
      for (let j = 0; j < x; j++) {
        arr.push('X');
      }
      console.log(`${arr.join('')}`);
    }
  }
} else {
  console.log('Missing size');
}
