# SublimeText XML tag completion plugin

This plugin is to convert the following XML file
```xml
<html>
<head></>
<body></>
</html>
```
to this:
```xml
<html>
<head></head>
<body></body>
</html>
```
It replaces </> with the corresponding tag name.

## Installation
* Package control:
  Use [Package Control](https://packagecontrol.io/) and search for 
  "CompleteXmlTag".
* Manually:
  Go to `Sublime Text → Preferences → Browse Packages` and clone the repo to
  this directory and rename the  repo folder to `CompleteXmlTag`.

## Usage
* Open the command pallette and type `complete close tag`.
* Click `Sublime Text → Selection → Format → Complete Close Tag`.

## Config
Not only the `xml` file can be formatted by this package, it also supports
other XML-based file type. Just by modifying the settings file this way:
```json
{
    "file_selectors": ["text.xml", "text.html"]
}
```
and the `html` file can also be formatted.

## License
This software is distributed under MIT license (see [License](./LICENSE) for
details).
