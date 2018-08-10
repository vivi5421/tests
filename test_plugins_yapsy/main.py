from yapsy.PluginManager import PluginManager
import logging

logging.basicConfig(level=logging.DEBUG)
# Build the manager
simplePluginManager = PluginManager()
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces(["plugins"])
# Load all plugins
simplePluginManager.setPluginLocator()
simplePluginManager.collectPlugins()

print("start")
# Activate all loaded plugins
print(simplePluginManager.getAllPlugins())
for pluginInfo in simplePluginManager.getAllPlugins():
    print(pluginInfo)
    simplePluginManager.activatePluginByName(pluginInfo.name)
    pluginInfo.plugin_object.speak()
