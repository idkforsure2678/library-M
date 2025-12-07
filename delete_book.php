<?php
include "db.php";

$id = $_POST["id"];
$conn->query("DELETE FROM books WHERE id=$id");

echo "success";
?>
