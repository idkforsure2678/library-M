<?php
require "db.php";

$title  = trim($_POST["title"] ?? "");
$author = trim($_POST["author"] ?? "");
$year   = trim($_POST["year"] ?? "");
$id     = $_POST["id"] ?? "";

if ($title === "" || $author === "") {
    http_response_code(400);
    exit("Missing required fields");
}

if ($id === "") {
    $stmt = $pdo->prepare("INSERT INTO books (title, author, year) VALUES (?, ?, ?)");
    $stmt->execute([$title, $author, $year]);
} else {
    $stmt = $pdo->prepare("UPDATE books SET title=?, author=?, year=? WHERE id=?");
    $stmt->execute([$title, $author, $year, $id]);
}
?>
