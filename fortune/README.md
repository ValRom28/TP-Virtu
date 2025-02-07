Ce répertoire contient un Dockerfile et les fichiers nécessaires pour créer une image `fortune`. Chaque conteneur instance de cette image est un serveur web avec une page en php qui propose à l’utilisateur une citation en anglais et une photo du campus d’Orléans. Les citations sont obtenues à l’aide du programme [fortune](https://fr.wikipedia.org/wiki/Fortune_(logiciel)), tandis que les photos sont celles qui sont contenues dans le répertoire images.

Lors de la création du conteneur, les photos sont toutes redimensionnées à au plus 800x600 grâce au script `convert.sh` qui fait appel aux commande d’[ImageMagick](https://fr.wikipedia.org/wiki/ImageMagick).

Comme vous pouvez le voir, ce Dockerfile a été préparé avec peu de soin. La version que vous intégrerez à votre rendu devra être fonctionnelle bien sûr, mais l’image docker obtenue et déployée devra être minimale: elle ne contiendra que les éléments qui sont nécessaires à son _exécution_. Les éléments qui ne servent qu’à la construction de l’image ne seront ni dans l’image, ni dans ses layers. Les layers, quant à eux, seront en nombre minimal.

