---
aliases: ["/2012/03/ajoutez-des-photos-par-lot-dans-wordrpress-unix-et-mac-os/"]
date: "2012-03-16T00:00:00Z"
description: "Vous utilisez WordPress pour votre blog ou votre site ? Vous en avez ras-le-bol de devoir insérer vos images une à une dans vos articles ? Vous êtes…"
tags: []
title: "Ajoutez des photos par lot dans Wordrpress ( UNIX et Mac OS )"
---
Vous utilisez WordPress pour votre blog ou votre site ?
Vous en avez ras-le-bol de devoir insérer vos images une à une dans vos articles ?
Vous êtes allergiques aux plugins à tout-va ?

J&#8217;ai la solution : un script shell, léger et rapide. (cliquez ici pour télécharger : [Batch WordPress][1])

Après m&#8217;être heurté à des connaissances tout de même limitées et au pavé &#8220;Scripts Shell&#8221;, d&#8217;Arnold Robbins, j&#8217;ai demandé un coup de main à [Romain Deville][2], car je faisais en effet fausse route.
Le principe est de disposer d&#8217;un script exécutable en quelques secondes qui utilise les photos que j&#8217;ai préparé pour mon article afin de générer le code HTML que je collerai dans l&#8217;article, après avoir importé mes photos dans WordPress. Et pouf, comme par magie, je n&#8217;aurai pas à &#8220;insérer&#8221; les images à la main.
Je vous passe les détails du code et vous explique comment utiliser le script :

1- Placez le script sur votre ordinateur, à un endroit où vous vous en souviendrez. Pour ma part, je le laisse dans mon dossier *Images, *soit sur Mac OS X à l&#8217;adresse :

<pre>~/Pictures/WordpressBatch.sh</pre>

2- Modifiez le script pour mettre le bon chemin vers votre blog. Prenez par exemple une image d&#8217;un de vos articles, et utilisez cette url.
Pour mon blog, les images sont stockées dans /assets/
Pour le votre, ce sera par défaut http://adresse-de-votre-blog.fr/wp-content/uploads
Pour modifier le script, ouvrez un Terminal ou une console et tapez

<pre>nano ~/Pictures/WordpressBatch.sh</pre>

3- Placez les images que vous souhaitez intégrer dans l&#8217;article dans un seul et même dossier prêt à l&#8217;envoi, et vérifiez que les noms des fichiers ne contiennent pas d&#8217;espaces ! Par exemple, déposez-les dans le dossier *Article-du-jour* sur votre bureau, soit à l&#8217;adresse :

<pre>~/Desktop/Article-du-jour</pre>

4- Ouvrez un Terminal dans Mac OS ou une console sur un Linux quelconque.

5- Exécutez le script en utilisant les paramètres que nous avons donné plus haut :

<pre>sh ~/Pictures/WordpressBatch.sh ~/Desktop/Article-du-jour</pre>

6- Vous n&#8217;avez plus qu&#8217;à vous rendre dans votre dossier *Article du jour, *à copier-coller le code HTML qui se trouve dans *output.txt* dans l&#8217;onglet HTML de votre nouvel article WordPress.
NB : Le dernier paragraphe ne doit pas être copié.

7- Puis importez vos images dans la Bibliothèque WordPress via &#8220;Envoyer/Insérer&#8221;.

&nbsp;

NB2 : vous pouvez simplifier considérablement l&#8217;exécution en plaçant le script dans le même dossier que les images et en vous plaçant dans ce dossier. Voici ce que ça donnerait :

<pre>cd ~/Desktop/Article-du-jour
sh WordPressBatch.sh</pre>

&nbsp;

Et voila !
Téléchargement : [Batch WordPress][1]

[1]: /assets/Batch-Wordpress.zip
 [2]: http://www.willyslens.fr
