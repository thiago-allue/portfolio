# Pandoc

- https://pandoc.org/

## Download and Installation

- https://github.com/jgm/pandoc/releases

## Docs

- https://pandoc.org/MANUAL.html

## Usual command line

- `pandoc "File Name.md" -o "File Name.pdf"`
- `pandoc "File Name.md" -o "File Name.pdf" -V geometry:margin=2cm`
- `pandoc --variable classoption=twocolumn paper.md -o paper.pdf`
- `pandoc --toc --variable classoption=twocolumn paper.md -o paper.pdf`
- `pandoc -f html https://www.website.com -o website.pdf -V geometry:margin=2cm`
- `pandoc --toc -V toc-title:"Table of Contents" content.md -o content.pdf -V geometry:margin=2cm --webtex`
- `pandoc --filter pandoc-citeproc --bibliography=paper.bib --variable --classoption=twocolumn --variable papersize=a4paper -s paper.md -o paper.pdf`
- `pandoc --filter pandoc-citeproc --bibliography=paper.bib --variable --classoption=twocolumn --variable papersize=a4paper -s paper.md -t latex -o paper.txt`
- `pandoc chap1.md chap2.md chap3.md metadata.yaml -s -o book.html`