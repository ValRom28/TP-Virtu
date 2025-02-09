<?php
$servername = "db";
$username = "root";
$password = "motdepasse";
$dbname = "ma_base_de_donnees";
$cached = "depuis la base de données";

// Connexion à MySQL
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Échec de la connexion : " . $conn->connect_error);
}

// Connexion à Redis
$redis = new Redis();
$redis->connect('redis', 6379);

// Vérifier si les données sont en cache
$cachedData = $redis->get("objets");
if ($cachedData) {
    $objets = json_decode($cachedData, true);
    $cached = "depuis le cache";
} else {
    $sql = "SELECT * FROM objets";
    $result = $conn->query($sql);

    $objets = [];
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $objets[] = $row;
        }
    }

    // Mettre en cache les résultats pendant 60 secondes
    $redis->set("objets", json_encode($objets), 60);
}

// Affichage stylisé des objets
echo "<h1>Liste des objets ($cached)</h1>";

if (!empty($objets)) {
    echo "<table border='1' cellpadding='5' cellspacing='0' style='border-collapse: collapse; width: 50%;'>";
    echo "<tr><th>Nom</th><th>Email</th></tr>";

    foreach ($objets as $objet) {
        echo "<tr><td>{$objet["nom"]}</td><td>{$objet["prix"]}€</td></tr>";
    }

    echo "</table>";
} else {
    echo "<p>Aucun objet trouvé.</p>";
}

$conn->close();
?>
