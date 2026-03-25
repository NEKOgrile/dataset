import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score
from io import StringIO

with open("Dataset.csv", 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    line = line.strip()
    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1]
    line = line.rstrip(',')
    if line:
        cleaned_lines.append(line)

cleaned_data = '\n'.join(cleaned_lines)
data = pd.read_csv(StringIO(cleaned_data))

data = data.dropna()

print("=== Données chargées ===")
print(f"Dimensions: {data.shape}")
print("\nPremières lignes:")
print(data.head())
print("\nStatistiques:")
print(data.describe())
print()

X = data[["nb_mots", "nb_pieces_jointes", "client_premium", "incident_production", "heure_ouvree"]]
y = data["urgent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(len(data))
print("=== Résultats ===")
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Recall :", recall_score(y_test, y_pred, average='weighted'))