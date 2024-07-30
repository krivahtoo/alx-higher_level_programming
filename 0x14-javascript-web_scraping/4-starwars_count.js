#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    for (const film in data.results) {
      if (film.characters && film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});
