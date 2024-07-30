#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to make a request and return a promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
}

// Main function to fetch and print character names
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

// Call the main function
fetchAndPrintCharacters();
