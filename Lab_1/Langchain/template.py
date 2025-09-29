import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name = "mongodb_connect"

list_of_files = [
  # ".github/workflows/.gitkeep", This Is use when You Want to Push Empty Directories
   ".github/workflows/ci.yaml",
   "config/__init__.py",
   "config/logging_config.yaml",
   "config/model_config.yaml",
   "config/prompt_template.yaml",
   "notebooks/model_experimentation.ipynb ",
   "notebooks/prompt_testing.ipynb",
   "notebooks/response_analysis.ipynb",
   "src/graph/__init__.py",
   "src/graph/graph_builder.py",
   "src/llm/groqllm.py",
   "src/llm/__init__.py",
   "src/nodes/__init__.py",
   "src/nodes/basic_chatbot_node.py",
   "src/state/__init__.py",
   "src/state/basic_state.py",
   "src/tools/__init__.py",
   "src/ui/__init__.py",
   "src/ui/uiconfigfile.ini",
   "src/ui/uiconfigfile.py",
   "src/ui/streamlitui/display_result.py",
   "src/ui/streamlitui/__init__.py",
   "src/ui/streamlitui/loadui.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "main.py"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
