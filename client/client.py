import os
import sys

import sublime
import sublime_plugin

# add vendorized dependencies to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')
if vendor_dir not in sys.path:
    sys.path.append(vendor_dir)

import requests  # noqa

settings = sublime.load_settings('Client Server Demo.sublime-settings')
server_host = settings.get('server_host')
server_port = settings.get('server_port')

SERVER_BASE_URL = '{}:{}'.format(server_host, server_port)


def _url(endpoint):
    return '{}{}'.format(SERVER_BASE_URL, endpoint)


def get_client_python_version():
    """Get the Python version running inside Sublime."""
    version = sys.version.split(' ')[0]
    return version


def get_server_python_version():
    """Get the Python version running on the local server."""
    resp = requests.get(_url('/version'))
    contents = resp.json()
    version = contents['version'].split(' ')[0]
    return version


class VersionsCommand(sublime_plugin.TextCommand):
    """
    Show Python versions running in Sublime and on the local server.
    """

    def run(self, edit):
        """Sublime entrypoint."""
        local_version = get_client_python_version()
        server_version = get_server_python_version()

        sublime.message_dialog(
            '- Client Python: {}\n- Server Python: {}'.format(
                local_version, server_version))
