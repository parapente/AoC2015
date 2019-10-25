<?php

$fname = "9.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
unset($lines[count($lines)-1]);
$dist = array();
$perms = array();
$uniq = new \Ds\Set();

function perm(&$p, $dest, $l, $r)
{
    if ($l == $r) {
        $row = count($p);
        $i = 0;
        foreach ($dest as $d) {
            $p[$row][$i] = $d;
            $i++;
        }
    } else {
        for ($i=$l; $i<=$r; $i++) {
            [$dest[$l], $dest[$i]] = [$dest[$i], $dest[$l]];
            perm($p, $dest, $l+1, $r);
            [$dest[$l], $dest[$i]] = [$dest[$i], $dest[$l]];
        }
    }
}

function find_longest($perms, $dist)
{
    $max = 0;
    $maxpath = array();

    foreach ($perms as $p) {
        $distance = 0;
        $prevnode = "";
        foreach ($p as $node) {
            $tmp = 0;
            if (array_key_exists($prevnode, $dist)) {
                if (array_key_exists($node, $dist[$prevnode])) {
                    $tmp = $dist[$prevnode][$node];
                    $distance += $tmp;
                }
            }
            if (array_key_exists($node, $dist)) {
                if (array_key_exists($prevnode, $dist[$node])) {
                    $tmp = $dist[$node][$prevnode];
                    $distance += $tmp;
                }
            }
            $prevnode = $node;
        }
        if ($distance > $max) {
            $max = $distance;
            $maxpath = $p;
        }
    }
    foreach ($maxpath as $node) {
        echo $node." ";
    }
    echo ": ".$max.PHP_EOL;
}

foreach ($lines as $line) {
    if (preg_match_all("/(\\w+) to (\\w+) = (\\d+)/", $line, $matches)) {
        /* print_r($matches); */
        $dist[$matches[1][0]][$matches[2][0]] = $matches[3][0];
        $uniq->add($matches[1][0]);
        $uniq->add($matches[2][0]);
    }
    /* echo $line.PHP_EOL; */
}
/* print_r($uniq); */
$destinations = $uniq->toArray();
perm($perms, $destinations, 0, count($destinations)-1);
/* echo count($perms).PHP_EOL; */
find_longest($perms, $dist);

fclose($fin);


?>
