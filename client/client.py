from . import load_vendorized  # noqa

import sys

import sublime
import sublime_plugin

import requests

SERVER_BASE_URL = None


def show_error_server_not_running():
    sublime.error_message((
        'Could not connect to server. Is it running at {server_url}?'
    ).format(server_url=SERVER_BASE_URL))


def _url(endpoint):
    return '{}{}'.format(SERVER_BASE_URL, endpoint)


class BaseCommand(sublime_plugin.TextCommand):
    """Perform setup common to all commands."""

    def run(self, edit):
        global SERVER_BASE_URL

        self.settings = sublime.load_settings('Client Server Demo.sublime-settings')
        SERVER_BASE_URL = '{host}:{port}'.format(
            host=self.settings.get('server_host'),
            port=self.settings.get('server_port'),
        )


class BashCommand(BaseCommand):
    """Run an arbitrary bash command via POST request."""

    def run(self, edit):
        super().run(edit)

        window = sublime.active_window()
        window.show_input_panel('Command', '', self._on_done, None, None)

    def _on_done(self, text):
        try:
            resp = requests.post(_url('/bash'), json={'command': text})
        except requests.exceptions.ConnectionError:
            show_error_server_not_running()
            raise

        command = resp.json()['command']
        output_text = resp.json()['output']

        sublime.message_dialog((
            '- Command: {}\n- Output:\n{}'
        ).format(command, output_text))


class UppercaseCommand(BaseCommand):
    """Convert text to uppercase via GET request."""

    def run(self, edit):
        super().run(edit)

        window = sublime.active_window()
        window.show_input_panel('Text', '', self._on_done, None, None)

    def _on_done(self, text):
        try:
            resp = requests.get(_url('/upper'), params={'text': text})
        except requests.exceptions.ConnectionError:
            show_error_server_not_running()
            raise

        input_text = resp.json()['input']
        output_text = resp.json()['output']

        sublime.message_dialog((
            '- Input: {}\n- Output: {}'
        ).format(input_text, output_text))


class VersionsCommand(BaseCommand):
    """Show Python versions running in Sublime and on the local server."""

    def run(self, edit):
        super().run(edit)

        local_version = self._get_client_python_version()
        server_version = self._get_server_python_version()

        sublime.message_dialog((
            '- Client Python: {}\n- Server Python: {}'
        ).format(local_version, server_version))

    def _get_client_python_version(self):
        """Get the Python version running inside Sublime."""
        version = sys.version.split(' ')[0]
        return version

    def _get_server_python_version(self):
        """Get the Python version running on the local server."""
        try:
            resp = requests.get(_url('/version'))
        except requests.exceptions.ConnectionError:
            show_error_server_not_running()
            raise

        contents = resp.json()
        version = contents['version'].split(' ')[0]
        return version
