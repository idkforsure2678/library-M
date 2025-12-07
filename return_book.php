<?php
include "db.php";

$id = $_POST["id"];

$sql = "UPDATE books 
        SET borrower_name=NULL, borrower_contact=NULL, borrowed=0 
        WHERE id=$id";

$conn->query($sql);
echo "success";
?>
