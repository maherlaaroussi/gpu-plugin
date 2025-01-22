# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.GPU.Usage import Usage

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.simple_action_holder = ActionHolder(
            plugin_base = self,
            action_base = Usage,
            action_id = "com_maherlaaroussi_gpuplugin::Usage",
            action_name = "GPU Usage",
        )
        self.add_action_holder(self.simple_action_holder)

        # Register plugin
        self.register(
            plugin_name = "GPU",
            github_repo = "https://github.com/maherlaaroussi/gpu-plugin",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )