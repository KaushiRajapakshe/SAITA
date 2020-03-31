param (
[Parameter(Mandatory=$true)]
[string] $MainServiceName
)
$ServiceInput = ""
$CurrentService = ""
$Service = ""

function Custom-Stop-Service ($ServiceInput)
{
	Write-Host "Name of `$ServiceInput: $($ServiceInput.Name)"
	Write-Host "Number of dependents: $($ServiceInput.DependentServices.Count)"
	If ($ServiceInput.DependentServices.Count -gt 0)
	{
		ForEach ($Service in $ServiceInput.DependentServices)
		{
			Write-Host "Dependent of $($ServiceInput.Name): $($Service.Name)"
			If ($Service.Status -eq "Running")
			{
				Write-Host "$($Service.Name) is running."
				$CurrentService = Get-Service -Name $Service.Name
				
				Custom-Stop-Service $CurrentService
				Write-Host "Stopping service $($CurrentService.Name)"
				Stop-Service -Name $CurrentService.Name -Force
			}
			Else
			{
				Write-Host "$($Service.Name) is stopped."
			}
			
		}
		Stop-Service -Name $MainServiceName
			Write-Host "Service $($MainService.Name) is Successfully stopped."
	}
	Else
	{
		Write-Host "Stopping service $($ServiceInput.Name)"
		Stop-Service -Name $ServiceInput.Name
	}
}

$MainService = Get-Service -Name $MainServiceName

If ($MainService.Status -eq "Stopped")
{
	Write-Host "Service $($MainService.Name) is already stopped."
}
Else
{
	Custom-Stop-Service $MainService
}
