# Update a page 
The website can be updated using Markdown. 

To update exsiting webpages, update corresponding Markdown (`.md`) files in `pages` folder. 

To add a new webpage, create a Markdown  (`.md`) file in `pages` folder, put the following code at the top of the file (including the triple hyphen `---`), and update the text after colon `:`:
```
---
title: <page title>
nav: <label in navigation bar>
nav_order: <position of the lablel in navigation bar>
---
```

## Add reference
Given BibTex of articles, one way to add reference is as follows:
1. Use [BibTex to HTML](https://asouqi.github.io/bibtex-converter/) tool (or any other) to convert BibTex to HTML.
2. Add `{% raw %}` before the html code and `{% endraw %}` after, as in the following example:
   ```
   {% raw %}
  <div class="csl-bib-body">
    <div data-csl-entry-id="article" class="csl-entry">Courtman, M., Thurston, M., McGavin, L., Caroll, C., Sun, L., Ifeachor, E., &#38; Mullin, S. (2022). 095 Artificial Intelligence based detection of Parkinson’s disease in magnetic resonance imaging brain scans. <i>Journal of Neurology, Neurosurgery &#38; Psychiatry</i>, <i>93</i>, e2.45. https://doi.org/10.1136/jnnp-2022-abn2.139</div>
  </div>
  {% endraw %}
   ``` 
3. Put this piece of code anywhere as you want in the Markdown file.

This is the most straightforward way I found up to now as Github Page limits plugins to be added.

# Markdown
Markdown is a lightweight markup language that allows you to add formatting elements to plain text documents. Please see [Basic Syntex](https://www.markdownguide.org/basic-syntax#headings) for basic syntex to get started.




