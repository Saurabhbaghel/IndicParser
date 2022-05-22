
import subprocess
import sys
from re import findall

def check_compatibility():
 command='''if nvcc --version 2&> /dev/null; then
    # Determine CUDA version using default nvcc binary
    CUDA_VERSION=$(nvcc --version | sed -n 's/^.*release \([0-9]\+\.[0-9]\+\).*$/\1/p');
elif /usr/local/cuda/bin/nvcc --version 2&> /dev/null; then
    # Determine CUDA version using /usr/local/cuda/bin/nvcc binary
    CUDA_VERSION=$(/usr/local/cuda/bin/nvcc --version | sed -n 's/^.*release \([0-9]\+\.[0-9]\+\).*$/\1/p');
elif [ -f "/usr/local/cuda/version.txt" ]; then
    # Determine CUDA version using /usr/local/cuda/version.txt file
    CUDA_VERSION=$(cat /usr/local/cuda/version.txt | sed 's/.* \([0-9]\+\.[0-9]\+\).*/\1/');
else
    CUDA_VERSION="";
fi;'''
 res=subprocess.run(args=command,shell=True,universal_newlines=True,capture_output=True)
 pattern = 'release \d+.\d+'
 CUDA_VERSION = findall(pattern,res.stdout)[0].split()[1]
 
 
 try:
  import detectron2
  from detectron2.utils.logger import setup_logger
  setup_logger()
  import argparse
  from detectron2.engine import DefaultTrainer, default_argument_parser, default_setup, hooks, launch
  from detectron2 import model_zoo
  from detectron2.engine import DefaultPredictor
  from detectron2.config import get_cfg
  from detectron2.utils.visualizer import Visualizer
  from detectron2.data import MetadataCatalog, DatasetCatalog
  from detectron2.utils.visualizer import ColorMode

  from detectron2.structures import BoxMode
  from detectron2.data.datasets import register_coco_instances



 except:
  raise Exception(f'Please install pytorch version for CUDA version {CUDA_VERSION}. Please install torchvision combatible with the torch version. Also install Detectron2')
  sys.exit(1)
