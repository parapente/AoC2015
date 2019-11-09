<?php

$fname = "12.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);

$total = 0;
preg_match_all("/(-*\\d+)/", $lines[0], $matches);
for ($i=0; $i<count($matches[0]); $i++) {
    $total += $matches[0][$i];
}

echo "Total: ".$total.PHP_EOL;
fclose($fin);

?>
