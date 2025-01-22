# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.GPU.Usage import Usage
from .actions.GPU.Temperature import Temperature
from .actions.GPU.VRAM import VRAM
from .actions.GPU.Power import Power

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        self.gpu_usage_holder = ActionHolder(
            plugin_base = self,
            action_base = Usage,
            action_id = "com_maherlaaroussi_gpuplugin::Usage",
            action_name = "GPU Usage",
        )
        self.add_action_holder(self.gpu_usage_holder)

        self.gpu_temperature_holder = ActionHolder(
            plugin_base = self,
            action_base = Temperature,
            action_id = "com_maherlaaroussi_gpuplugin::Temperature",
            action_name = "GPU Temperature",
        )
        self.add_action_holder(self.gpu_temperature_holder)

        self.gpu_vram_holder = ActionHolder(
            plugin_base = self,
            action_base = VRAM,
            action_id = "com_maherlaaroussi_gpuplugin::VRAM",
            action_name = "GPU VRAM",
        )
        self.add_action_holder(self.gpu_vram_holder)

        self.gpu_power_holder = ActionHolder(
            plugin_base = self,
            action_base = Power,
            action_id = "com_maherlaaroussi_gpuplugin::Power",
            action_name = "GPU Power",
        )
        self.add_action_holder(self.gpu_power_holder)

        # Register plugin
        self.register(
            plugin_name = "GPU",
            github_repo = "https://github.com/maherlaaroussi/gpu-plugin",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )