# [Genealogical Data Communication](https://www.familysearch.org/en/wiki/GEDCOM)

- Used for loading between softwares and not ideal for reading
- There are GITs for validating the data in .ged files
- It's like a 

## sample

```gedcom
sample.ged
0 HEAD
1 SOUR PAF
2 NAME Personal Ancestral File
2 VERS 5.0
1 DATE 30 NOV 2000
1 GEDC
2 VERS 5.5
2 FORM LINEAGE-LINKED
1 CHAR ANSEL
1 SUBM @U1@
0 @I1@ INDI
1 NAME John /Smith/
1 SEX M
1 FAMS @F1@
0 @I2@ INDI
1 NAME Elizabeth /Stansfield/
1 SEX F
1 FAMS @F1@
0 @I3@ INDI
1 NAME James /Smith/
1 SEX M
1 FAMC @F1@
0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 MARR
1 CHIL @I3@
0 @U1@ SUBM
1 NAME Submitter
0 TRLR
```

# python-gedcom module
- Useful for navigating hierarchy and pulling certain tags.

# Problem: determing ancestral relationship
## Least Common Ancestor
### Definition
- Root of tree at top
- LCA = lowest level common node
- Necessary for finding distance between nodes
### Eulerian Path Method

![image](https://github.com/andrewdavis23/gedcom/assets/47924318/4f1fbbbe-7911-4d10-ab39-ddbf2ce9eacf)

![image](https://github.com/andrewdavis23/gedcom/assets/47924318/39253446-8423-4248-89db-b5643e731a88)

So, you need to store the ID of the node which would be the INDI number in the GEDCOM file.  What about the depth?  How do you get that out of a GEDCOM file?

![image](https://github.com/andrewdavis23/gedcom/assets/47924318/cf34c3f5-57a1-4d9a-af56-96c875766b84)

Then you find the minimum depth between the two indices in the Eulerian tour. Take the indice of that value and use it to find the ID of the node.



## Getting the Names Sorted

## Compound Relationships
- double cousins

## research links
- [PHP Code](https://stackoverflow.com/questions/1063666/calculate-family-relationship-from-genealogical-data)
- [Eulerian Path Video](https://www.bing.com/videos/riverview/relatedvideo?q=method+for+finding+least+common+ancestor&mid=A5D73A4339196F91690BA5D73A4339196F91690B)
