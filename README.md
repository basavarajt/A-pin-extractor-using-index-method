# 🌟 **Poem PIN Extractor**

A fun and educational Python project that turns poems into **secret numeric PIN codes** using word positions and lengths.
Perfect for practicing string manipulation, loops, indexing, error handling, and clean coding.

---

## 📌 **How the PIN Is Generated**

For each poem:

1. Split the poem into lines
2. For each line *i* (0-based index):

   * Take the **i-th word** in that line
   * If the word exists → add the **length** of that word to the PIN
   * If it does *not* exist → add `'0'`
3. Merge all digits to form the poem’s secret PIN
4. Repeat for every poem provided

This guarantees every line contributes to the final code — even short or incomplete ones.

---

## 🔍 **Example**

### Input Poem:

```
Stars and the moon
shine in the sky
white and
until the end of the night
```

### Processing:

* Line 0 → word 0 = "Stars" → len = 5
* Line 1 → word 1 = "in" → len = 2
* Line 2 → missing word at index 2 → add 0
* Line 3 → word 3 = "of" → len = 2

### Output PIN:

```
5202
```

---

## 🧠 **How It Works (Simple Version)**

* Break poem into lines
* Break each line into words
* Use the **line number** to choose which word to examine
* Convert selected word to a number using its length
* If the word doesn’t exist, use `'0'`
* Combine everything into a string PIN

This creates a consistent, reliable decoding system for any poem or text block.

---

## 🧪 **Example Code Snippet**

```python
from typing import List

def extract_code_from_poem(poem: str) -> str:
    code = []
    lines = poem.split('\n')

    for i, line in enumerate(lines):
        words = line.split()
        if i < len(words):
            digit = str(len(words[i]))
        else:
            digit = '0'
        code.append(digit)

    return ''.join(code)


def pin_extractor(poems: List[str]) -> List[str]:
    return [extract_code_from_poem(poem) for poem in poems]
```

---

## 🚀 **Run the Script**

```
python pin_extractor.py
```

Expected output:

```
['5202', '3346', '50000']
```

---

## 🎌 **Fun Anime-Style Explanation (Optional Flavor!)**

Imagine each poem is a **ninja training ground**:

* Each *line* is a squad
* Each *word* is a ninja in that squad
* For mission *i*, your job is to pick ninja *i*
* Measure their **power level** (length of their name)
* If the ninja is missing → mark `'0'`

Combine all the power levels → you get the **secret ninja PIN**.

Your Python script is basically performing a coded ninja ceremony 😤🔥

---

## 📁 **Repository Contents**

```
├── pin_extractor.py   # Main script
├── README.md          # Documentation
```

---

## 💡 **Possible Improvements**

* Add unit tests
* Create a CLI version (command line interface)
* Build a GUI with Tkinter or PyQt
* Add file input support
* Add visualization of how the PIN is formed
* Encode/decode system for messages

---

## 🤝 **Contributing**

Feel free to fork, improve, or open issues.
Pull requests welcome!

---

## ⭐ **Like This Project?**

Give it a star ⭐ on GitHub — it helps more people find it!


