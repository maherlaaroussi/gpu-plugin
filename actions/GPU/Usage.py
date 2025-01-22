# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

# Import python modules
import os
import subprocess
import re

# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class Usage(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_configuration = False
    
    def on_ready(self):
        self.update()
        
    def on_tick(self):
        self.update()

    def update(self):
        percent = round(self.get_gpu_usage())
        self.set_center_label(text=f"{percent}%", font_size=24)
        
    def get_gpu_usage():
        # Run the `rocm-smi -u -d 0` command
        result = subprocess.run(['rocm-smi', '-u', '-d', '0'], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Use a regular expression to find the GPU usage percentage
            match = re.search(r'GPU use \(%\): (\d+)', result.stdout)
            if match:
                gpu_usage = match.group(1)
                print(f"GPU Usage: {gpu_usage}%")
            else:
                print("GPU usage not found in the output.")
        else:
            print(f"Error running rocm-smi: {result.stderr}")