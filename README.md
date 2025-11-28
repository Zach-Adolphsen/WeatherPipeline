# Weather Pipeline

A Python-based weather data pipeline that fetches weather forecast data from the OpenWeather API and stores it in a PostgreSQL database for analysis and tracking.

## Overview

This project retrieves weather forecast data for Fargo, ND using the OpenWeather API and persists the data to a PostgreSQL database. It's designed to be run periodically to build a historical dataset of weather forecasts.

## Features

- Fetches 5-day weather forecast data from OpenWeather API
- Stores weather data in PostgreSQL database
- Uses environment variables for secure configuration management
- Modular architecture with separate database and configuration modules

## Project Structure
WeatherPipeline/
├── src/ │ 
         ├── config.py # Configuration and environment variable management 
         └── database.py # Database connection and data insertion logic 
├── main.py # Main application entry point 
└── README.md # Project documentation

There are more files in the project that are not tracked by git
