# Sublime Plugin Client-Server Demo

This repo provides a proof of concept for running a Sublime Text plugin as a client-server architecture.

It consists of:

1. A thin client plugin running inside Sublime (Python 3.3)
1. A local backend server outside of Sublime (Python 3.6)

My use case for this project is that I wanted to write Python 3.6 code for a Sublime plugin; however, its current highest supported Python version is 3.3.6.

The client and server communicate via an HTTP API using Flask.

The demo client includes a vendorized dependency for `requests`.

## Setup

```
git clone https://github.com/tedmiston/sublime-plugin-client-server-demo.git
cd sublime-plugin-client-server-demo
cd server
pipenv install
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
ln -s ~/sublime-plugin-client-server-demo/client/ sublime-plugin-client-server-demo-client
```

## Quickstart

1. Start the server: `cd server && ./run.sh`
1. In Sublime, run `Client Server Demo: Versions` in the command palette.

## Development

To add/install vendorized dependencies:

```
pip install --target=vendor requests
```
