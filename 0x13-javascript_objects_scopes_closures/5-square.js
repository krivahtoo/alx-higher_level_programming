#!/usr/bin/node
import Rectangle from './4-rectangle';

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      const arr = [];
      for (let j = 0; j < this.width; j++) {
        arr.push(c || 'X');
      }
      console.log(`${arr.join('')}`);
    }
  }
}

export default Square;
