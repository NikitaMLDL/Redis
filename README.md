<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Project Description</h1>

<h2>backend.py</h2>
<p>This file implements a simple FastAPI application that interacts with a Redis database.</p>
<ul>
    <li><strong>Initialization:</strong> It initializes a FastAPI app.</li>
    <li>
        <strong>User Check Endpoint:</strong>
        The <code>/check_user/{user_id}</code> endpoint takes a user ID as input and checks if it exists in the Redis database. It connects to Redis with SSL, retrieves user data using a pipeline for efficiency, and returns the count of the user (or 0 if the user doesn't exist).
    </li>
    <li>
        <strong>Server Setup:</strong>
        If the script is run directly, it starts a local server on <code>127.0.0.1:8080</code> using Uvicorn.
    </li>
</ul>

<h2>main.py</h2>
<p>This file uses Flask and Flask-Restful to create a RESTful API to manage user profiles.</p>
<ul>
    <li><strong>Initialization:</strong> It initializes a Flask app and establishes a connection to Redis.</li>
    <li>
        <strong>UserProfile Resource:</strong> This resource allows:
        <ul>
            <li><strong>POST:</strong> Create a new user profile if it doesn't exist.</li>
            <li><strong>PUT:</strong> Update an existing user profile.</li>
            <li><strong>DELETE:</strong> Remove a user profile if it exists.</li>
        </ul>
    </li>
    <li>
        <strong>AdminActions Resource:</strong> Provides endpoints for:
        <ul>
            <li><strong>GET:</strong> Retrieve all user profiles.</li>
            <li><strong>DELETE:</strong> Clear the database of all user profiles.</li>
        </ul>
    </li>
    <li><strong>Endpoint Registration:</strong> The resources are added to the API with specific routes.</li>
</ul>

<h2>main_redis.py</h2>
<p>This file creates a Telegram bot that interacts with users and manages their profiles stored in Redis.</p>
<ul>
    <li><strong>Bot Initialization:</strong> A Telegram bot is set up using a token (which is expected to be provided).</li>
    <li>
        <strong>User Profile Management:</strong>
        <ul>
            <li><code>/start:</code> Welcomes the user and prompts for creating a profile.</li>
            <li><code>/create:</code> Prompts the user to enter their name and age to create a profile.</li>
            <li><code>/update:</code> Allows users to update their profile with a new name and age.</li>
            <li><code>/delete:</code> Deletes the user's profile if it exists.</li>
        </ul>
    </li>
    <li>
        <strong>Admin Commands:</strong> Provides admin functionalities to view all user profiles or delete them with ease.
    </li>
    <li>
        <strong>Error Handling:</strong> Catches Redis connection errors and prints appropriate messages if an exception occurs.
    </li>
</ul>

<h2>Overall Description</h2>
<p>This project demonstrates how to create a user management system using a combination of FastAPI, Flask, Redis, and a Telegram bot. It supports CRUD operations for user profiles while also providing admin functionalities for managing the information stored in Redis. 🚀✨</p>

</body>
</html>
