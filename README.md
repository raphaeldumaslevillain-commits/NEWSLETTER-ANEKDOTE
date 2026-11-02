# Newsletter Anekdote — Offres du moment

Version de démonstration de la newsletter d’origine, enrichie de quatre offres fictives : **Offres loges, Cannes, Les Ardentes, GP de Monaco**.

**Les prestations et images des quatre offres sont fictives.** Ils servent à présenter la mise en page. Aucune disponibilité, date, affiliation officielle ou prestation réelle n’est annoncée. Les visuels d’ambiance ont été générés avec ImageGen, puis exportés au format JPEG pour la newsletter.

## Voir et modifier

- [Prévisualisation GitHub Pages](https://raphaeldumaslevillain-commits.github.io/NEWSLETTER-ANEKDOTE/)
- `index.html` + `styles.css` : édition web, images locales.
- `newsletter.html` : édition email, styles intégrés et images servies par GitHub Pages.
- `offers.json` : textes, prestations de démonstration et libellés des boutons.
- `templates/newsletter-base.html` : trame éditoriale mise à jour selon les retours, isolée des signatures et du fil de discussion.
- `scripts/build.py` : génération des deux éditions, sans dépendance.
- `verification.json` : dimensions, liens et contrôles de construction.
- `assets/offers/image-prompts.json` : prompts des quatre visuels ImageGen.

Après une modification : `python3 scripts/build.py`. Pour un aperçu local : `python3 -m http.server 8000`.

## Placement et conversion

Le parcours présente d’abord les **quatre réalisations** (loge, Cannes, Roland-Garros, Yves Rocher), puis **« Et pour votre marque ? » et les six offres**, et enfin **les quatre offres du moment**, avant la prise de contact finale. La loge apparaît uniquement dans les offres du moment. Les cartes indiquent un format sur mesure, sans nombre d’invités imposé. Ce choix de présentation n’est pas présenté comme un gain de conversion mesuré.

La grille conserve la composition de 640 px et les marges de 40 px de la newsletter. Sur ordinateur, chaque carte mesure 268 px de large, avec un visuel de 268 × 168 px et un intervalle de 24 px. Les quatre visuels sont en couleur et exportés à 536 × 336 px pour les écrans denses. Les boutons HTML contrastés mesurent 48 px de haut et ne dépendent pas du chargement des images.

À 640 px et en dessous, les cartes s’empilent en une colonne, avec des marges de 24 px, des paragraphes de 16 px et des boutons sur toute la largeur utile de la carte. Le reste de la newsletter s’adapte également pour éviter un défilement horizontal.

Chaque offre pointe vers le formulaire de contact Anekdote, avec un paramètre `utm_content` distinct. Ces paramètres identifient l’offre dans un outil de mesure compatible ; ils n’installent pas à eux seuls un système de statistiques. Aucun formulaire ni email n’est envoyé automatiquement.

Références de conception : [boutons HTML et libellés explicites — Mailchimp](https://templates.mailchimp.com/design/calls-to-action/), [lisibilité et boutons sur mobile — Mailchimp](https://templates.mailchimp.com/design/mobile-friendliness/).

## Base éditoriale et retours

Les quatre études de cas conservent les textes, chiffres et images du mail corrigé du 10 septembre 2026, transféré le 29 octobre. La mise à jour éditoriale du 2 novembre intègre les textes demandés pour le conseil en stratégie et l’événementiel, le passage à six offres sans doublon loge, et « Nous serions ravis » dans la conclusion. Le générateur vérifie le parcours et la préservation de cette trame éditoriale lors de l’insertion des cartes.

« Voir cet email dans votre navigateur » mène maintenant à GitHub Pages. Le lien de désinscription reste sans destination, comme dans la source ; le lien Roland-Garros conserve `/projets/__trashed/`. Ces deux points devront être renseignés ou validés avant un véritable envoi.

Le rendu d’un email dépend du logiciel de messagerie. Le contrôle navigateur porte sur la version web et sa variante email ; il ne constitue pas un test d’envoi dans tous les clients mail.

## Publication

GitHub Pages utilise la branche `main`, dossier `/ (root)`. Le fichier `.nojekyll` permet de servir directement les fichiers statiques. Aucun processus de compilation n’est requis pour l’hébergement.
