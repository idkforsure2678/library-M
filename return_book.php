<?php
require "db.php";

$id = $_POST["id"] ?? "";

if ($id === "") {
    http_response_code(400);
    exit("Invalid book ID");
}

$stmt = $pdo->prepare("SELECT borrower_name FROM books WHERE id=?");
$stmt->execute([$id]);
$book = $stmt->fetch();

$borrower = $book["borrower_name"] ?? "";

$pdo->prepare("
    UPDATE books 
    SET borrowed = 0, borrower_name = NULL 
    WHERE id = ?
")->execute([$id]);

$pdo->prepare("
    INSERT INTO borrow_log (book_id, borrower_name, action)
    VALUES (?, ?, 'return')
")->execute([$id, $borrower]);

?>
