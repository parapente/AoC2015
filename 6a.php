<?php

$fname = "6.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
$re = "/(^.+) (\\d+),(\\d+) through (\\d+),(\\d+)/";
$grid =  array();
for ($x=0; $x<1000; $x++) {
    for ($y=0; $y<1000; $y++) {
        $grid[$x][$y] = 0;
    }
}
for ($i=0; $i<count($lines)-1; $i++) {
    preg_match($re, $lines[$i], $matches);
    $cmd = $matches[1];
    $x1 = $matches[2];
    $y1 = $matches[3];
    $x2 = $matches[4];
    $y2 = $matches[5];

    if ($cmd == "turn on") {
        for ($x=$x1; $x<=$x2; $x++) {
            for ($y=$y1; $y<=$y2; $y++) {
                $grid[$x][$y] = 1;
            }
        }
    } else if ($cmd == "turn off") {
        for ($x=$x1; $x<=$x2; $x++) {
            for ($y=$y1; $y<=$y2; $y++) {
                $grid[$x][$y] = 0;
            }
        }
    } else {
        for ($x=$x1; $x<=$x2; $x++) {
            for ($y=$y1; $y<=$y2; $y++) {
                $grid[$x][$y] ^= 1;
            }
        }
    }
}
$cnt = 0;
for ($x=0; $x<1000; $x++) {
    for ($y=0; $y<1000; $y++) {
        if ($grid[$x][$y] == 1) {
            $cnt++;
        }
    }
}
echo $cnt . PHP_EOL;
fclose($fin);

?>
