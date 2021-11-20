import os
import shutil
import glob
import sys, getopt
from bs4 import BeautifulSoup, element

class TranslationException(Exception):
    pass

ELEMENTS = {
    "h1": "\\section{{\\huge{{{content}}}}}",
    "h2": "\\section{{{content}}}",
    "h3": "\\subsection{{{content}}}",
    "h4": "\\subsubsection{{{content}}}",
    "p": "\\par\n{content}\n",
    "dl": "\\begin{{description}}\n{content}\n\\end{{description}}",
    "ol": "\\begin{{enumerate}}\n{content}\n\\end{{enumerate}}",
    "ul": "\\begin{{itemize}}\n{content}\n\\end{{itemize}}",
    "li": "\\item {content}",
    "table": "\\begin{{table}}\n{content}\n\\end{{table}}",
    "em": "\\emph{{{content}}}",
    "i": "\\textit{{{content}}}",
    "b": "\\textbf{{{content}}}",
    "tt": "\\texttt{{{content}}}",
    "pre": "\\verb{{{content}}}",
}

translated_images = []

def translateTable(table:element.Tag)->str:
    tableRows = table.find_all("tr", recursive=False)
    colNum = max([len(i.findChildren(recursive=False)) for i in tableRows])

    outputTableLines = []
    outputTableLines.append("\\begin{tabular}{ "+"c "*colNum+"}")
    for row in tableRows:
        ths = row.findChildren("th")
        tds = row.findChildren("td")
        cells = ths if len(ths)>0 else tds
        outputTableLines.append("&".join([''.join(cell.get_text().split()) for cell in cells])+"\\\\ \\hline")
    outputTableLines.append("\\end{tabular}")
    return '\n'.join(outputTableLines)

def translateImage(baseAddress:str, img:element.Tag)->str:
    src = img["src"]
    width,height = img.attrs.get("height", None), img.attrs.get("width", None)
    options = "[width={width}, height={height}]".format(width=width,height=height)
    r="\\includegraphics"+(options if width and height else "")+"{{{src}}}".format(src="./images/"+os.path.basename(src))
    translated_images.append(baseAddress+src)
    return r

def translateElement(baseAddress:str, element:element.Tag)->str:
    if element.name == "img":
        return translateImage(baseAddress, element)
    elif element.name == "table":
        return translateTable(element)
    else:
        if element.name in ELEMENTS:
            return ELEMENTS[element.name].format(content=element.get_text())
    return ""

def getBaseAddress(bs4:BeautifulSoup) -> str:
    baseAddress = bs4.find("base")
    return baseAddress["href"] if baseAddress else "./"

def removeHeaderFooter(body:element.Tag) -> None:
    print(type(body))
    navBar = body.find("nav", {"class":"navbar"})
    if navBar: navBar.decompose()
    
    footer = body.find("section", {"class":"footer"})
    if footer: footer.decompose()

def HTMLtoTex(bs4:BeautifulSoup) -> str:    
    baseAddress = getBaseAddress(bs4)
    body = bs4.find("body")
    if body==None:
        raise TranslationException
    removeHeaderFooter(body)
    bodyElements = body.findChildren(recursive=True)
    translatedLines = []

    for element in bodyElements:
        translatedLines.append(translateElement(baseAddress, element))
    if len(translatedLines)==0 or not translatedLines: raise TranslationException

    if not os.path.exists("./texOutput/"): os.makedirs("texOutput")
    if len(translated_images)!=0:
        if not os.path.exists("./texOutput/images/"): os.makedirs("texOutput/images")
        for image_path in translated_images:
            shutil.copy2(image_path, "./texOutput/images/")
    
    return '\n'.join(translatedLines)


def createOutput(tex:str, originalPath:str)->None:
    fileName = os.path.basename(originalPath).split(".")[0]
    outputFile = open("./texOutput/{filename}.tex".format(filename=fileName), "w")
    outputFile.write(tex)


def translateFile(name:str)->None:
    file = open(name, encoding="utf-8")
    bs4 = BeautifulSoup(file, features="html.parser")
    tex=None
    try:
        tex = HTMLtoTex(bs4)
        outputTex = '''\\documentclass{{article}}
        \\usepackage{{graphicx}}
        \\begin{{document}}
        {content}
        \\end{{document}}
        '''.format(content=tex)
    
        createOutput(outputTex, name)
        print("{name} file translated to LaTeX!".format(name=name))
    except TranslationException as e:
        print("The file {} could not be translated to LATEX".format(name))
    

def translateAll()->None:
    files = glob.glob("**/*.html",recursive=True)
    for f in files:
        translateFile(f)

if __name__=="__main__":
    optlist = []
    try:
        argv = sys.argv[1:]
        if len(argv)==0:
            print("RAISED")
            raise "error"
        optlist, args = getopt.getopt(argv, "af:", ["all","file"])
    except Exception as e:
        print("Wrong usage! Use the script as:")
        print("python3 ./html-latex.py -f <filename>")
        print("python3 ./html-latex.py -a")
        print("-f <filename>    The file you want to translate to .tex")
        print("-a               Translates all the .html files in the current folder to .tex files")


    for k,v in optlist:
        if k in ("-a", "--all"):
            translateAll()
        elif k in ("-f", "--file"):
            translateFile(v)