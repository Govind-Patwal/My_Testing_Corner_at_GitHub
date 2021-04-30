## Running Jupyter notebook from D drive (or any drive except D) on Windows

### Why?
- By default Jupyter Notebook opens the files on C drive and does not give the option to access files on any non-C drive drive
- Many people (including I) want to reserve the C drive for OS, and D for data, so that in case of OS failure, they can reinstall the OS without losing data.

### How?
 - Press 'Windows' button -> Anaconda Prompt (Anaconda3)
 - the default prompt will be 
 ```
 (base) C:\Users\test_user_name>
 ```
 - enter the name of the desired drive follwed by the colon (example below)
```
(base) C:\Users\test_user_name>d:
```
- on the prompt, enter jupyter notebook and hit enter
```
(base) D:\> jupyter notebook
```

## All steps after opening the Anaconda Prompt (Anaconda3)
```
(base) C:\Users\test_user_name>d:
(base) D:\> jupyter notebook
```

## Result
The steps above will open the desired folder and a person will be able to navigate to the required files/folders and access the .ipynb files

## Resource:
https://www.youtube.com/watch?v=1edPJiA0_38

---