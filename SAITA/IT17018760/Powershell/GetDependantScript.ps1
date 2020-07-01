param (
[Parameter(Mandatory=$true)]
[string] $MainServiceName
)

$Scount = (Get-Service -Name $MainServiceName -DependentServices).Count

return $Scount





