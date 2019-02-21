<?php

$fname = "5.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
$dblletters = "/(..).*\\1/";
$dblletters2 = "/(.).\\1/";
$nice = 0;
for ($i=0; $i<count($lines)-1; $i++) {
    $dbl = preg_match($dblletters, $lines[$i]);
    $dbl2 = preg_match($dblletters2, $lines[$i]);
    echo $dbl . ' ' . $dbl2 . PHP_EOL;
    if ($dbl && $dbl2) {
        $nice++;
    }
}
echo $nice.PHP_EOL;
fclose($fin);

?>
