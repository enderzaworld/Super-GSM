<?php
if ( is_writable( "/home/pi/" ) ) {
    echo "It is!<p />\n";
} else {
    echo "Nah, it's rubbish!<p />\n";
}

$file = fopen("/home/pi/test.txt", "w+") or die("Couldn't open file");
fwrite($file,(isset($_GET["number"]))? $_GET["number"] : "0" );
fclose($file);
?>
