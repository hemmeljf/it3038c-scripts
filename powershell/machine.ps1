$Machines = 'localhost' 

Foreach ($machine in $Machines)  

{ 

$pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 3).CounterSamples.CookedValue 

    $sample = 1 

    foreach ($p in $pt) { 

        "Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample | out-file C:\output.txt

        $sample++ 

    } 

} 
} 