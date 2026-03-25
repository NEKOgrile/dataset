# Construction et analyse d’un premier modèle

## 1. Cible à prédire
On veut prédire si un ticket est urgent ou pas.

## 2. Type de problème
C’est un problème de classification (oui ou non).

## 3. Variables d’entrée
On utilise par exemple :
- le nombre de mots
- le nombre de pièces jointes
- si le client est premium
- s’il y a un incident en production
- l’heure d’ouverture

On garde seulement les variables utiles.

## 4. Séparation train / test
On sépare les données en :
- 80 % pour entraîner
- 20 % pour tester

## 5. Entraînement du modèle
On utilise un modèle simple comme une régression logistique.
Le modèle apprend à faire le lien entre les données et si le ticket est urgent.

## 6. Prédictions
On utilise le modèle sur les données de test pour prédire si un ticket est urgent ou non.

## 7. Évaluation (métriques)
On obtient :
- accuracy : 1.0
- recall : 1.0

Donc le modèle fait aucune erreur sur les données test.

## 8. Conclusion sur le modèle
Le modèle a l’air parfait, mais en réalité il faut faire attention.
- Le dataset est petit et assez simple, donc le modèle apprend trop facilement.
- Les résultats peuvent être trompeurs et ne pas marcher sur de nouvelles données.
- Le recall reste important parce qu’on ne veut pas rater les tickets urgents.

## Restitution
- **Qu’a-t-on voulu prédire ?**
  On voulait prédire si un ticket est urgent ou pas.
- **Le modèle semble-t-il utile ?**
  Le modèle semble très bon avec des résultats parfaits, mais ce n’est pas forcément fiable à cause du dataset trop petit.
- **Quelle métrique vous paraît la plus importante ici ?**
  Le recall, parce que le but c’est de ne pas rater les tickets urgents.
- **Quelle limite principale avez-vous identifiée ?**
  La principale limite c’est la taille du dataset. Le modèle peut être trop adapté aux données et ne pas bien fonctionner en réalité.
