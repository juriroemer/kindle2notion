from enum import Enum


class Locale(Enum):
    # Enum containing languages
    ENGLISH = "en"
    SPANISH = "es"
    GERMAN = "de"

    def __str__(self):
        return self.value
    
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Word(Enum):
    # For each word, we have to handle different languages
    NOTE = {
        Locale.ENGLISH: "note",
        Locale.SPANISH: "nota",
        Locale.GERMAN: "Notiz",
    }
    LOCATION = {
        Locale.ENGLISH: "location",
        Locale.SPANISH: "posición",
        Locale.GERMAN: "Position",
    }
    PAGE = {
        Locale.ENGLISH: "page",
        Locale.SPANISH: "página",
        Locale.GERMAN: "Seite",
    }
    DATE_ADDED = {
        Locale.ENGLISH: "added on",
        Locale.SPANISH: "añadido el",
        Locale.GERMAN: "Hinzugefügt am",
    }
    # Date formats also depend on language
    DATE_FORMAT = {
        Locale.ENGLISH: "%A, %B %d, %Y %I:%M:%S %p",
        Locale.SPANISH: "%A, %d %B %Y %H:%M:%S",
        Locale.GERMAN: "%A, %d. %B %Y %H:%M:%S",
    }

    def __str__(self, language=Locale.ENGLISH):
        return self.value[language]
