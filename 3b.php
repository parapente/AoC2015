<?php

class Point
{
    public $x;
    public $y;

    public function __construct()
    {
        $this->x = 0;
        $this->y = 0;
    }
}

$fin = fopen("3.dat", "r");
$data = fread($fin, filesize("3.dat"));
$datalen = strlen($data);
$house = array();
$x = 0;
$y = 0;
$santa = new Point();
$robosanta = new Point();
$house["0x0"] = 1;
for ($i = 0; $i < $datalen; $i++) {
    if (($i % 2) == 0) {
        $santa_ref = $santa;
    } else {
        $santa_ref =  $robosanta;
    }
    switch ($data[$i]) {
    case '>':
        $santa_ref->x++;
        break;
    case '<':
        $santa_ref->x--;
        break;
    case '^':
        $santa_ref->y++;
        break;
    case 'v':
        $santa_ref->y--;
        break;
    }
    $x = $santa_ref->x;
    $y = $santa_ref->y;
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
