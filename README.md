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
## Update home page
Markdown file for home page is `index.md`. Follow the above instructions to update the page.

## Add news
To add a news, create a new file in folder `news/_posts` with name format `yyyy-mm-dd-<name>.md` eg `2023-10-09-aneurysm-clip.md`. Once the file is created, the corresponding news card should appeared in the News page. 

The file should contain the following header:
```
---
layout: news
author: <author>
title: <title>
thumbnail: <thumbnail image path, which should be saved as /assets/img/news_thumbnail_<name>.png>
excerpt_separator: <!--more-->
---
```
 - Only author, title, and thumbnail needs configuration. 
 - It's recommended to resize/crop the thumbnail image to 640x640 pixels.
 - `excerpt_separator` allows showing a part of the news content (excerpt) in the news card. Use `<!--more-->` to separate out the excerpt (the text before it will be excerpt).
 - It's easier to copy the code in previous news file and edit based on it.

## Add projects
Similar to adding news, create a new file in folder `projects/_posts` with name format `yyyy-mm-dd-<name>.md` eg `2023-10-08-stroke.md`. The date can be used to arrange the order of the project cards in the Projects page, it doesn't matter which exactly date chosen. 

The file should contain the following header:
```
---
layout: project
title: <full title of the project>
thumbnail_title: <title appears in the project card>
thumbnail: <thumbnail image path, which should be saved as /assets/img/projects_thumbnail_<name>.png>
brief: <a brief introduction to the project, which will be shown in the project card>
---
```
 - Only title, thumbnail_title, thumbnail and brief needs configuration. 
 - It's recommended to resize/crop the thumbnail image to 640x640 pixels.
 - It's easier to copy the code in previous project file and edit based on it.

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

# Useful things
## Useful commands
### padding images
convert filename -gravity center -background "rgb(255,255,255)" -extent 640x640 filename 

