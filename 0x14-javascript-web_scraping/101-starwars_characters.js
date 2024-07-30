#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
}
async function fetchAndPrintCharacters() {
  try {
    const movieBody = await makeRequest(url);
    const movie = JSON.parse(movieBody);
    const characterUrls = movie.characters;

    for (const characterUrl of characterUrls) {
      const characterBody = await makeRequest(characterUrl);
      const character = JSON.parse(characterBody);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}
fetchAndPrintCharacters();
