Step 1: Install Python. Link https://www.python.org/downloads/windows/
- For bootcamp, I installed  Python 3.7 (Windows x86-64 executable installer)

Step 2: Install Anaconda. Link https://www.anaconda.com/products/distribution#Downloads
- for bootcamp, I installed the 3.8 64-Bit Graphical Installer (510 MB)

Step 3: Open Anaconda Powershell

(base)...> conda update conda

(base)...> version

(base)...> conda create -n PythonData python=3.7 anaconda

(base)...> conda activate PythonData

(PythonData)...> conda deactivate

(base)...> conda create -n mlenv python=3.7 anaconda

(base)...> conda activate mlenv

(mlenv)...> conda install -c conda-forge imbalanced-learn

(mlenv)...> python -m ipykernel install --user --name mlenv

(mlenv)...> conda deactivate

(base)...> conda activate PythonData

(PythonData)...> conda install scikit-learn

(PythonData)...> conda install plotly

(PythonData)...> conda install -c pyviz hvplot

(PythonData)...> conda install tensorflow

---