#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const arr = [];
      for (let j = 0; j < this.width; j++) {
        arr.push('X');
      }
      console.log(`${arr.join('')}`);
    }
  }

  rotate () {
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

export default Rectangle;
