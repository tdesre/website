document.addEventListener("DOMContentLoaded", function () {
    const quotes = [
        "Les feuilles de bambou sont utilisées pour fabriquer du papier depuis des siècles.",
        "Les feuilles de chêne peuvent vivre jusqu'à 1 000 ans !",
        "Le plus vieil arbre du monde, un pin Bristlecone, est âgé de plus de 4 800 ans.",
        "Les fruits de l’arbre Baobab sont riches en vitamine C, contenant six fois plus que les oranges.",
        "Le séquoia géant peut atteindre une hauteur de plus de 110 mètres, soit presque la taille d'un immeuble de 40 étages.",
        "Certaines feuilles d'eucalyptus contiennent des huiles essentielles utilisées en médecine et en parfumerie.",
        "Les feuilles de l'arbre à thé sont à l'origine de l'une des boissons les plus consommées au monde : le thé."
    ];
    

    let currentIndex = 0; // Index de la citation actuelle
    const quoteElement = document.getElementById("random-quote");
    const circle = document.querySelector(".progress-ring circle");
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

    // Initialisation de l'anneau
    circle.style.strokeDasharray = `${circumference}`;
    circle.style.strokeDashoffset = `${circumference}`;

    function changeQuote() {
        // Ajoute une classe pour déclencher l’animation de disparition
        quoteElement.classList.add("hidden");

        // Attend la fin de l’animation (1 seconde), puis change la citation
        setTimeout(() => {
            currentIndex = (currentIndex + 1) % quotes.length; // Passer à la citation suivante
            quoteElement.textContent = quotes[currentIndex];

            // Réaffiche la citation avec une animation
            quoteElement.classList.remove("hidden");
        }, 1000); // Temps synchronisé avec la transition CSS

        // Réinitialise et anime le cercle
        circle.style.transition = "none";
        circle.style.strokeDashoffset = `${circumference}`; // Remet à zéro
        setTimeout(() => {
            circle.style.transition = "stroke-dashoffset 10s linear";
            circle.style.strokeDashoffset = `0`; // Remplit progressivement
        }, 10);
    }

    // Change la citation toutes les 10 secondes
    setInterval(changeQuote, 10000);

    // Lance immédiatement l’animation à la fin du chargement
    changeQuote();
});



document.querySelector(".interactive-footer").addEventListener("mouseenter", function () {
    this.style.height = "600px";
});

document.querySelector(".interactive-footer").addEventListener("mouseleave", function () {
    this.style.height = "50px";
});
