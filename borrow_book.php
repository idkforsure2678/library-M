<?php
include "db.php";

$id = $_POST["id"];
$name = $_POST["name"];
$contact = $_POST["contact"];

$sql = "UPDATE books 
        SET borrower_name='$name', borrower_contact='$contact', borrowed=1 
        WHERE id=$id";

$conn->query($sql);
echo "success";
?>
