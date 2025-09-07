import pandas as pd

def load_data(input_path: str) -> pd.DataFrame:
    """Charger les données brutes Titanic."""
    return pd.read_csv(input_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage et transformation du dataset Titanic."""
    # Supprimer la colonne Cabin
    df = df.drop(columns=['Cabin'])
    
    # Remplacer les âges manquants par la médiane
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    
    # Remplacer les ports d’embarquement manquants par le mode
    mode_embarked = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(mode_embarked)
    
    # Convertir Survived en booléen
    df['Survived'] = df['Survived'].astype(bool)
    
    # Créer colonne IsChild
    df['IsChild'] = df['Age'] < 18
    
    # Créer colonne FareCategory
    df['FareCategory'] = pd.qcut(df['Fare'], 4, labels=['Low', 'Medium', 'High', 'Very High'])
    
    return df

def save_data(df: pd.DataFrame, output_csv: str, output_parquet: str):
    """Sauvegarder les données nettoyées en CSV et Parquet."""
    df.to_csv(output_csv, index=False)
    df.to_parquet(output_parquet, index=False)
    print("✅ Données exportées en:", output_csv, "et", output_parquet)

if __name__ == "__main__":
    # Chemins absolus adaptés à ton environnement Windows
    input_path = "C:/Users/0203555F/OneDrive - SNCF/Documents/Documents perso/Apprentissage DATA Engineer/PROJETS ETL/titanic_project/data/raw/train.csv"
    output_csv = "C:/Users/0203555F/OneDrive - SNCF/Documents/Documents perso/Apprentissage DATA Engineer/PROJETS ETL/titanic_project/data/clean/titanic_clean.csv"
    output_parquet = "C:/Users/0203555F/OneDrive - SNCF/Documents/Documents perso/Apprentissage DATA Engineer/PROJETS ETL/titanic_project/data/clean/titanic_clean.parquet"
    
    # Pipeline
    print("📥 Chargement des données brutes...")
    df = load_data(input_path)
    print("🔧 Nettoyage et transformation...")
    df_clean = clean_data(df)
    print("💾 Sauvegarde des données...")
    save_data(df_clean, output_csv, output_parquet)
