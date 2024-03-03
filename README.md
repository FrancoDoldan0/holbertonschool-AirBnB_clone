<p align="center">
  <img src="https://i.ibb.co/tbz1c9T/logo.png" alt="logo" border="0">
</p>

<h1 align="center">AirBnB clone - The console
</h1>

## Description

This repository serves as the starting point for a student project aimed at creating a replica of the AirBnB website. At this initial stage, there exists a backend interface, referred to as the console, which facilitates the management of program data. The console commands empower users to create, update, and delete objects, as well as handle file storage. Through the utilization of JSON serialization/deserialization, the storage remains persistent across sessions.

## Directory Structure

The project is structured as follows:

- `console.py`: This is the main file for the command interpreter of the console component.
- `models/engine/`: Inside this directory, you'll find the `file_storage.py` file, responsible for handling the serialization and deserialization of objects to and from JSON files.
- `models/`: This directory holds the classes like `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.
- `tests/`: Here lie the unit tests for the application.

## Testing 

Tests for the Holberton AirBnB project are located in the `tests` folder. 

To run all the tests together, use this command:

```bash
$ python3 unittest -m discover tests






