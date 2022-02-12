## Introduction

Powershell is a convenient scripting language to help  

## Summary


## Defining parameters

<pre>

$customParameters = New-Object PSObject -Property @{
    task_name = "logfile-import"
    task_command = "C:\Temp\temp.bat"
    working_directory = "C:\Temp"
}

Write-Host "Parameters in 1 line are: Name: $($customParameters.task_name) Command: $($customParameters.task_command) Work Dir: $($customParameters.working_directory)" -ForegroundColor Green

Write-Host "Parameters are: `nName: $($customParameters.task_name) `nCommand: $($customParameters.task_command) `nWork Dir: $($customParameters.working_directory)" -ForegroundColor Green

</pre>


https://stackoverflow.com/questions/15113413/how-do-i-concatenate-strings-and-variables-in-powershell
https://www.microsoft.com/en-us/download/details.aspx?id=36389
https://devblogs.microsoft.com/scripting/powertip-new-lines-with-powershell/

## Scheduled Task


<pre>
$customParameters = New-Object PSObject -Property @{
    task_name = "logfile-import"
    task_command = "C:\Temp\temp.bat"
    working_directory = "C:\Temp"
    task_trigger = "-Daily -At 9am"

}

$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument $($customParameters.task_command)
echo "$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument C:\Temp\temp.bat"
Write-Host '($action)'

</pre>

https://www.windowscentral.com/how-create-scheduled-tasks-powershell-windows-10
https://devblogs.microsoft.com/scripting/use-powershell-to-create-scheduled-tasks/
