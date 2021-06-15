# Word generator package

#### This project generates a random picture, typing a table and puts it in a word file.
#### You can specify a clear length of the generated text and the path where the generated file will be saved.
***
## Installing
pip install word-gener
## How to use
```python
from word_gen.word_gen import Word

random_drawing(shapes) #This function generates a random picture from geometric shapes shapes- shapes of figures
get_table() #This function generates a random fixed-sized table of numbers
random_string(length) #length- number of letters of random text. This function generates a random set of letters of a given length
merge(path) #path- selected save path. This function combines several word files into one single file at the specified path. Possibly can be used as a standalone helper library or smth idk ¯\_(ツ)_/¯
trash_clean() #This function cleans up intermediate files
```
# Example
```python
from word_gen.word_gen import Word

Word.random_drawing('circle''rectangle''ellipse''line) 
Word.get_table() 
Word.random_string(12) 
Word.merge(r"C:\Users\Cherloy\Desktop\testing\result.docx") 
Word.trash_clean() 
```
