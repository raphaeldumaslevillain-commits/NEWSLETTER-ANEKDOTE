# Newsletter Anekdote

Reproduction du HTML de la newsletter intégrée au mail transféré le 29 octobre 2026 à 14 h 46, reprenant la version corrigée du 10 septembre 2026 à 12 h 36.

## Fichiers

- `index.html` : newsletter avec les styles dans `styles.css` et les images locales.
- `styles.css` : les 75 ensembles de déclarations CSS du message, repris sans modification.
- `newsletter.html` : version email autonome avec les styles intégrés et les images hébergées dans ce dépôt.
- `assets/images/` : six visuels originaux, dont la photo d’équipe extraite du mail.
- `verification.json` : résultats des contrôles de fidélité.

Ouvrir `index.html` dans un navigateur. Aucun outil de compilation ni dépendance n’est nécessaire. Pour une prévisualisation locale, lancer `python3 -m http.server 8000`, puis ouvrir `http://localhost:8000`.

## Fidélité à la source

La composition d’origine de 640 px est conservée, avec ses textes, espaces, sauts de ligne, liens, images, proportions, tableaux, polices et couleurs. Le HTML de la newsletter est isolé des signatures, des en-têtes de transfert et des anciennes versions citées dans le fil. Aucun contenu rédactionnel n’est réécrit.

Les styles de la version web sont extraits dans des classes `nl-*`. La version email conserve les styles inline pour éviter de dépendre d’une feuille CSS externe dans la messagerie. Les images locales ont été téléchargées sans transformation ; la photo d’équipe correspond aux octets du fichier intégré au mail.

La source utilise Montserrat avec Arial/Helvetica en secours, et Georgia pour les titres. Aucune police web supplémentaire n’est injectée : le choix de secours reste celui du message original. La composition fixe de 640 px est volontairement conservée sur les petits écrans.

Les destinations des liens sont reprises telles quelles. La source ne fournit aucune URL pour « Voir cet email dans votre navigateur » et « Se désinscrire » ; son lien Roland-Garros pointe vers `/projets/__trashed/`. Ces éléments restent identiques et devront être renseignés ou validés avant un envoi de campagne.

## Vérification

- Textes et espaces identiques au HTML source.
- 30 tableaux et sept éléments image, correspondant à six fichiers originaux.
- 343 éléments comparés dans le même navigateur à un viewport de 960 × 900 px : dimensions, typographie, couleurs, bordures, marges et espacements identiques.
- Captures intégrales de 960 × 7 192 px : comparaison pixel par pixel sans différence entre la source inline et la version avec CSS séparé.

La comparaison porte sur les deux versions dans le même navigateur. Le rendu d’un email dépend aussi du logiciel de messagerie et des polices installées.
