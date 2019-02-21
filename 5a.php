<?php

$fname = "5.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
$vowels = "/[aeiou]/";
$dblletters = "/(.)\\1/";
$nice = 0;
for ($i=0; $i<count($lines)-1; $i++) {
    preg_match_all($vowels, $lines[$i], $matches);
    $vows = count($matches[0]);
    $dbl = preg_match($dblletters, $lines[$i]);
    $req3 =  strpos($lines[$i], "ab") !== false ||
             strpos($lines[$i], "cd") !== false ||
             strpos($lines[$i], "pq") !== false ||
             strpos($lines[$i], "xy") !== false;
    echo $vows . ' ' . $dbl . ' ' . ($req3?"True":"False") . PHP_EOL;
    if (($vows > 2) && $dbl && !$req3) {
        $nice++;
    }
}
echo $nice.PHP_EOL;
fclose($fin);

?>
