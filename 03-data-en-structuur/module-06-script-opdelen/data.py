"""Alles wat met het inlezen van data te maken heeft."""
import pandas as pd

MAP = "../../voorbeelddata/"


def lees_lokalen():
    return pd.read_csv(MAP + "lokalen.csv")


def lees_toetsen():
    return pd.read_csv(MAP + "toetsen.csv")


def lees_medewerkers():
    return pd.read_csv(MAP + "medewerkers.csv")


def lees_beschikbaarheid():
    return pd.read_csv(MAP + "beschikbaarheid.csv")


def lees_rooster():
    return pd.read_csv(MAP + "rooster.csv")
