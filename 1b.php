<?php

$fin = fopen("1.dat", "r");
$data = fread($fin, filesize("1.dat"));
$floor = 0;
$pos = 1;
for ($i = 0; $i < strlen($data); $i++) {
    if ($data[$i] === "(") {
        $floor++;
    }
    if ($data[$i] === ")") {
        $floor--;
    }
    if ($floor === -1) {
        echo $pos;
        break;
    }
    $pos++;
}
fclose($fin);

?>
