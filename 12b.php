<?php

function dosum($json)
{
    $subtotal = 0;

    if (is_object($json)) {
        foreach ($json as $key => $value) {
            if (is_int($value)) {
                $subtotal += $value;
            }
            if (is_string($value) && ($value === "red"))
                return 0;
            if (is_array($value) || is_object($value)) {
                $subtotal += dosum($value);
            }
        }
    }
    if (is_array($json)) {
        foreach ($json as $value) {
            if (is_int($value)) {
                $subtotal += $value;
            }
            if (is_array($value) || is_object($value)) {
                $subtotal += dosum($value);
            }
        }
    }
    return $subtotal;
}

$fname = "12.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);

$json = json_decode($lines[0]);
$total = dosum($json);
echo "Total: ".$total.PHP_EOL;

fclose($fin);

?>
