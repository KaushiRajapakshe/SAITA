param (
[Parameter(Mandatory=$true)]
[string] $MainServiceName
)
$ServiceInput = ""
$CurrentService = ""
$Service = ""



function Custom-Start-Service ($ServiceInput)
{
	Write-Host "Name of `$ServiceInput: $($ServiceInput.Name)"
	Write-Host "Number of dependents: $($ServiceInput.DependentServices.Count)"
	If ($ServiceInput.DependentServices.Count -gt 0)
	{
		ForEach ($Service in $ServiceInput.DependentServices)
		{
			Write-Host "Dependent of $($ServiceInput.Name): $($Service.Name)"
			If ($Service.Status -eq "Stopped")
			{
				Write-Host "$($Service.Name) is stopped now."
				$CurrentService = Get-Service -Name $Service.Name
				
				Custom-Start-Service $CurrentService
				
				Start-Service -Name $CurrentService.Name 
			}
			Else
			{
				Write-Host "$($Service.Name) is Started."
			}
			
		}
			Start-Service -Name $MainServiceName
			Write-Host "Service $($MainService.Name) is Successfully Running."
			exit
	}
	Else
	{
		Write-Host "Started service $($ServiceInput.Name)"
		Start-Service -Name $ServiceInput.Name
	}
}

$MainService = Get-Service -Name $MainServiceName

If ($MainService.Status -eq "Running")
{
	Write-Host "Service $($MainService.Name) is already Started."
}
Else
{
	Custom-Start-Service $MainService
}
