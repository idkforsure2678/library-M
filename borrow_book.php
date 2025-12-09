<?php
require "db.php";

$id = $_POST["id"] ?? "";
$borrower = trim($_POST["borrower_name"] ?? "");

if ($id === "" || $borrower === "") {
    http_response_code(400);
    exit("Invalid borrow data");
}

/* Mark book as borrowed */
$stmt = $pdo->prepare("
    UPDATE books 
    SET borrowed = 1, borrower_name = ? 
    WHERE id = ?
");
$stmt->execute([$borrower, $id]);

/* Log borrow action */
$log = $pdo->prepare("
    INSERT INTO borrow_log (book_id, borrower_name, action)
    VALUES (?, ?, 'borrow')
");
$log->execute([$id, $borrower]);
?>
