import os
import sys
import importlib

class PluginManager(object):
    def __init__(self):
        self.plugins_path = os.path.join("src", "plugins", "examples")
        self._plugins = list()

    @property
    def plugins_path(self):
        return self._plugins_path

    @plugins_path.setter
    def plugins_path(self, path):
        if not os.path.exists(path):
            raise IOError("Path does not exist")
        if not path in sys.path:
            sys.path.insert(0, path)
        self._plugins_path = path

    @property
    def plugins(self):
        return self._plugins

    def collectPlugins(self):
        for (root, dirs, files) in os.walk(self._plugins_path):
            for a_file in files:
                (name, extension) = os.path.splitext(a_file)
                if extension == os.extsep + "py":
                    self._plugins.append(name)


    def loadPlugins(self):
        for plugin in self._plugins:
            module = importlib.import_module(plugin)
            plugin_class = getattr(module, plugin)
            plugin_instance = plugin_class()
            plugin_instance.activate()
