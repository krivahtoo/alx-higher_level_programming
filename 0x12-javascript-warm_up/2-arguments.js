#!/usr/bin/node
const count = process.argv.length;
if (count > 2) {
  console.log('Arguments found');
} else if (count === 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
