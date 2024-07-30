#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function fetchCharacterName (characterUrl, callback) {
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      callback(null);
    } else {
      const character = JSON.parse(body);
      callback(character.name);
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;
      let completedRequests = 0;
      const characterNames = new Array(characterUrls.length);

      characterUrls.forEach((characterUrl, index) => {
        fetchCharacterName(characterUrl, (name) => {
          characterNames[index] = name;
          completedRequests++;

          if (completedRequests === characterUrls.length) {
            characterNames.forEach(name => {
              if (name) console.log(name);
            });
          }
        });
      });
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
