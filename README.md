# AI Embedded Music Recommender

This project utilizes cosine similarity between music tracks and recommends tracks to the user after receiving input from the user.
The webpage consists of ReactJS, Flask, and PostgreSql server. 
The data used is from the [FreeMusicArchive](https://github.com/mdeff/fma)), and is analyzed and prepared using Jupyter notebooks.

## Polished Music Data
Jupyter notebooks for compressing and cleaning up the music data are kept in notebooks/ 

## Postgresql Server

Scripts regarding setting up the server can be found in flaskProject/db

## Backend

Backend is setup in Python and Flask, files used are flaskProject/app.py and flaskProject/fetch_results.py


## Frontend

Frontend consists of serveral js class files in src/: App.js, Home.js, index.js, BasicRecommendResult.js, UserForm.js 