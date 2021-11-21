# Installation
The scripts use some packages that are not installed by default. In order to install the required packages you can run:
` pip install -r requirements.txt `

# Broken links finder
The broken links finder script is `./broken-links-finder.py`.
The program will look for the broken links in *all* the HTML pages located in the same root folder of the script. The script does not follow links between pages, it checks that every link in every .html file works.
The script can be run with:
` python3 ./broken-links-finder.py` or
`python ./broken-links-finder.py`

# HTML to LaTeX converter
The HTML to LaTeX converter is called `./html-latex.py`.
The script converts one or many HTML files to .tex files, containing the most important information of the webpage (text, titles, images, tables, etc.).
The output files will be stored in the directory `./texOutput/`: the TEX files will have the same name as the HTML files, while the images needed by the files will be copied inside the folder `./texOutput/images/`.

### Convert a single file
The script can be used to convert a single file:
`python3 ./html-latex.py [-f <path> | --file <path>]` or
`python ./html-latex.py [-f <path> | --file <path>]`

### Convert multiple files
The script can be also used to convert all the files in the directory of the script:
`python3 ./html-latex.py [-a | --all]` or
`python ./html-latex.py [-a | --all]`
