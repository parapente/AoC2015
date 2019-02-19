<?php

$fname = "4.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$datalen = strlen($data);
$i = 1;
while (substr(md5($data.strval($i)), 0, 5) !== "00000") {
    $i++;
}
echo $i.PHP_EOL;
fclose($fin);

?>
