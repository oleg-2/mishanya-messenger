<?php

$msg = $_GET["msg"];

if ($msg == "deldel") {
$f = fopen('data.txt', 'w');
fclose($f);
} 
else {
$fp = fopen("data.txt", 'a');
fwrite($fp, "$msg\n");
fclose($fp);
}

?>