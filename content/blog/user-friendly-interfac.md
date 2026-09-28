---
aliases: ["/2013/09/user-friendly-interfac/"]
date: "2013-09-21T00:00:00Z"
description: "Je réalise que je n’avais jamais publié ce brouillon, à propos d’un progrès majeur de mon site Mon site basilesimon.fr est online depuis mai 2011. Son…"
tags: []
title: "De la nécessité d’une interface web plus “user-friendly”"
draft: true
---
*Je réalise que je n&#8217;avais jamais publié ce brouillon, à propos d&#8217;un progrès majeur de mon site*

Mon site [basilesimon.fr][1] est online depuis mai 2011. Son design vise à être aussi simple que possible, suivant le principe K.I.S.S. ([Keep It Simple, Stupid, article sur Wikipedia][2]), et aussi parce que je le considère comme étant une plateforme durable à laquelle je n&#8217;applique que rarement des changements importants.
Cette conception se reflète dans les statistiques: mon blog est environ 7 fois plus consulté que le site principal, principalement parce que ledit site est un catalogue statique de mon travail, là où le blog offre des mises à jour et des activités relayées par les réseaux sociaux.

Même si je me sens aujourd&#8217;hui plus confiant par rapport au HTML/CSS, ce n&#8217;étais pas tout à fait le cas en 2011, et cette raison a aussi participé au choix d&#8217;un design simple.
Quand j&#8217;ai créée ce site, j&#8217;utilisais un Mac. Ce simple fait s&#8217;est en fait révélé être un véritable trouble-fête pour le design !
En effet, le Mac utilisait déjà la technologie dite &#8220;multi-touch&#8221;, qui permettait à différents placements de doigts sur le trackpad de provoquer différentes réactions : un doigt dirige le pointeur de la souris, deux doigts de haut en bas font défiler la page vers le bas&#8230; et deux doigts de gauche à droite la font défiler vers la droite. Je n&#8217;avais pas réalisé l&#8217;impact que cette simple fonctionnalité pourrait avoir.
Cela m&#8217;a mené à créer un site selon une expérience utilisateur qui était la mienne à ce moment-là : la possibilité de faire défiler la page non seulement verticalement, mais aussi horizontalement. Quelle erreur j&#8217;ai faite quand j&#8217;ai codé les pages en alignant les images de gauche à droite sur une simple ligne ! Le mouvement était transparent pour un possesseur d&#8217;un portable Apple&#8230; mais tout sauf pratique pour un utilisateur de PC ou d&#8217;une souris.

[<img src="/assets/screenshot.jpg" alt="" title="screenshot" width="640" height="313" class="aligncenter size-full wp-image-2299" />][3]

Il fallait vraiment que je trouve une solution à ce problème, car l&#8217;on sait tous qu&#8217;une interface non &#8220;user-friendly&#8221; pousse le lecteur à tout faire sauf à rester sur la page. Dans mon cas, pour voir toutes les images, l&#8217;utilisateur qui n&#8217;avait pas le multi-touch devait amener son pointeur de souris sur la barre de défilement en bas de l&#8217;écran et la glisser tout le long de la page. Berk.

Mais la solution était vraiment simple, en fin de compte. Comme mes pages ne demandaient pas de défiler verticalement, il me fallait simplement un script qui convertisse le mouvement de roulette vertical en un mouvement horizontal.
Voilà !

> <pre>/* Copyright 2008 Paul Bennett - http://paulicio.us/
* Scroller.js
* Captures mouse wheel events and runs the ScrollSmoothly
* function based on their output.
* Aims to aid usability by allowing the user to scroll the
* page horizontally smoothly using only their mousewheel.
* Mousewheel event capture by Adomas PaltanaviÄius at http://adomas.org/
*/

function handle(delta) {
if (delta &lt;0) ScrollSmoothly(15,15,'right');
else if (delta >0) ScrollSmoothly(15,15,'left');
else;
}

function wheel(event){var delta = 0;
if (!event) event = window.event;
if (event.wheelDelta) {delta = event.wheelDelta/120;
if (window.opera) delta = -delta;
} else if (event.detail) {delta = -event.detail/3;
}
if (delta) handle(delta);
if (event.preventDefault) event.preventDefault();
event.returnValue = false;
}

var repeatCount = 0;

function ScrollSmoothly(scrollPos,repeatTimes, direction) {if(repeatCount &lt; repeatTimes)
if(direction == 'right')
window.scrollBy(5,0);
else
window.scrollBy(-5,0);
else
{
repeatCount = 0;
clearTimeout(cTimeout);
return;
}
repeatCount++;
cTimeout = setTimeout("ScrollSmoothly('" + scrollPos + "','"+ repeatTimes +"','"+ direction +"')",01);
}

/* Initialization code. */
if (window.addEventListener)
window.addEventListener('DOMMouseScroll', wheel, false);
window.onmousewheel = document.onmousewheel = wheel;
</pre>

Alors merci beaucoup Paul Bennett, ton script m'a beaucoup aidé.
Notons ici qu'il vaut mieux insérer ces quelques lignes de code aussi haut que possible pour qu'il se charge au plus vite. Pour ma part, je l'ai même placé au-dessus du code d'Analytics, dans le tag .
IMPORTANT : le code donné plus haut DOIT être place entre deux balises script.</p>
**ET MAINTENANT UN MOT DES STATISTIQUES**

Le Taux de Rebond est *"le percentage de visites d'une seule page (c.a.d. des visites durant laquelle la personne a quitté le site depuis la page d'entrée sans interagir avec celle-ci)"*, selon Google Analytics. Ce taux était un problème pour moi, car les interactions étaient si compliquées que les lecteurs quittaient la page sans le désir d'en voir plus.
Après l'introduction du script, mon taux de rebond s'est amélioré : d'entre 53% et 76% en août-septembre 2011, il est tombé à environ 35% ces derniers mois.

A propos du temps moyen passé sur la page, il oscille en ce moment entre 00:40 et 01:20, là où en août-septembre 2011 il gravitait entre 00:35 et 00:55. Honnêtement, je suis déçu de ce chiffre, et j'espérais ici un progrès bien plus conséquent.

Toutefois, cette fonctionnalité est une amélioration majeure de l'expérience utilisateur de mon site, en particulier si l'on utilise une souris.

[1]: http://basilesimon.fr
 [2]: http://fr.wikipedia.org/wiki/Principe_KISS
 [3]: /assets/screenshot.jpg
