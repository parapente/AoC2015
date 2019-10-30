<?php

function incr(&$curpass)
{
    $i = 7;
    $remainder = 1;
    while($i > 0) {
        if ($remainder) {
            if ($curpass[$i] == 'z') {
                $curpass[$i] = 'a';
            }
            else {
                $curpass[$i] = $curpass[$i] + 1;
                $remainder  = 0;
            }
        }
        $i--;
    }
}

function chkpass($curpass)
{
    $stage2pass = true;
    for ($i=0;$i<strlen($curpass);$i++) {
        if ($curpass[$i] == 'i' || $curpass[$i] == 'o' || $curpass[$i] == 'l')
            $stage2pass = false;
    }
    if ($stage2pass == false)
        return false;
    $prev = 0;
    $stage1pass = false;
    $count = 0;
}

function find_next_passwd($curpass)
{
    incr($curpass);
    while (!chkpass($curpass)) {
        incr($curpass);
    }
    return $curpass;
}

$fname = "11.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);

$curpass = $lines[0];
$newpass = find_next_passwd($curpass);
echo strlen($newpass).PHP_EOL;

fclose($fin);


?>
