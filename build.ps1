pyinstaller -n pmdrc-randomizer --onefile --console src\main.py
$compress = @{
	Path = "dist\pmdrc-randomizer.exe", "config.json"
	DestinationPath = "windows.zip"
}
Compress-Archive @compress
