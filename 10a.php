<?php

function readnum($n)
{
    $prev = '';
    $count = 0;
    $newnum = "";
    for ($j=0; $j<strlen($n); $j++) {
        if ($prev === '') {
            $prev = $n[$j];
            $count = 1;
        } else if ($prev === $n[$j]) {
            $count++;
        } else {
            $newnum .= strval($count).$prev;
            $prev = $n[$j];
            $count = 1;
        }
    }
    $newnum .= strval($count).$prev;
    return($newnum);
}

$fname = "10.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);

$num = $lines[0];
for ($i=0; $i<40; $i++) {
    $nextnum = readnum($num);
    $num = $nextnum;
}
echo strlen($num).PHP_EOL;

fclose($fin);


?>
