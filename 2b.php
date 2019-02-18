<?php

$fin = fopen("2.dat", "r");
$data = fread($fin, filesize("2.dat"));
$presents = explode("\n", $data);
$ribbon = 0;
for ($i = 0; $i < count($presents); $i++) {
    if (preg_match("/(\\d+)x(\\d+)x(\\d+)/", $presents[$i], $match)) {
        $l = intval($match[1]);
        $w = intval($match[2]);
        $h = intval($match[3]);
        $box = array(2*$l+2*$w, 2*$w+2*$h, 2*$h+2*$l);
        $ribbon += min($box) + $l*$w*$h;
    }
}
echo $ribbon . "\n";
fclose($fin);

?>
