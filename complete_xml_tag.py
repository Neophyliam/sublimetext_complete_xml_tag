import sublime
import sublime_plugin

from .utils import complete_close_tag


class CompleteCloseTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if not filename or filename[-3:].lower() != 'xml':
            return
        string_region = sublime.Region(0, self.view.size())
        string = self.view.substr(string_region)
        try:
            new_string = complete_close_tag(string)
        except InputError as e:
            sublime.status_message(str(e))
            return
        self.view.replace(edit, string_region, new_string)