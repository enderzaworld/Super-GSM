<?php
$file = fopen("test.txt","w");
echo fwrite($file,$_GET["number"]);
fclose($file);
?>