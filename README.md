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
2. Add `{% raw %}` before the html code and `{% endraw %}` after, as following:
   ```
   {% raw %}
   <your html code>
   {% endraw %}
   ``` 
3. Put this piece of code anywhere as you want in the Markdown file.

This is the most straightforward way I found up to now as Github Page limits plugins to be added.

# Markdown
Markdown is a lightweight markup language that allows you to add formatting elements to plain text documents. Please see [Basic Syntex](https://www.markdownguide.org/basic-syntax#headings) for basic syntex to get started.


# Build locally
1. Clone the repo to local folder
2. Install [Jekyll](https://jekyllrb.com/docs/installation/)
3. Run `jekyll s` in the root directory of the repo

# This template
If you would like to know more about this template, please see the [tutorial](https://evanwill.github.io/go-go-ghpages-b/).
