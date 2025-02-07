* Named Entity Recognition with spaCy

The python app `app.py` accepts a POST request with a string and returns an array of named ORGs from the string. The app is enabled by the Flask library and is set up to run on AWS AppRunner.

The pyton app `local-app.py` is the 'original' version of the app that can be run locally on macOS. It uses a more accurate model that cannot be run on AWS AppRunner due to resource constraints.
