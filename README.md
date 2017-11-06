# Development

```sh
# Install Python dependencies
pip install -r requirements.txt

# Install Elasticsearch
brew install elasticsearch

# Install Kibana, a visualization and debugging tool for Elasticsearch
brew install kibana
```

# Launch Elasticsearch/Kibana

```sh
# You can replace "start" with "stop" or "restart"
brew services start elasticsearch

# Similarly, you can start Kibana using this
brew services start kibana
```

# Launch Web App

Remember to launch Elasticsearch before launching the web app

```
# Make sure the working directory is where `app.py` is located
FLASK_APP=./app.py flask run
```

