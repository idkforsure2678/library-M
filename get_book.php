<?php
require "db.php";

$stmt = $pdo->query("SELECT * FROM books ORDER BY id DESC");
$books = $stmt->fetchAll();

echo json_encode($books);
