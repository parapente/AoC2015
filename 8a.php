<?php

$fname = "8.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);
$total = 0;

foreach ($lines as $line) {
    $total += strlen($line);
    /* echo strlen($line)." ".$line." - "; */
    $line = substr($line, 1, strlen($line)-2);
    if (preg_match_all("/\\\\x[0-9a-f]{2}/", $line, $matches)) {
        /* print_r($matches); */
        foreach ($matches[0] as $m) {
            $line =  str_replace($m, chr(hexdec($m)), $line);
        }
    }
    $line = str_replace("\\\\", "\\", $line);
    $line = str_replace("\\\"", "\"", $line);
    $total -= strlen($line);
    /* echo $line.PHP_EOL; */
}
echo $total.PHP_EOL;

fclose($fin);


?>
