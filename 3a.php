<?php

$fin = fopen("3.dat", "r");
$data = fread($fin, filesize("3.dat"));
$datalen = strlen($data);
$house = array();
$x = 0;
$y = 0;
for ($i = 0; $i < $datalen; $i++) {
    switch ($data[$i]) {
    case '>':
        $x++;
        break;
    case '<':
        $x--;
        break;
    case '^':
        $y++;
        break;
    case 'v':
        $y--;
        break;
    }
    $key = strval($x).'x'.strval($y);
    if (!array_key_exists($key, $house)) {
        $house[$key] = 1;
    } else {
        $house[$key]++;
    }
}
echo count($house) . "\n";
fclose($fin);

?>
