# fortunes-spam

Fortune cookies taken from subjects and bodies of funny or strange SPAM messages.

It's intended to be used with the [fortune](http://fortunes.cat-v.org/) Unix program.

## Notice

The text of fortunes is obfuscated using rot13, since they are mostly offensive.

## Install

Copy the files 'spam-o' and 'spam-o.dat' in one of the following directory:
 * /usr/local/share/games/fortunes/off/
 * /usr/share/games/fortunes/off/
 * /usr/local/share/games/fortunes/
 * /usr/share/games/fortunes/

or wherever your unix puts fortune files.
In Linux, if you put the files in an "/off/"(ensive) directory the fortune program will read the files only when the "-o" or "-a" option is used (for details: man fortune).

If you're interested in Italian spam, you've to copy also the files 'spam-ita-o' and 'spam-ita-o.dat'.
The charset of both files (spam-o and spam-ita-o) is UTF-8; convert it to suite your system, if needed.

## Update

If you add your own fortunes, you can also update the *.dat* files running **make** (it requires the *strfile* command, usually found in the *fortune-mod* package)

# License

Copyright 2003-2018 Davide Alberani <da@erlug.linux.it>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
