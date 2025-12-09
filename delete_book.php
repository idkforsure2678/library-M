<?php
require "db.php";

$id = $_POST["id"] ?? "";

if ($id === "") {
    http_response_code(400);
    exit("Invalid book ID");
}

$stmt = $pdo->prepare("DELETE FROM books WHERE id=?");
$stmt->execute([$id]);
?>
