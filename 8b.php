<?php

$fname = "8.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);
$total = 0;

foreach ($lines as $line) {
    $total -= strlen($line);
    /* echo strlen($line)." ".$line." - "; */
    $line = str_replace("\\", "\\\\", $line);
    $line = str_replace("\"", "\\\"", $line);
    $line = "\"".$line."\"";
    $total += strlen($line);
    /* echo $line.PHP_EOL; */
}
echo $total.PHP_EOL;

fclose($fin);


?>
