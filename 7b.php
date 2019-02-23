<?php

function repush(&$dq, &$cmd)
{
    /* echo "Pushing back..."; */
    /* print_r($cmd); */
    $dq->reverse();
    $dq->push($cmd);
    $dq->reverse();
}

$fname = "7.dat";
$fin = fopen($fname, "r");
$data = fread($fin, filesize($fname));
$lines = explode("\n", $data);
$val = array();

$dq = new \Ds\Deque();
for ($i=0; $i<count($lines)-1; $i++) {
    $ops = array();
    $ops = explode(" ", $lines[$i]);
    $dq->push($ops);
}
$dq->reverse();

while ($dq->count()) {
    $cmd = array();
    $cmd = $dq->pop();
    /* echo "Trying..."; */
    /* print_r($cmd); */
    if ($cmd[1] == "->") {
        $res = 0;
        if (is_numeric($cmd[0])) {
            $res = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[2]] = $res;
    }
    if ($cmd[0] == "NOT") {
        $res = 0;
        if (is_numeric($cmd[1])) {
            $res = intval($cmd[1]);
        } else {
            if (isset($val[$cmd[1]])) {
                $res = $val[$cmd[1]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[3]] = ~$res;
    }
    if ($cmd[1] == "AND") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 & $res2;
    }
    if ($cmd[1] == "OR") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 | $res2;
    }
    if ($cmd[1] == "LSHIFT") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 << $res2;
    }
    if ($cmd[1] == "RSHIFT") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 >> $res2;
    }
}
echo $val["a"].PHP_EOL;
$tmp = $val["a"];
unset($val);
$val = array();
$val["b"] = $tmp;

$dq = new \Ds\Deque();
for ($i=0; $i<count($lines)-1; $i++) {
    $ops = array();
    $ops = explode(" ", $lines[$i]);
    $dq->push($ops);
}
$dq->reverse();

while ($dq->count()) {
    $cmd = array();
    $cmd = $dq->pop();
    /* echo "Trying..."; */
    /* print_r($cmd); */
    if ($cmd[1] == "->") {
        if ($cmd[2] == "b") {
            continue;
        }
        $res = 0;
        if (is_numeric($cmd[0])) {
            $res = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[2]] = $res;
    }
    if ($cmd[0] == "NOT") {
        $res = 0;
        if (is_numeric($cmd[1])) {
            $res = intval($cmd[1]);
        } else {
            if (isset($val[$cmd[1]])) {
                $res = $val[$cmd[1]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[3]] = ~$res;
    }
    if ($cmd[1] == "AND") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 & $res2;
    }
    if ($cmd[1] == "OR") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 | $res2;
    }
    if ($cmd[1] == "LSHIFT") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 << $res2;
    }
    if ($cmd[1] == "RSHIFT") {
        $res1 = 0;
        if (is_numeric($cmd[0])) {
            $res1 = intval($cmd[0]);
        } else {
            if (isset($val[$cmd[0]])) {
                $res1 = $val[$cmd[0]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $res2 = 0;
        if (is_numeric($cmd[2])) {
            $res2 = intval($cmd[2]);
        } else {
            if (isset($val[$cmd[2]])) {
                $res2 = $val[$cmd[2]];
            } else {
                repush($dq, $cmd);
                continue;
            }
        }
        $val[$cmd[4]] = $res1 >> $res2;
    }
}
echo $val["a"].PHP_EOL;
fclose($fin);


?>
