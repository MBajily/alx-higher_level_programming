#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
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
      const characterUrls = movie.characters;

      // Function to fetch and print character names
      const fetchCharacter = (url) => {
        request.get(url, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      };

      // Fetch and print each character
      characterUrls.forEach(fetchCharacter);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
