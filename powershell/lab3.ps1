function getIP{ 
    (get-netipaddress).ipv4address | Select-String "192*" 
} 
$IP = getIP 

function getUser{
    (get-LocalUser).name | Select-String "Admin*"
}
$User = getUser

function getHostname{ 
    (Get-ComputerInfo).CsName
}
$Hostname = getHostname

function getVersion{
    (Get-Host).Version.Major
}
$Version = getVersion

function getDate{
    (Get-Date)
}
$Date = getDate

$Message = "This machine's IP address is $IP. User is $User. Hostname is $Hostname. PowerShell version is $Version. Today's date is $Date"

Write-Host $Message
$Body = $Message

