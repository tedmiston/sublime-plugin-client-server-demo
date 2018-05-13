# Sublime Plugin Client-Server Demo

This repo provides a proof of concept for running a Sublime Text plugin as a client-server architecture.

It consists of:

1. A thin client plugin running inside Sublime (Python 3.3)
1. A local backend server outside of Sublime (Python 3.6)

My use case for this project is that I wanted to write Python 3.6 code for a Sublime plugin; however, its current highest supported Python version is 3.3.6.

The client and server communicate via an HTTP API using Flask.

The demo client includes a vendorized dependency for `requests`.

## Development

To add/install vendorized dependencies:

```
pip install --target=vendor requests
```
