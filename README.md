# Newsletter Anekdote — Offres du moment

Version de démonstration de la newsletter d’origine, enrichie de quatre offres fictives : **Offres loges, Cannes, Les Ardentes, GP de Monaco**.

Les quatre offres sont des exemples de présentation. Des photographies documentaires illustrent leurs lieux et leurs ambiances.

## Voir et modifier

- [Prévisualisation GitHub Pages](https://raphaeldumaslevillain-commits.github.io/NEWSLETTER-ANEKDOTE/)
- `index.html` + `styles.css` : édition web, images locales.
- `newsletter.html` : édition email, styles intégrés et images servies par GitHub Pages.
- `offers.json` : textes, prestations de démonstration et libellés des boutons.
- `templates/newsletter-base.html` : trame éditoriale mise à jour selon les retours, isolée des signatures et du fil de discussion.
- `scripts/build.py` : génération des deux éditions, sans dépendance.
- `verification.json` : dimensions, liens et contrôles de construction.

Après une modification : `python3 scripts/build.py`. Pour un aperçu local : `python3 -m http.server 8000`.

## Placement et conversion

Le parcours présente d’abord les **cinq réalisations** (loge, Cannes, Roland-Garros, Yves Rocher, Peugeot), puis **« Et pour votre marque ? »**, les sept expertises et le lien de rendez-vous, et enfin **les quatre offres du moment**, avant la prise de contact finale. La loge apparaît uniquement dans les offres du moment. Les cartes indiquent un format sur mesure, sans nombre d’invités imposé. Ce choix de présentation n’est pas présenté comme un gain de conversion mesuré.

Sur ordinateur, la newsletter mesure 600 px de large, avec des marges intérieures de 40 px. Chaque carte mesure 248 px de large, avec un visuel de 248 × 155 px et un intervalle de 24 px. Les quatre visuels sont en couleur et exportés à 536 × 336 px pour les écrans denses. Les boutons HTML contrastés mesurent 48 px de haut et ne dépendent pas du chargement des images.

À 600 px et en dessous, les cartes s’empilent en une colonne, avec des marges de 24 px, des paragraphes de 16 px et des boutons sur toute la largeur utile de la carte. Le reste de la newsletter s’adapte également pour éviter un défilement horizontal.

Cannes et le GP de Monaco ouvrent un e-mail à Christelle Egron avec l’objet de l’offre. Les loges et Les Ardentes pointent vers le formulaire de contact Anekdote, avec un paramètre `utm_content` distinct. Ces paramètres identifient l’offre dans un outil de mesure compatible ; ils n’installent pas à eux seuls un système de statistiques. Aucun formulaire ni email n’est envoyé automatiquement.

Références de conception : [boutons HTML et libellés explicites — Mailchimp](https://templates.mailchimp.com/design/calls-to-action/), [lisibilité et boutons sur mobile — Mailchimp](https://templates.mailchimp.com/design/mobile-friendliness/).

## Photos et licences

Les photographies ont été recadrées et redimensionnées pour les cartes.

- **Offres loges** — [Loge du concert d’Aya Nakamura, projet Anekdote](https://www.anekdote.fr/projets/concert-aya-nakamura-x-ghd-x-juliette-has-a-gun/).
- **Cannes** — [Photographie de la villa, médiathèque de DBM Group](https://digitalbrandmakers-group.com/wp-content/uploads/2025/11/Rectangle-3.png).
- **Les Ardentes** — Jean-Philippe Bonhomme (JPB.), [Vald sur la scène Wallifornia Beach, Les Ardentes 2019](https://commons.wikimedia.org/wiki/File:Vald_en_live_sur_la_sc%C3%A8ne_Wallifornia_Beach_(Les_Ardentes).jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Le recadrage est distribué sous la même licence.
- **GP de Monaco** — visuel fourni pour la newsletter, recadré hors de l’encart.

## Base éditoriale et retours

La mise à jour du 5 novembre 2026 ajoute Peugeot au Mondial de l’Auto, précise le contexte du dîner Big Média à Cannes et présente les sept expertises pour 2027. Le générateur vérifie l’ordre de lecture et le lien de rendez-vous avant l’insertion des offres.

« Voir cet email dans votre navigateur » mène maintenant à GitHub Pages. Le lien de désinscription reste sans destination, comme dans la source ; le lien Roland-Garros conserve `/projets/__trashed/`. Ces deux points devront être renseignés ou validés avant un véritable envoi.

Le rendu d’un email dépend du logiciel de messagerie. Le contrôle navigateur porte sur la version web et sa variante email ; il ne constitue pas un test d’envoi dans tous les clients mail.

## Publication

GitHub Pages utilise la branche `main`, dossier `/ (root)`. Le fichier `.nojekyll` permet de servir directement les fichiers statiques. Aucun processus de compilation n’est requis pour l’hébergement.
