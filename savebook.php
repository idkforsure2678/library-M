<?php
include "db.php";

$title = $_POST["title"];
$author = $_POST["author"];
$year = $_POST["year"];
$id = $_POST["id"];

if ($id == "") {
    $sql = "INSERT INTO books (title, author, year) VALUES ('$title', '$author', '$year')";
} else {
    $sql = "UPDATE books SET title='$title', author='$author', year='$year' WHERE id=$id";
}

$conn->query($sql);
echo "success";
?>
