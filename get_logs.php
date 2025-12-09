<?php
require "db.php";

header('Content-Type: application/json');

$stmt = $pdo->query("
    SELECT l.id, b.title, b.author, l.borrower_name, l.action, l.action_date
    FROM borrow_log l
    JOIN books b ON l.book_id = b.id
    ORDER BY l.action_date DESC
");

$logs = $stmt->fetchAll(PDO::FETCH_ASSOC);

echo json_encode($logs);
?>
