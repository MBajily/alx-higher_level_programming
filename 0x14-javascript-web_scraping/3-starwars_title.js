#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
