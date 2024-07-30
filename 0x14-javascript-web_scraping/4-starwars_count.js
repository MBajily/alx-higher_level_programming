#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const films = JSON.parse(body).results;
      const count = films.reduce((acc, film) => {
        return acc + film.characters.filter(character => character.endsWith('/18/')).length;
      }, 0);
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
