param (
[Parameter(Mandatory=$true)]
[int] $number
)
function Delete-ComputerRestorePoint($SequenceNumber){
	begin{
		$fullName="SystemRestore.DeleteRestorePoint"
		#check if the type is already loaded
		$isLoaded=([AppDomain]::CurrentDomain.GetAssemblies() | ForEach-Object {$_.GetTypes()} | Where-Object {$_.FullName -eq $fullName}) -ne $null
		if (!$isLoaded){
			$SRClient= Add-Type   -memberDefinition  @"
		    	[DllImport ("Srclient.dll")]
		        public static extern int SRRemoveRestorePoint (int index);
"@  -Name DeleteRestorePoint -NameSpace SystemRestore -PassThru
		}
	}
	process{
		 		[SystemRestore.DeleteRestorePoint]::SRRemoveRestorePoint($SequenceNumber)

	}
}

Delete-ComputerRestorePoint($number)