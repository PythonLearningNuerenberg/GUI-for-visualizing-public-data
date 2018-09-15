### Python Coding Style Conventions (based on PEP 8 and PEP 257)
---
* **Module und Package Names**: Short and all-lowercase names. Underscores can be used to improve the readability.
    * *Pyhton Modul* is any source code file (*.py), no matter if it contains a class or not.
      > **classifier.py**   
      > **array_plotter.py**
    * *Python Package* is a directory containing python modules.
      > **classifiers/nbclassifier.py**   
      > **classifiers/knnclassifier.py**
* **Class Names**: Starting with upper case and followig CamelCase-Style (also named CapWords or Pascal Case)
```python
class FileReader:
```
* **Method Names**: All lower case. Underscores can be used to improve the readability.
```python
def build_data_frame(path, classification):
```
* **Variable Names**: Starting with lower case and followig CamelCase-Style (also called CapWords or Pascal Case)
```python
fileName = 'testfile.csv'
dataFrameContainer = FileReader().csv_to_dataframe(fileName)
counter = 0
```
* **Function and Method Comments**: Block comment using triple double-quotes (""") below the def line.  
```python
def build_data_frame(path, classification):
    """
    builds a pandas data frame out of the training data  
    :param path: path to training files as string
    :param classification: classification type as string
    :return: pandas data frame
    """
```

