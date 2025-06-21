param( [string] $File)

function findNoASCIICharacters {

    param(
            [parameter(Mandatory = $true)] [string] $File
    )

    Get-Content $File | Where-Object {$_ -cmatch '[^\x20-\x7F]'}

}

findNoASCIICharacters $File
