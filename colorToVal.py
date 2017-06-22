
import sublime
import sublime_plugin
import re
import os


SETTINGS = {}
lastCompletion = {"needFix": False, "value": None, "region": None}


def plugin_loaded():
    init_settings()

def init_settings():
    get_settings()
    sublime.load_settings('colorRename.sublime-settings').add_on_change('get_settings', get_settings)

def get_settings():
    settings = sublime.load_settings('colorRename.sublime-settings')

    SETTINGS['exts'] = settings.get('exts', [".css", ".scss", ".less", ".sass", ".styl"])
    SETTINGS['data'] = settings.get('data')
    # data = settings.get('data')
def search(data):
    result={}
    count={}
    # print(data)
    for key in data:
        val = data[key]
        if val in count:count[val] = 1+ count[val]
        else: count[val] = 1
        if val in result:
            if count[val] > 1:result[val].append(key)
        else:
            result[val]=[key]
    return result
    # SETTINGS['leadingzero'] = settings.get('leadingzero', False)

def get_setting(view, key):
    return view.settings().get(key, SETTINGS[key]);

class CssRemCommand(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):

        # only works on specific file types
        fileName, fileExtension = os.path.splitext(view.file_name())
        if not fileExtension.lower() in get_setting(view, 'exts'):
            return []

        # reset completion match
        lastCompletion["needFix"] = False
        location = locations[0]
        snippet = []

        # get rem match
        match = re.compile("([a-fA-F1-9]{3,6})").match(prefix)
        if match:
            value = '#'+match.group(0)
           
            data = search(SETTINGS['data'])
            print(data)
            rename = data[value]

            commentStr = '';
            if (fileExtension.lower() in [".sass", ".scss", ".styl", ".less"]):
                commentStr = '; // ' + value + '';
            else:
                commentStr = ';/*' + value + '*/';

            # set completion snippet
            for index in range(len(rename)):

                snippet+= [[value +'\t'+'-> '+ rename[index] +'(keep number value)', '\\'+rename[index][0] +rename[index][1:]+commentStr]]
    
        return snippet

