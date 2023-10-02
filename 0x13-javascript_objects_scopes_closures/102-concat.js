#!/usr/bin/node
const fs = require('fs').promises;
const { argv } = require('process');

const a = argv[2];
const b = argv[3];
const c = argv[4];

async function concatTwoFiles () {
  try {
    const dataA = await fs.readFile(a);
    const dataB = await fs.readFile(b);
    fs.writeFile(c, dataA + dataB);
  } catch (err) {
    console.log(err);
  }
}

concatTwoFiles();
