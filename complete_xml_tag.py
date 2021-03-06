import sublime
import sublime_plugin

from .utils import complete_close_tag


class CompleteCloseTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        string_region = sublime.Region(0, self.view.size())
        string = self.view.substr(string_region)
        try:
            new_string = complete_close_tag(string)
        except ValueError as e:
            sublime.status_message(str(e))
        except Exception:  # Other types of exception
            return
        else:
            self.view.replace(edit, string_region, new_string)

    def is_enabled(self):
        s = sublime.load_settings('complete_xml_tag.sublime-settings')
        for selector in s.get('file_selectors', []):
            if self.view.match_selector(0, selector):
                return True
        return False
