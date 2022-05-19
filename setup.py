from setuptools import setup
from setuptools.command.install import _install
import pip

class install(_install):
	def run(self):
		_install.do_egg_install(self)
		pip.main


setup(
	name = 'indicparser',
	version = '0.1',
	url = 'https://github.com/Saurabhbaghel/indicparser',
	packages = ['indicparser'],
# 	package_data = {
# 		'configs':['*.yaml'],
# 		},
	dependency_links = [ 
# 		'torchvision==0.6 -f '
# 		'https://download.pytorch.org/whl/cu101/torch_stable.html',
# 		'detectron2==0.1.3 -f' 
		'https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.5/detectron2-0.1.3%2Bcu101-cp38-cp38-linux_x86_64.whl#egg=detectron2-0.1.3'
		],
		
	
		
	install_requires = [
		'numpy',
		'opencv-python',
# 		'torch==1.5', 
		'torchvision==0.6 ', #'-f https://download.pytorch.org/whl/cu101/torch_stable.html',
		'pyyaml==5.4',
		'detectron2 @ https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.5/index.html',
		'pytesseract',
		'pdf2image',
		'pdfreader',
		'layoutparser[ocr]'
		]
	
)
