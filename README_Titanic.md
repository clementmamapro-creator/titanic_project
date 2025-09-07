# 🚀 Projet Data Engineering : Nettoyage du dataset Titanic

## 🎯 Objectif
Ce projet a pour but de réaliser un pipeline **ETL complet** (Extract – Transform – Load) avec Python/pandas, 
à partir du célèbre dataset Titanic (Kaggle).  
L’objectif n’est pas de faire de la prédiction, mais de **préparer des données brutes en données exploitables**.

---

## 📂 Structure du projet
```
📁 titanic_project/
 ├── 📁 data/
 │    ├── raw/         # Données brutes (train.csv)
 │    └── clean/       # Données nettoyées (titanic_clean.csv, titanic_clean.parquet)
 ├── 📁 notebooks/
 │    └── 01_titanic_cleaning.ipynb   # Notebook complet ETL
 ├── 📁 scripts/
 │    └── cleaning.py  # Script Python réutilisable
 ├── README.md
 └── requirements.txt
```

---

## 🛠️ Étapes réalisées

### 1. Extraction
- Chargement du fichier CSV (`train.csv`).
- Aperçu des données brutes (`head()`, `info()`, `shape`).

### 2. Exploration
- Analyse descriptive (`describe()`).
- Détection des valeurs manquantes (`isnull().sum()`).
- Analyse des colonnes catégorielles (`Sex`, `Embarked`).

### 3. Nettoyage
- Suppression de la colonne `Cabin` (trop de valeurs manquantes).
- Remplacement des valeurs manquantes d’`Age` par la médiane.
- Remplacement des valeurs manquantes d’`Embarked` par la valeur la plus fréquente.
- Conversion de `Survived` en booléen.
- Création de nouvelles colonnes :
  - `IsChild` (Age < 18)
  - `FareCategory` (Low, Medium, High, Very High)

### 4. Validation & Visualisation
- Vérification des valeurs manquantes.
- Visualisations avec matplotlib/seaborn :
  - Distribution des âges
  - Répartition par port d’embarquement
  - Répartition par catégorie de tarif
  - Comparaison enfants/adultes
  - Taux de survie par catégorie de tarif

### 5. Chargement
- Export des données nettoyées en :
  - `titanic_clean.csv`
  - `titanic_clean.parquet`

---

## 📊 Résultats
- Un dataset **nettoyé et enrichi**, prêt pour l’analyse ou la modélisation.
- Exemple : répartition des passagers par port d’embarquement, catégorie de tarif, enfants/adultes.

---

## 🔧 Stack technique
- Python 3.x
- Pandas
- Numpy
- Matplotlib
- Seaborn
- PyArrow (export Parquet)

---

## 📢 Valorisation
Ce projet illustre ma capacité à :
- Construire un pipeline ETL simple.
- Nettoyer et enrichir un dataset brut.
- Exporter dans des formats modernes (CSV, Parquet).
- Documenter et partager mon travail (GitHub, LinkedIn).

---

✍️ Auteur : [Ton Prénom Nom] – Data Engineer en apprentissage 🚀
