# Installing Requirements

`python -m pip install --upgrade pip && pip install -r requirements.txt`

Updates pip and installs all the requirements from the requirements.txt file. Ensure you are running this from the project root directory.

# Updating Requirements

`pip freeze > requirements.txt`

Saves all the current project requirements to the requirements.txt file. Ensure you are running this from the project root directory.

# Running the bot

`https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=shnijmghvktm9mpvv9p2fdbm978sl5&redirect_uri=http://localhost:3000&scope=chat%3Aread+chat%3Aedit`

Grab the token from the url this redirects to
`http://localhost:3000/#access_token=[TOKEN]&scope=chat%3Aread+chat%3Aedit&token_type=bearer`

Rename the file sample_config.json to just 'config.json' and fill out the information properly, mainly the token in twitch is the most important at the moment.