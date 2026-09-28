Add-Type -AssemblyName System.Drawing
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')
$out = Join-Path $root 'output\rev005-interior-remediation-v07'
$qa = Join-Path $out 'qa'
$wide = Get-ChildItem $qa -Filter '*_A_CONTEXT.png' | Sort-Object Name
$tileW=320; $tileH=200; $cols=3; $rowsPerSheet=9
for($offset=0; $offset -lt $wide.Count; $offset += $rowsPerSheet) {
  $slice=$wide | Select-Object -Skip $offset -First $rowsPerSheet
  $bmp = New-Object System.Drawing.Bitmap ([int]($tileW*$cols)),([int]($tileH*$slice.Count))
  $g=[System.Drawing.Graphics]::FromImage($bmp); $g.Clear([System.Drawing.Color]::FromArgb(22,28,32))
  for($r=0; $r -lt $slice.Count; $r++) {
    $base=$slice[$r].Name.Substring(0,$slice[$r].Name.Length-('_A_CONTEXT.png').Length)
    $files=@("${base}_A_CONTEXT.png","${base}_B_FUNCTIONAL.png","${base}_C_SEQUENCE.png")
    for($c=0; $c -lt $files.Count; $c++) {
      $p=Join-Path $qa $files[$c]
      if(Test-Path $p) { $im=[System.Drawing.Image]::FromFile($p); $rect=[System.Drawing.Rectangle]::new([int]($c*$tileW),[int]($r*$tileH),[int]$tileW,[int]$tileH); $g.DrawImage($im,$rect); $im.Dispose() }
    }
  }
  $idx=[int]($offset/$rowsPerSheet)+1; $path=Join-Path $out ('CONTACT_SHEET_{0:D2}.png' -f $idx); $bmp.Save($path,[System.Drawing.Imaging.ImageFormat]::Png); $g.Dispose(); $bmp.Dispose()
}
Get-ChildItem $out -Filter 'CONTACT_SHEET_*.png' | Select-Object -ExpandProperty FullName
