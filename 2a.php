<?php

$fin = fopen("2.dat", "r");
$data = fread($fin, filesize("2.dat"));
$presents = explode("\n", $data);
$paper = 0;
for ($i = 0; $i < count($presents); $i++) {
    if (preg_match("/(\\d+)x(\\d+)x(\\d+)/", $presents[$i], $match)) {
        $l = intval($match[1]);
        $w = intval($match[2]);
        $h = intval($match[3]);
        $box = array($l*$w, $w*$h, $h*$l);
        $paper += min($box);
        foreach ($box as $side) {
            $paper += 2*$side;
        }
    }
}
echo $paper . "\n";
fclose($fin);

?>
