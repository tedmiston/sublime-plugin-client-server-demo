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

SERVER_BASE_URL = None


def _url(endpoint):
    return '{}{}'.format(SERVER_BASE_URL, endpoint)


def get_client_python_version():
    """Get the Python version running inside Sublime."""
    version = sys.version.split(' ')[0]
    return version


def get_server_python_version():
    """Get the Python version running on the local server."""
    try:
        resp = requests.get(_url('/version'))
    except requests.exceptions.ConnectionError:
        sublime.error_message((
            'Could not connect to server. Is it running at {server_url}?'
        ).format(server_url=SERVER_BASE_URL))
        raise

    contents = resp.json()
    version = contents['version'].split(' ')[0]
    return version


class VersionsCommand(sublime_plugin.TextCommand):
    """
    Show Python versions running in Sublime and on the local server.
    """

    def run(self, edit):
        """Sublime entrypoint."""
        global SERVER_BASE_URL

        self.settings = sublime.load_settings('Client Server Demo.sublime-settings')
        SERVER_BASE_URL = '{host}:{port}'.format(
            host=self.settings.get('server_host'),
            port=self.settings.get('server_port'),
        )

        local_version = get_client_python_version()
        server_version = get_server_python_version()

        sublime.message_dialog((
            '- Client Python: {}\n- Server Python: {}'
        ).format(local_version, server_version))


class UppercaseCommand(sublime_plugin.TextCommand):
    """
    Convert text to uppercase via POST request.
    """

    def run(self, edit):
        """Sublime entrypoint."""
        global SERVER_BASE_URL

        self.settings = sublime.load_settings('Client Server Demo.sublime-settings')
        SERVER_BASE_URL = '{host}:{port}'.format(
            host=self.settings.get('server_host'),
            port=self.settings.get('server_port'),
        )

        window = sublime.active_window()
        window.show_input_panel('Text', '', self._on_done, None, None)

    def _on_done(self, text):
        resp = requests.post(_url('/upper'), json={'text': text})
        input_text = resp.json()['input']
        output_text = resp.json()['output']

        sublime.message_dialog((
            '- Input: {}\n- Output: {}'
        ).format(input_text, output_text))
