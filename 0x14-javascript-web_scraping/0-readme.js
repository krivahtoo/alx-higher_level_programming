#!/usr/bin/node

const { readFileSync } = require('fs');

try {
  console.log(readFileSync(process.argv[2]).toString());
} catch (e) {
  console.error(e);
}
