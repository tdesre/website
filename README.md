# **🌱 Catalogue Botanique**

Ceci est un projet de développement d'une application web dont l'objectif est de créer un catalogue de feuilles et de fruits.

## **📖 Table des matières**
- [🌟 Introduction](#-introduction)
- [🔍 MVP et MVT dans ce projet](#-mvp-et-mvt-dans-ce-projet)
- [✨ Fonctionnalités principales](#-fonctionnalités-principales)
- [🛠️ Outils utilisés](#️-outils-utilisés)
- [⚙️ Installation](#️-installation)
- [📚 Cas d'usage](#-cas-dusage)
- [✅ Tests et Couverture](#-tests-et-couverture)
- [🤝 Contributeurs](#-contributeurs)
- [🖼️ Aperçu des pages](#️-aperçu-des-pages)

---

## **🌟 Introduction**
Le projet *Catalogue Botanique* a été développé dans le cadre d'un projet académique pour démontrer nos compétences en programmation web.  
Il permet de :
- Explorer un large catalogue de feuilles et de fruits.
- Afficher une description regroupant des informations sur les éléments du catalogue.
- Fournir une expérience utilisateur interactive et dynamique.

---

## **🔍 MVP et MVT dans ce projet**

### **MVP (Minimum Viable Product)**
Le concept de **MVP** repose sur la création d'une version fonctionnelle et minimale d'un produit pour tester ses fonctionnalités.  
Pour ce projet, notre MVP comprend :
1. Une **page d'accueil dynamique** avec des faits intéressants.
2. Un **catalogue interactif** permettant de naviguer entre les feuilles et fruits de façon ergonomique.
3. Une **section "À propos" extensible**, accessible via le footer, pour fournir des informations sur les contacts des créateurs du site web.

### **MVT (Model-View-Template)**
Le projet suit également l'architecture **MVT** :
- **Model** : Les modèles définissent la façon dont sont structurées les données (ex. : `Species` pour les feuilles et fruits).
- **View** : Les vues gèrent la logique métier (ex. : affichage des pages et gestion des interactions utilisateur).
- **Template** : Les fichiers HTML définissent la présentation visuelle et utilisent les données fournies par les vues.

---

## **✨ Fonctionnalités principales**
- **Page d'accueil dynamique** : Affichage dynamique de citations faits intéressants toutes les 10 secondes.

- **Catalogue interactif** : Navigation dans une liste de feuilles et fruits avec des informations détaillées sur chaque élément. Bandeau d'affichage permettant une navigation fluide entre les différentes pages du site web.

- **Section "À propos" interactive** : Accessible depuis un footer extensible, contenant des informations sur le projet et des contacts.

- **Conception responsive** : Compatible sur tous types d'ordinateurs.

- **Design élégant et intuitif** : Affichage dynamique et interactif des éléments du catalogue.

---

## **🛠️ Outils utilisés**
- *Backend* : [Python](https://www.python.org/doc/), [Django](https://www.djangoproject.com/)
- *Frontend* : HTML, CSS, JS
- *Base de données* : [SQLite](https://www.sqlite.org/)
- *AUTRE* : [Bootstrap](https://getbootstrap.com/) pour une partie des designs

---

## **⚙️ Installation**
1. Clonez ce dépôt :  
   ```bash
   git clone https://gitlab-cw4.centralesupelec.fr/theophile.desre/coding-weeks-site-web.git


## 📚 Cas d'usage  
### Cas 1 : Recherche d'une feuille  
1. L'utilisateur tape un mot-clé dans la barre de recherche.  
2. L'application affiche les espèces correspondantes à ce mot clé.  
3. En cliquant sur un résultat, l'utilisateur accède à des détails ainsi qu'une sélection d'images de l'espèce.  

### Cas 2 : Apprentissage via un quizz  
1. L'utilisateur lance le quizz comportant 5 questions.  
2. Il répond à des questions sur les feuilles et fruits.  
3. Il reçoit un score et des corrections pour apprendre de manière ludique.  

---
## ✅ Tests et Couverture  
Pour garantir la qualité et la stabilité de notre application, nous avons conçu une suite de tests avec Django et mesuré leur couverture grâce à l'outil **Coverage**.  

### Commandes utilisées :  
1. **Exécution des tests avec Coverage** :  
   ```bash
   coverage run --source='.' manage.py test
   coverage report

## **🤝 Contributeurs**
- *Amélie BELLAZI*
- *Hortense CLAUDON*
- *Tom CONNERY*
- *Théophile DESRE*
- *Philippine FROUX*
- *Ilan TARABULA*

---

## 🖼️ Aperçu des pages

### Page d'accueil
<img src="https://gitlab-cw4.centralesupelec.fr/theophile.desre/coding-weeks-site-web/-/raw/Ilan_fix_accueil_wed/img/Capture_d_%C3%A9cran__1_.png" alt="Page d'accueil" width="800">

### Page de catalogue
<img src="https://gitlab-cw4.centralesupelec.fr/theophile.desre/coding-weeks-site-web/-/raw/Ilan_fix_accueil_wed/img/Capture_d_%C3%A9cran__6_.png" alt="Page de catalogue" width="800">

### Détails des feuilles/fruits
<img src="https://gitlab-cw4.centralesupelec.fr/theophile.desre/coding-weeks-site-web/-/raw/Ilan_fix_accueil_wed/img/Capture_d_%C3%A9cran__9_.png" alt="Détails" width="800">