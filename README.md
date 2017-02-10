# Skeletorfw's Challenge Generator
SCG is a challenge XML generator for Binding of Isaac Afterbirth+.

It aims to provide an easy way to create valid challenge XML files using a simple interface or pasteable seed.

### Notes
#### IDs
The item IDs were stripped from the HTML source of the PlatinumGod ( <3 to elucidator). To do this, a mixture of bash scripting, text editor magic, and eventually excel were all used.

1. Firstly the source HTML was copied into a text file and split into segments for Items & Trinkets.
2. Next this text file was de-crudded to return only lines containing the ID or name, using bash:

```egrep 'item-title|TrinketID' PG_Dump_Items.txt >> Items_Strip1.txt```

3. This file was then opened using a text editor. The html tags were stripped out and a comma was added between the pairs.
4. Next the Item IDs were shifted to the beginning of the line using awk:

```awk -F',' '{ print $2","$1 }' Items_Strip1.txt >> Items_Strip2.txt```

5. And finally the list was sorted by item ID to make everything logical for import later.

(Eventually I will possibly store all this data in a sqlite database to keep it all compact)

### Thanks
A great thanks to the following people for creating the resources which has made this possible:
* DD [The Dignitary] - for creating the original XML challenge guide I followed to write this tool.
* elucidator - for the fantastic PlatinumGod.com site.

### Links

* [Platinum God](http://platinumgod.co.uk/) - Information on all the mechanics and items in the game.
* [How to create a custom challenge - Afterbirth+](http://steamcommunity.com/sharedfiles/filedetails/?id=835061601) - The original challenge XML guide.