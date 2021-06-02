# Word generator package

#### This project generates a random picture, typing a table and puts it in a word file.
#### You can specify a clear length of the generated text and the path where the generated file will be saved.
***
## Installing
pip install word-gener
## How to use
```python
import word_gen.word_gen
from word_gen.word_gen import *

random_drawing() #This function generates a random picture from geometric shapes
get_table() #This function generates a random fixed-sized table of numbers
generate_random_string(length) #length- number of letters of random text. This function generates a random set of letters of a given length
merge(path) #path- selected save path. This function combines several word files into one single file at the specified path. Possibly can be used as a standalone helper library or smth idk ¯\_(ツ)_/¯
trash_clean() #This function cleans up intermediate files
```
# Example
```python
from word_gen.word_gen import word

random_drawing() 
get_table() 
generate_random_string(12) 
merge(r"C:\Users\Cherloy\Desktop\testing\result.docx") 
trash_clean() 
```
