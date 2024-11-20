# **🌱 Catalogue Botanique**

Un projet académique de développement web visant à créer un catalogue interactif de feuilles et fruits.

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
- Afficher des informations détaillées sur chaque élément botanique.
- Fournir une expérience utilisateur interactive et dynamique.

---

## **🔍 MVP et MVT dans ce projet**

### **MVP (Minimum Viable Product)**
Le concept de **MVP** repose sur la création rapide d'une version fonctionnelle et minimale d'un produit pour tester ses fonctionnalités essentielles.  
Dans ce projet, notre MVP inclut :
1. Une **page d'accueil dynamique** avec des citations changeantes.
2. Un **catalogue interactif** permettant de naviguer entre les feuilles et fruits.
3. Une **section "À propos" extensible**, accessible via le footer, pour fournir des informations sur le projet et les contacts.

### **MVT (Model-View-Template)**
Le projet suit l'architecture **MVT**, typique de Django :
- **Model** : Les modèles définissent la structure des données (ex. : `Species` pour les feuilles et fruits).
- **View** : Les vues gèrent la logique métier (ex. : affichage des pages et gestion des interactions utilisateur).
- **Template** : Les fichiers HTML définissent la présentation visuelle et utilisent les données fournies par les vues.

Cette structure garantit une séparation claire entre les données, la logique et l'interface utilisateur, rendant le code plus modulaire et maintenable.

---

## **✨ Fonctionnalités principales**
- **Page d'accueil dynamique** : Affichage de citations changeantes toutes les 10 secondes avec une animation fluide.

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
   git clone https://github.com/nom-utilisateur/catalogue-botanique.git


## 📚 Cas d'usage  
### Cas 1 : Recherche d'une feuille  
1. L'utilisateur tape un mot-clé dans la barre de recherche.  
2. L'application affiche les espèces correspondantes.  
3. En cliquant sur un résultat, l'utilisateur accède à des détails ainsi qu'une sélection d'images de l'espèce.  

### Cas 2 : Apprentissage via un quizz  
1. L'utilisateur lance le quizz interactif.  
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