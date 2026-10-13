from dataclasses import dataclass
import json
import os
import random
from typing import List, Optional, Dict


_DATA_FILE = os.path.join(os.path.dirname(__file__), "names.json")
_CACHE = None


@dataclass(frozen=True)
class AllahName:
    number: int
    arabic: str
    transliteration: str
    english_name: str
    english_meaning: str
    arabic_meaning: str

    def to_dict(self, lang: str = "en") -> Dict[str, str]:
        return {
            "number": self.number,
            "arabic": self.arabic,
            "transliteration": self.transliteration,
            "name": self.arabic if lang == "ar" else self.english_name,
            "meaning": self.arabic_meaning if lang == "ar" else self.english_meaning,
        }


def _load_data() -> List[AllahName]:
    global _CACHE
    if _CACHE is not None:
        return _CACHE

    with open(_DATA_FILE, "r", encoding="utf-8-sig") as f:
        raw = json.load(f)

    names = []
    for item in raw["names"]:
        translations = item.get("translations", {})
        meanings = item.get("meaning", {})
        names.append(
            AllahName(
                number=item["number"],
                arabic=item["arabic"],
                transliteration=item.get("transliteration", ""),
                english_name=translations.get("en", item["arabic"]),
                english_meaning=meanings.get("en", ""),
                arabic_meaning=meanings.get("ar", ""),
            )
        )
    _CACHE = names
    return _CACHE


def get_all_names() -> List[AllahName]:
    """Retrieve all 99 names of Allah in order."""
    return _load_data()


def get_by_number(number: int) -> Optional[AllahName]:
    """Find a name by its number (1 to 99)."""
    if number < 1 or number > 99:
        return None
    names = _load_data()
    return names[number - 1]


def get_random_name() -> AllahName:
    """Return a random name of Allah."""
    names = _load_data()
    return random.choice(names)


def search_names(query: str) -> List[AllahName]:
    """
    Search names by Arabic text, transliteration, or English meaning.
    """
    q = query.strip().lower()
    results = []
    for name in _load_data():
        if (
            q in name.arabic
            or q in name.transliteration.lower()
            or q in name.english_name.lower()
            or q in name.english_meaning.lower()
            or q in name.arabic_meaning
        ):
            results.append(name)
    return results
