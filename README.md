# allah-names (Python) ✨

**The 99 Beautiful Names of Allah (Asma ul-Husna) with transliteration, Arabic explanation, and English meanings.**

Includes offline bundled dataset, search, and random selection utilities.

---

## ✨ Features
- 📴 **100% Offline**: Dataset bundled directly within the package (no network / no API key).
- 🔍 **Multi-lingual Search**: Search by Arabic spelling, Latin transliteration, or English meaning.
- 🎲 **Name of the Day**: Random selection helper.
- ⚡ **Zero External Dependencies**: Pure Python standard library only.

---

## 📦 Installation
```bash
pip install allah-names
```

---

## 🚀 Usage

### 1. Get All 99 Names
```python
from allah_names import get_all_names

names = get_all_names()
for n in names[:5]:
    print(f"{n.number}. {n.arabic} ({n.transliteration}) - {n.english_meaning}")
```

### 2. Get Name by Number (1 to 99)
```python
from allah_names import get_by_number

name = get_by_number(1)
print(name.arabic)          # "الله"
print(name.transliteration) # "Allah"
print(name.english_name)    # "The Greatest Name"
print(name.arabic_meaning)  # "الإله الحق المستحق للعبادة وحده"
```

### 3. Search Names
```python
from allah_names import search_names

# Search by English meaning
merciful = search_names("Merciful")
for m in merciful:
    print(m.arabic, m.transliteration)

# Search by Arabic
q = search_names("الغفور")
```

### 4. Random Name Generator
```python
from allah_names import get_random_name

random_name = get_random_name()
print(f"Name of the day: {random_name.arabic} ({random_name.english_meaning})")
```

---

## 📄 License
MIT License.
