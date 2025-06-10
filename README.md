<style>
  .docx-wrapper>section.docx { background: white; box-shadow: 0 0 1px rgba(0, 0, 0, 0.8);width:96%!important;margin: 0 auto;margin-top:calc(30px); }
  .docx { color: black; }
  section.docx { box-sizing: border-box; display: flex; flex-flow: column nowrap; position: relative; overflow: hidden; }
  section.docx>article { margin-bottom: auto; }
  .docx table { border-collapse: collapse; }
  .docx table td, .docx table th { vertical-align: top;}
  .docx p { margin: 0pt; min-height: 1em; }
  .docx span { white-space: pre-wrap; overflow-wrap: break-word; }
  .docx a { color: inherit; text-decoration: inherit; }
</style>
<style>
  .docx {
    --docx-majorHAnsi-font: Calibri Light;
    --docx-minorHAnsi-font: Calibri;
    --docx-dk1-color: #000000;
    --docx-lt1-color: #FFFFFF;
    --docx-dk2-color: #44546A;
    --docx-lt2-color: #E7E6E6;
    --docx-accent1-color: #4472C4;
    --docx-accent2-color: #ED7D31;
    --docx-accent3-color: #A5A5A5;
    --docx-accent4-color: #FFC000;
    --docx-accent5-color: #5B9BD5;
    --docx-accent6-color: #70AD47;
    --docx-hlink-color: #0563C1;
    --docx-folHlink-color: #954F72;
  }
</style>
<style>
  .docx span {
    font-family: var(--docx-minorHAnsi-font);
    min-height: 11.00pt;
    font-size: 11.00pt;
  }
  .docx p {
    margin-bottom: 6.00pt;
    line-height: 1.15;
  }
  .docx p, p.docx_normal span {
    font-family: Calibri;
    color: #000000;
  }
  p.docx_heading1 {
    margin-bottom: 0.00pt;
    text-indent: -0.50pt;
    margin-left: 0.50pt;
    margin-right: 35.40pt;
    text-align: center;
  }
  p.docx_heading1 span {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx_heading1 span {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx_heading2 {
    margin-bottom: 11.10pt;
    text-indent: -0.50pt;
    margin-left: 0.50pt;
  }
  p.docx_heading2 span {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 13.00pt;
    font-size: 13.00pt;
  }
  p.docx_heading2 span {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 13.00pt;
    font-size: 13.00pt;
  }
  p.docx_heading3 {
    margin-top: 2.00pt;
    margin-bottom: 0.00pt;
  }
  p.docx_heading3 span {
    font-family: var(--docx-majorHAnsi-font);
    color: #1F3763;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  p.docx_heading3 span {
    font-family: var(--docx-majorHAnsi-font);
    color: #1F3763;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  p.docx_heading4 {
    margin-top: 2.00pt;
    margin-bottom: 0.00pt;
  }
  p.docx_heading4 span {
    font-family: var(--docx-majorHAnsi-font);
    font-style: italic;
    color: #2F5496;
  }
  p.docx_heading4 span {
    font-family: var(--docx-majorHAnsi-font);
    font-style: italic;
    color: #2F5496;
  }
  p.docx_heading5 {
    margin-top: 2.00pt;
    margin-bottom: 0.00pt;
  }
  p.docx_heading5 span {
    font-family: var(--docx-majorHAnsi-font);
    color: #2F5496;
  }
  p.docx_heading5 span {
    font-family: var(--docx-majorHAnsi-font);
    color: #2F5496;
  }
  .docx table, table.docx_tablenormal td {
    padding-top: 0.00pt;
    padding-left: 5.40pt;
    padding-bottom: 0.00pt;
    padding-right: 5.40pt;
  }
  span.docx_heading2char {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 13.00pt;
    font-size: 13.00pt;
  }
  span.docx_heading2char p {
    margin-bottom: 11.10pt;
    text-indent: -0.50pt;
    margin-left: 0.50pt;
  }
  span.docx_heading2char {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 13.00pt;
    font-size: 13.00pt;
  }
  span.docx_heading1char {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  span.docx_heading1char p {
    margin-bottom: 0.00pt;
    text-indent: -0.50pt;
    margin-left: 0.50pt;
    margin-right: 35.40pt;
    text-align: center;
  }
  span.docx_heading1char {
    font-family: Times New Roman;
    font-weight: bold;
    color: #000000;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx_listparagraph {
    margin-left: 36.00pt;
  }
  p.docx_listparagraph span {
    font-family: Calibri;
    color: #000000;
  }
  p.docx_nospacing {
    margin-bottom: 0.00pt;
    line-height: 1.00;
  }
  p.docx_nospacing span {
    font-family: Calibri;
    color: #000000;
  }
  span.docx_heading3char {
    font-family: var(--docx-majorHAnsi-font);
    color: #1F3763;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  span.docx_heading3char p {
    margin-top: 2.00pt;
    margin-bottom: 0.00pt;
  }
  span.docx_heading3char {
    font-family: var(--docx-majorHAnsi-font);
    color: #1F3763;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  span.docx_strong {
    font-weight: bold;
  }
  span.docx_emphasis {
    font-style: italic;
  }
  span.docx_hyperlink {
    color: #0563C1;
    text-decoration: underline;
  }
  span.docx_unresolvedmention {
    color: #605E5C;
    background-color: #E1DFDD;
  }
  p.docx_tocheading {
    margin-top: 12.00pt;
    text-indent: 0.00pt;
    margin-left: 0.00pt;
    margin-right: 0.00pt;
    text-align: left;
    margin-bottom: 0.00pt;
  }
  p.docx_tocheading span {
    font-family: var(--docx-majorHAnsi-font);
    font-weight: normal;
    color: #2F5496;
    min-height: 16.00pt;
    font-size: 16.00pt;
  }
  p.docx_toc1 {
    margin-bottom: 5.00pt;
  }
  p.docx_toc1 span {
    font-family: Calibri;
    color: #000000;
  }
  p.docx_toc3 {
    margin-bottom: 5.00pt;
    margin-left: 22.00pt;
  }
  p.docx_toc3 span {
    font-family: Calibri;
    color: #000000;
  }
  span.docx_heading5char {
    font-family: var(--docx-majorHAnsi-font);
    color: #2F5496;
  }
  span.docx_heading5char p {
    margin-top: 2.00pt;
    margin-bottom: 0.00pt;
  }
  span.docx_heading5char {
    font-family: var(--docx-majorHAnsi-font);
    color: #2F5496;
  }
  span.docx_heading4char {
    font-family: var(--docx-majorHAnsi-font);
    font-style: italic;
    color: #2F5496;
  }
  span.docx_heading4char p {
    margin-top: 2.00pt;
    margin-bottom: 0.00pt;
  }
  span.docx_heading4char {
    font-family: var(--docx-majorHAnsi-font);
    font-style: italic;
    color: #2F5496;
  }
  p.docx_pw-post-body-paragraph {
    margin-top: 5.00pt;
    margin-bottom: 5.00pt;
    line-height: 1.00;
  }
  p.docx_pw-post-body-paragraph span {
    font-family: Times New Roman;
    color: black;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  span.docx_followedhyperlink {
    color: #954F72;
    text-decoration: underline;
  }
  p.docx_header {
    margin-bottom: 0.00pt;
    line-height: 1.00;
  }
  p.docx_header span {
    font-family: Calibri;
    color: #000000;
  }
  p.docx_header span {
    font-family: Calibri;
    color: #000000;
  }
  span.docx_headerchar {
    font-family: Calibri;
    color: #000000;
  }
  span.docx_headerchar p {
    margin-bottom: 0.00pt;
    line-height: 1.00;
  }
  span.docx_headerchar {
    font-family: Calibri;
    color: #000000;
  }
  p.docx_footer {
    margin-bottom: 0.00pt;
    line-height: 1.00;
  }
  p.docx_footer span {
    font-family: Calibri;
    color: #000000;
  }
  p.docx_footer span {
    font-family: Calibri;
    color: #000000;
  }
  span.docx_footerchar {
    font-family: Calibri;
    color: #000000;
  }
  span.docx_footerchar p {
    margin-bottom: 0.00pt;
    line-height: 1.00;
  }
  span.docx_footerchar {
    font-family: Calibri;
    color: #000000;
  }
  table.docx_tablegrid p {
    margin-bottom: 0.00pt;
    line-height: 1.00;
  }
  table.docx_tablegrid td {
    border-top: 0.50pt solid black;
    border-left: 0.50pt solid black;
    border-bottom: 0.50pt solid black;
    border-right: 0.50pt solid black;
    padding-top: 0.00pt;
    padding-left: 5.40pt;
    padding-bottom: 0.00pt;
    padding-right: 5.40pt;
  }
  p.docx_caption {
    margin-bottom: 10.00pt;
    line-height: 1.00;
  }
  p.docx_caption span {
    font-style: italic;
    color: #44546A;
    min-height: 9.00pt;
    font-size: 9.00pt;
    font-family: Calibri;
  }
</style>
<style>
  p.docx-num-25-0:before {
    content: ""counter(docx-num-25-0, decimal)".\9";
    counter-increment: docx-num-25-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-25-0 {
    counter-reset: docx-num-25-1;
  }
  p.docx-num-25-1:before {
    content: "o\9";
    counter-increment: docx-num-25-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-25-1 {
    counter-reset: docx-num-25-2;
  }
  p.docx-num-25-2:before {
    content: "\9";
    counter-increment: docx-num-25-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-25-2 {
    counter-reset: docx-num-25-3;
  }
  p.docx-num-25-3:before {
    content: "\9";
    counter-increment: docx-num-25-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-25-3 {
    counter-reset: docx-num-25-4;
  }
  p.docx-num-25-4:before {
    content: "\9";
    counter-increment: docx-num-25-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-25-4 {
    counter-reset: docx-num-25-5;
  }
  p.docx-num-25-5:before {
    content: "\9";
    counter-increment: docx-num-25-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-25-5 {
    counter-reset: docx-num-25-6;
  }
  p.docx-num-25-6:before {
    content: "\9";
    counter-increment: docx-num-25-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-25-6 {
    counter-reset: docx-num-25-7;
  }
  p.docx-num-25-7:before {
    content: "\9";
    counter-increment: docx-num-25-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-25-7 {
    counter-reset: docx-num-25-8;
  }
  p.docx-num-25-8:before {
    content: "\9";
    counter-increment: docx-num-25-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-25-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-21-0:before {
    content: "\9";
    counter-increment: docx-num-21-0;
    font-family: Symbol;
  }
  p.docx-num-21-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-21-0 {
    counter-reset: docx-num-21-1;
  }
  p.docx-num-21-1:before {
    content: ""counter(docx-num-21-1, decimal)".\9";
    counter-increment: docx-num-21-1;
  }
  p.docx-num-21-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-21-1 {
    counter-reset: docx-num-21-2;
  }
  p.docx-num-21-2:before {
    content: ""counter(docx-num-21-2, decimal)".\9";
    counter-increment: docx-num-21-2;
  }
  p.docx-num-21-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-21-2 {
    counter-reset: docx-num-21-3;
  }
  p.docx-num-21-3:before {
    content: ""counter(docx-num-21-3, decimal)".\9";
    counter-increment: docx-num-21-3;
  }
  p.docx-num-21-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-21-3 {
    counter-reset: docx-num-21-4;
  }
  p.docx-num-21-4:before {
    content: ""counter(docx-num-21-4, decimal)".\9";
    counter-increment: docx-num-21-4;
  }
  p.docx-num-21-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-21-4 {
    counter-reset: docx-num-21-5;
  }
  p.docx-num-21-5:before {
    content: ""counter(docx-num-21-5, decimal)".\9";
    counter-increment: docx-num-21-5;
  }
  p.docx-num-21-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-21-5 {
    counter-reset: docx-num-21-6;
  }
  p.docx-num-21-6:before {
    content: ""counter(docx-num-21-6, decimal)".\9";
    counter-increment: docx-num-21-6;
  }
  p.docx-num-21-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-21-6 {
    counter-reset: docx-num-21-7;
  }
  p.docx-num-21-7:before {
    content: ""counter(docx-num-21-7, decimal)".\9";
    counter-increment: docx-num-21-7;
  }
  p.docx-num-21-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-21-7 {
    counter-reset: docx-num-21-8;
  }
  p.docx-num-21-8:before {
    content: ""counter(docx-num-21-8, decimal)".\9";
    counter-increment: docx-num-21-8;
  }
  p.docx-num-21-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-20-0:before {
    content: ""counter(docx-num-20-0, decimal)".\9";
    counter-increment: docx-num-20-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-20-0 {
    counter-reset: docx-num-20-1;
  }
  p.docx-num-20-1:before {
    content: "o\9";
    counter-increment: docx-num-20-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-20-1 {
    counter-reset: docx-num-20-2;
  }
  p.docx-num-20-2:before {
    content: "\9";
    counter-increment: docx-num-20-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-20-2 {
    counter-reset: docx-num-20-3;
  }
  p.docx-num-20-3:before {
    content: "\9";
    counter-increment: docx-num-20-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-20-3 {
    counter-reset: docx-num-20-4;
  }
  p.docx-num-20-4:before {
    content: "\9";
    counter-increment: docx-num-20-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-20-4 {
    counter-reset: docx-num-20-5;
  }
  p.docx-num-20-5:before {
    content: "\9";
    counter-increment: docx-num-20-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-20-5 {
    counter-reset: docx-num-20-6;
  }
  p.docx-num-20-6:before {
    content: "\9";
    counter-increment: docx-num-20-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-20-6 {
    counter-reset: docx-num-20-7;
  }
  p.docx-num-20-7:before {
    content: "\9";
    counter-increment: docx-num-20-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-20-7 {
    counter-reset: docx-num-20-8;
  }
  p.docx-num-20-8:before {
    content: "\9";
    counter-increment: docx-num-20-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-20-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-18-0:before {
    content: "\9";
    counter-increment: docx-num-18-0;
    font-family: Symbol;
    min-height: 11.00pt;
    font-size: 11.00pt;
  }
  p.docx-num-18-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-18-0 {
    counter-reset: docx-num-18-1;
  }
  p.docx-num-18-1:before {
    content: "o\9";
    counter-increment: docx-num-18-1;
    font-family: Courier New;
  }
  p.docx-num-18-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-18-1 {
    counter-reset: docx-num-18-2;
  }
  p.docx-num-18-2:before {
    content: "\9";
    counter-increment: docx-num-18-2;
    font-family: Wingdings;
  }
  p.docx-num-18-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-18-2 {
    counter-reset: docx-num-18-3;
  }
  p.docx-num-18-3:before {
    content: "\9";
    counter-increment: docx-num-18-3;
    font-family: Symbol;
  }
  p.docx-num-18-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-18-3 {
    counter-reset: docx-num-18-4;
  }
  p.docx-num-18-4:before {
    content: "o\9";
    counter-increment: docx-num-18-4;
    font-family: Courier New;
  }
  p.docx-num-18-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-18-4 {
    counter-reset: docx-num-18-5;
  }
  p.docx-num-18-5:before {
    content: "\9";
    counter-increment: docx-num-18-5;
    font-family: Wingdings;
  }
  p.docx-num-18-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-18-5 {
    counter-reset: docx-num-18-6;
  }
  p.docx-num-18-6:before {
    content: "\9";
    counter-increment: docx-num-18-6;
    font-family: Symbol;
  }
  p.docx-num-18-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-18-6 {
    counter-reset: docx-num-18-7;
  }
  p.docx-num-18-7:before {
    content: "o\9";
    counter-increment: docx-num-18-7;
    font-family: Courier New;
  }
  p.docx-num-18-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-18-7 {
    counter-reset: docx-num-18-8;
  }
  p.docx-num-18-8:before {
    content: "\9";
    counter-increment: docx-num-18-8;
    font-family: Wingdings;
  }
  p.docx-num-18-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-39-0:before {
    content: ""counter(docx-num-39-0, decimal)".\9";
    counter-increment: docx-num-39-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-39-0 {
    counter-reset: docx-num-39-1;
  }
  p.docx-num-39-1:before {
    content: "o\9";
    counter-increment: docx-num-39-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-39-1 {
    counter-reset: docx-num-39-2;
  }
  p.docx-num-39-2:before {
    content: "\9";
    counter-increment: docx-num-39-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-39-2 {
    counter-reset: docx-num-39-3;
  }
  p.docx-num-39-3:before {
    content: "\9";
    counter-increment: docx-num-39-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-39-3 {
    counter-reset: docx-num-39-4;
  }
  p.docx-num-39-4:before {
    content: "\9";
    counter-increment: docx-num-39-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-39-4 {
    counter-reset: docx-num-39-5;
  }
  p.docx-num-39-5:before {
    content: "\9";
    counter-increment: docx-num-39-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-39-5 {
    counter-reset: docx-num-39-6;
  }
  p.docx-num-39-6:before {
    content: "\9";
    counter-increment: docx-num-39-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-39-6 {
    counter-reset: docx-num-39-7;
  }
  p.docx-num-39-7:before {
    content: "\9";
    counter-increment: docx-num-39-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-39-7 {
    counter-reset: docx-num-39-8;
  }
  p.docx-num-39-8:before {
    content: "\9";
    counter-increment: docx-num-39-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-39-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-14-0:before {
    content: ""counter(docx-num-14-0, lower-alpha)".\9";
    counter-increment: docx-num-14-0;
  }
  p.docx-num-14-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-14-0 {
    counter-reset: docx-num-14-1;
  }
  p.docx-num-14-1:before {
    content: ""counter(docx-num-14-1, lower-alpha)".\9";
    counter-increment: docx-num-14-1;
  }
  p.docx-num-14-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-14-1 {
    counter-reset: docx-num-14-2;
  }
  p.docx-num-14-2:before {
    content: ""counter(docx-num-14-2, lower-roman)".\9";
    counter-increment: docx-num-14-2;
  }
  p.docx-num-14-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-14-2 {
    counter-reset: docx-num-14-3;
  }
  p.docx-num-14-3:before {
    content: ""counter(docx-num-14-3, decimal)".\9";
    counter-increment: docx-num-14-3;
  }
  p.docx-num-14-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-14-3 {
    counter-reset: docx-num-14-4;
  }
  p.docx-num-14-4:before {
    content: ""counter(docx-num-14-4, lower-alpha)".\9";
    counter-increment: docx-num-14-4;
  }
  p.docx-num-14-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-14-4 {
    counter-reset: docx-num-14-5;
  }
  p.docx-num-14-5:before {
    content: ""counter(docx-num-14-5, lower-roman)".\9";
    counter-increment: docx-num-14-5;
  }
  p.docx-num-14-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-14-5 {
    counter-reset: docx-num-14-6;
  }
  p.docx-num-14-6:before {
    content: ""counter(docx-num-14-6, decimal)".\9";
    counter-increment: docx-num-14-6;
  }
  p.docx-num-14-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-14-6 {
    counter-reset: docx-num-14-7;
  }
  p.docx-num-14-7:before {
    content: ""counter(docx-num-14-7, lower-alpha)".\9";
    counter-increment: docx-num-14-7;
  }
  p.docx-num-14-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-14-7 {
    counter-reset: docx-num-14-8;
  }
  p.docx-num-14-8:before {
    content: ""counter(docx-num-14-8, lower-roman)".\9";
    counter-increment: docx-num-14-8;
  }
  p.docx-num-14-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-41-0:before {
    content: ""counter(docx-num-41-0, decimal)".\9";
    counter-increment: docx-num-41-0;
  }
  p.docx-num-41-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-41-0 {
    counter-reset: docx-num-41-1;
  }
  p.docx-num-41-1:before {
    content: ""counter(docx-num-41-1, lower-alpha)".\9";
    counter-increment: docx-num-41-1;
  }
  p.docx-num-41-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-41-1 {
    counter-reset: docx-num-41-2;
  }
  p.docx-num-41-2:before {
    content: ""counter(docx-num-41-2, lower-roman)".\9";
    counter-increment: docx-num-41-2;
  }
  p.docx-num-41-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-41-2 {
    counter-reset: docx-num-41-3;
  }
  p.docx-num-41-3:before {
    content: ""counter(docx-num-41-3, decimal)".\9";
    counter-increment: docx-num-41-3;
  }
  p.docx-num-41-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-41-3 {
    counter-reset: docx-num-41-4;
  }
  p.docx-num-41-4:before {
    content: ""counter(docx-num-41-4, lower-alpha)".\9";
    counter-increment: docx-num-41-4;
  }
  p.docx-num-41-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-41-4 {
    counter-reset: docx-num-41-5;
  }
  p.docx-num-41-5:before {
    content: ""counter(docx-num-41-5, lower-roman)".\9";
    counter-increment: docx-num-41-5;
  }
  p.docx-num-41-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-41-5 {
    counter-reset: docx-num-41-6;
  }
  p.docx-num-41-6:before {
    content: ""counter(docx-num-41-6, decimal)".\9";
    counter-increment: docx-num-41-6;
  }
  p.docx-num-41-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-41-6 {
    counter-reset: docx-num-41-7;
  }
  p.docx-num-41-7:before {
    content: ""counter(docx-num-41-7, lower-alpha)".\9";
    counter-increment: docx-num-41-7;
  }
  p.docx-num-41-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-41-7 {
    counter-reset: docx-num-41-8;
  }
  p.docx-num-41-8:before {
    content: ""counter(docx-num-41-8, lower-roman)".\9";
    counter-increment: docx-num-41-8;
  }
  p.docx-num-41-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-12-0:before {
    content: "\9";
    counter-increment: docx-num-12-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-12-0 {
    counter-reset: docx-num-12-1;
  }
  p.docx-num-12-1:before {
    content: "o\9";
    counter-increment: docx-num-12-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-12-1 {
    counter-reset: docx-num-12-2;
  }
  p.docx-num-12-2:before {
    content: "\9";
    counter-increment: docx-num-12-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-12-2 {
    counter-reset: docx-num-12-3;
  }
  p.docx-num-12-3:before {
    content: "\9";
    counter-increment: docx-num-12-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-12-3 {
    counter-reset: docx-num-12-4;
  }
  p.docx-num-12-4:before {
    content: "\9";
    counter-increment: docx-num-12-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-12-4 {
    counter-reset: docx-num-12-5;
  }
  p.docx-num-12-5:before {
    content: "\9";
    counter-increment: docx-num-12-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-12-5 {
    counter-reset: docx-num-12-6;
  }
  p.docx-num-12-6:before {
    content: "\9";
    counter-increment: docx-num-12-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-12-6 {
    counter-reset: docx-num-12-7;
  }
  p.docx-num-12-7:before {
    content: "\9";
    counter-increment: docx-num-12-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-12-7 {
    counter-reset: docx-num-12-8;
  }
  p.docx-num-12-8:before {
    content: "\9";
    counter-increment: docx-num-12-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-12-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-11-0:before {
    content: "\9";
    counter-increment: docx-num-11-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-11-0 {
    counter-reset: docx-num-11-1;
  }
  p.docx-num-11-1:before {
    content: "o\9";
    counter-increment: docx-num-11-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-11-1 {
    counter-reset: docx-num-11-2;
  }
  p.docx-num-11-2:before {
    content: "\9";
    counter-increment: docx-num-11-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-11-2 {
    counter-reset: docx-num-11-3;
  }
  p.docx-num-11-3:before {
    content: "\9";
    counter-increment: docx-num-11-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-11-3 {
    counter-reset: docx-num-11-4;
  }
  p.docx-num-11-4:before {
    content: "\9";
    counter-increment: docx-num-11-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-11-4 {
    counter-reset: docx-num-11-5;
  }
  p.docx-num-11-5:before {
    content: "\9";
    counter-increment: docx-num-11-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-11-5 {
    counter-reset: docx-num-11-6;
  }
  p.docx-num-11-6:before {
    content: "\9";
    counter-increment: docx-num-11-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-11-6 {
    counter-reset: docx-num-11-7;
  }
  p.docx-num-11-7:before {
    content: "\9";
    counter-increment: docx-num-11-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-11-7 {
    counter-reset: docx-num-11-8;
  }
  p.docx-num-11-8:before {
    content: "\9";
    counter-increment: docx-num-11-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-11-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-16-0:before {
    content: ""counter(docx-num-16-0, decimal)".\9";
    counter-increment: docx-num-16-0;
    font-weight: bold;
    min-height: 12.00pt;
    font-size: 12.00pt;
    text-decoration: none;
  }
  p.docx-num-16-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 18.00pt;
  }
  p.docx-num-16-0 {
    counter-reset: docx-num-16-1;
  }
  p.docx-num-16-1:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)".\9";
    counter-increment: docx-num-16-1;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  p.docx-num-16-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -21.60pt;
    margin-left: 39.60pt;
  }
  p.docx-num-16-1 {
    counter-reset: docx-num-16-2;
  }
  p.docx-num-16-2:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)".\9";
    counter-increment: docx-num-16-2;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  p.docx-num-16-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -25.20pt;
    margin-left: 61.20pt;
  }
  p.docx-num-16-2 {
    counter-reset: docx-num-16-3;
  }
  p.docx-num-16-3:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)"."counter(docx-num-16-3, decimal)".\9";
    counter-increment: docx-num-16-3;
  }
  p.docx-num-16-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -32.40pt;
    margin-left: 86.40pt;
  }
  p.docx-num-16-3 {
    counter-reset: docx-num-16-4;
  }
  p.docx-num-16-4:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)"."counter(docx-num-16-3, decimal)"."counter(docx-num-16-4, decimal)".\9";
    counter-increment: docx-num-16-4;
  }
  p.docx-num-16-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -39.60pt;
    margin-left: 111.60pt;
  }
  p.docx-num-16-4 {
    counter-reset: docx-num-16-5;
  }
  p.docx-num-16-5:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)"."counter(docx-num-16-3, decimal)"."counter(docx-num-16-4, decimal)"."counter(docx-num-16-5, decimal)".\9";
    counter-increment: docx-num-16-5;
  }
  p.docx-num-16-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -46.80pt;
    margin-left: 136.80pt;
  }
  p.docx-num-16-5 {
    counter-reset: docx-num-16-6;
  }
  p.docx-num-16-6:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)"."counter(docx-num-16-3, decimal)"."counter(docx-num-16-4, decimal)"."counter(docx-num-16-5, decimal)"."counter(docx-num-16-6, decimal)".\9";
    counter-increment: docx-num-16-6;
  }
  p.docx-num-16-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-16-6 {
    counter-reset: docx-num-16-7;
  }
  p.docx-num-16-7:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)"."counter(docx-num-16-3, decimal)"."counter(docx-num-16-4, decimal)"."counter(docx-num-16-5, decimal)"."counter(docx-num-16-6, decimal)"."counter(docx-num-16-7, decimal)".\9";
    counter-increment: docx-num-16-7;
  }
  p.docx-num-16-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -61.20pt;
    margin-left: 187.20pt;
  }
  p.docx-num-16-7 {
    counter-reset: docx-num-16-8;
  }
  p.docx-num-16-8:before {
    content: ""counter(docx-num-16-0, decimal)"."counter(docx-num-16-1, decimal)"."counter(docx-num-16-2, decimal)"."counter(docx-num-16-3, decimal)"."counter(docx-num-16-4, decimal)"."counter(docx-num-16-5, decimal)"."counter(docx-num-16-6, decimal)"."counter(docx-num-16-7, decimal)"."counter(docx-num-16-8, decimal)".\9";
    counter-increment: docx-num-16-8;
  }
  p.docx-num-16-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-36-0:before {
    content: ""counter(docx-num-36-0, decimal)".\9";
    counter-increment: docx-num-36-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-36-0 {
    counter-reset: docx-num-36-1;
  }
  p.docx-num-36-1:before {
    content: "o\9";
    counter-increment: docx-num-36-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-36-1 {
    counter-reset: docx-num-36-2;
  }
  p.docx-num-36-2:before {
    content: "\9";
    counter-increment: docx-num-36-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-36-2 {
    counter-reset: docx-num-36-3;
  }
  p.docx-num-36-3:before {
    content: "\9";
    counter-increment: docx-num-36-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-36-3 {
    counter-reset: docx-num-36-4;
  }
  p.docx-num-36-4:before {
    content: "\9";
    counter-increment: docx-num-36-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-36-4 {
    counter-reset: docx-num-36-5;
  }
  p.docx-num-36-5:before {
    content: "\9";
    counter-increment: docx-num-36-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-36-5 {
    counter-reset: docx-num-36-6;
  }
  p.docx-num-36-6:before {
    content: "\9";
    counter-increment: docx-num-36-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-36-6 {
    counter-reset: docx-num-36-7;
  }
  p.docx-num-36-7:before {
    content: "\9";
    counter-increment: docx-num-36-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-36-7 {
    counter-reset: docx-num-36-8;
  }
  p.docx-num-36-8:before {
    content: "\9";
    counter-increment: docx-num-36-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-36-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-31-0:before {
    content: ""counter(docx-num-31-0, decimal)"\9";
    counter-increment: docx-num-31-0;
  }
  p.docx-num-31-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.60pt;
    margin-left: 18.60pt;
  }
  p.docx-num-31-0 {
    counter-reset: docx-num-31-1;
  }
  p.docx-num-31-1:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"\9";
    counter-increment: docx-num-31-1;
  }
  p.docx-num-31-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.60pt;
    margin-left: 18.60pt;
  }
  p.docx-num-31-1 {
    counter-reset: docx-num-31-2;
  }
  p.docx-num-31-2:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"\9";
    counter-increment: docx-num-31-2;
  }
  p.docx-num-31-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -36.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-31-2 {
    counter-reset: docx-num-31-3;
  }
  p.docx-num-31-3:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"."counter(docx-num-31-3, decimal)"\9";
    counter-increment: docx-num-31-3;
  }
  p.docx-num-31-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-31-3 {
    counter-reset: docx-num-31-4;
  }
  p.docx-num-31-4:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"."counter(docx-num-31-3, decimal)"."counter(docx-num-31-4, decimal)"\9";
    counter-increment: docx-num-31-4;
  }
  p.docx-num-31-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-31-4 {
    counter-reset: docx-num-31-5;
  }
  p.docx-num-31-5:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"."counter(docx-num-31-3, decimal)"."counter(docx-num-31-4, decimal)"."counter(docx-num-31-5, decimal)"\9";
    counter-increment: docx-num-31-5;
  }
  p.docx-num-31-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-31-5 {
    counter-reset: docx-num-31-6;
  }
  p.docx-num-31-6:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"."counter(docx-num-31-3, decimal)"."counter(docx-num-31-4, decimal)"."counter(docx-num-31-5, decimal)"."counter(docx-num-31-6, decimal)"\9";
    counter-increment: docx-num-31-6;
  }
  p.docx-num-31-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-31-6 {
    counter-reset: docx-num-31-7;
  }
  p.docx-num-31-7:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"."counter(docx-num-31-3, decimal)"."counter(docx-num-31-4, decimal)"."counter(docx-num-31-5, decimal)"."counter(docx-num-31-6, decimal)"."counter(docx-num-31-7, decimal)"\9";
    counter-increment: docx-num-31-7;
  }
  p.docx-num-31-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -90.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-31-7 {
    counter-reset: docx-num-31-8;
  }
  p.docx-num-31-8:before {
    content: ""counter(docx-num-31-0, decimal)"."counter(docx-num-31-1, decimal)"."counter(docx-num-31-2, decimal)"."counter(docx-num-31-3, decimal)"."counter(docx-num-31-4, decimal)"."counter(docx-num-31-5, decimal)"."counter(docx-num-31-6, decimal)"."counter(docx-num-31-7, decimal)"."counter(docx-num-31-8, decimal)"\9";
    counter-increment: docx-num-31-8;
  }
  p.docx-num-31-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -90.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-4-0:before {
    content: "\9";
    counter-increment: docx-num-4-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-4-0 {
    counter-reset: docx-num-4-1;
  }
  p.docx-num-4-1:before {
    content: "o\9";
    counter-increment: docx-num-4-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-4-1 {
    counter-reset: docx-num-4-2;
  }
  p.docx-num-4-2:before {
    content: "\9";
    counter-increment: docx-num-4-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-4-2 {
    counter-reset: docx-num-4-3;
  }
  p.docx-num-4-3:before {
    content: "\9";
    counter-increment: docx-num-4-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-4-3 {
    counter-reset: docx-num-4-4;
  }
  p.docx-num-4-4:before {
    content: "\9";
    counter-increment: docx-num-4-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-4-4 {
    counter-reset: docx-num-4-5;
  }
  p.docx-num-4-5:before {
    content: "\9";
    counter-increment: docx-num-4-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-4-5 {
    counter-reset: docx-num-4-6;
  }
  p.docx-num-4-6:before {
    content: "\9";
    counter-increment: docx-num-4-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-4-6 {
    counter-reset: docx-num-4-7;
  }
  p.docx-num-4-7:before {
    content: "\9";
    counter-increment: docx-num-4-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-4-7 {
    counter-reset: docx-num-4-8;
  }
  p.docx-num-4-8:before {
    content: "\9";
    counter-increment: docx-num-4-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-4-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-5-0:before {
    content: "\9";
    counter-increment: docx-num-5-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-5-0 {
    counter-reset: docx-num-5-1;
  }
  p.docx-num-5-1:before {
    content: "o\9";
    counter-increment: docx-num-5-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-5-1 {
    counter-reset: docx-num-5-2;
  }
  p.docx-num-5-2:before {
    content: "\9";
    counter-increment: docx-num-5-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-5-2 {
    counter-reset: docx-num-5-3;
  }
  p.docx-num-5-3:before {
    content: "\9";
    counter-increment: docx-num-5-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-5-3 {
    counter-reset: docx-num-5-4;
  }
  p.docx-num-5-4:before {
    content: "\9";
    counter-increment: docx-num-5-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-5-4 {
    counter-reset: docx-num-5-5;
  }
  p.docx-num-5-5:before {
    content: "\9";
    counter-increment: docx-num-5-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-5-5 {
    counter-reset: docx-num-5-6;
  }
  p.docx-num-5-6:before {
    content: "\9";
    counter-increment: docx-num-5-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-5-6 {
    counter-reset: docx-num-5-7;
  }
  p.docx-num-5-7:before {
    content: "\9";
    counter-increment: docx-num-5-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-5-7 {
    counter-reset: docx-num-5-8;
  }
  p.docx-num-5-8:before {
    content: "\9";
    counter-increment: docx-num-5-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-5-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-2-0:before {
    content: "\9";
    counter-increment: docx-num-2-0;
    font-family: Symbol;
  }
  p.docx-num-2-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-2-0 {
    counter-reset: docx-num-2-1;
  }
  p.docx-num-2-1:before {
    content: "o\9";
    counter-increment: docx-num-2-1;
    font-family: Courier New;
  }
  p.docx-num-2-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-2-1 {
    counter-reset: docx-num-2-2;
  }
  p.docx-num-2-2:before {
    content: "\9";
    counter-increment: docx-num-2-2;
    font-family: Wingdings;
  }
  p.docx-num-2-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-2-2 {
    counter-reset: docx-num-2-3;
  }
  p.docx-num-2-3:before {
    content: "\9";
    counter-increment: docx-num-2-3;
    font-family: Symbol;
  }
  p.docx-num-2-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-2-3 {
    counter-reset: docx-num-2-4;
  }
  p.docx-num-2-4:before {
    content: "o\9";
    counter-increment: docx-num-2-4;
    font-family: Courier New;
  }
  p.docx-num-2-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-2-4 {
    counter-reset: docx-num-2-5;
  }
  p.docx-num-2-5:before {
    content: "\9";
    counter-increment: docx-num-2-5;
    font-family: Wingdings;
  }
  p.docx-num-2-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-2-5 {
    counter-reset: docx-num-2-6;
  }
  p.docx-num-2-6:before {
    content: "\9";
    counter-increment: docx-num-2-6;
    font-family: Symbol;
  }
  p.docx-num-2-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-2-6 {
    counter-reset: docx-num-2-7;
  }
  p.docx-num-2-7:before {
    content: "o\9";
    counter-increment: docx-num-2-7;
    font-family: Courier New;
  }
  p.docx-num-2-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-2-7 {
    counter-reset: docx-num-2-8;
  }
  p.docx-num-2-8:before {
    content: "\9";
    counter-increment: docx-num-2-8;
    font-family: Wingdings;
  }
  p.docx-num-2-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-13-0:before {
    content: "\9";
    counter-increment: docx-num-13-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-13-0 {
    counter-reset: docx-num-13-1;
  }
  p.docx-num-13-1:before {
    content: "o\9";
    counter-increment: docx-num-13-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-13-1 {
    counter-reset: docx-num-13-2;
  }
  p.docx-num-13-2:before {
    content: "\9";
    counter-increment: docx-num-13-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-13-2 {
    counter-reset: docx-num-13-3;
  }
  p.docx-num-13-3:before {
    content: "\9";
    counter-increment: docx-num-13-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-13-3 {
    counter-reset: docx-num-13-4;
  }
  p.docx-num-13-4:before {
    content: "\9";
    counter-increment: docx-num-13-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-13-4 {
    counter-reset: docx-num-13-5;
  }
  p.docx-num-13-5:before {
    content: "\9";
    counter-increment: docx-num-13-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-13-5 {
    counter-reset: docx-num-13-6;
  }
  p.docx-num-13-6:before {
    content: "\9";
    counter-increment: docx-num-13-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-13-6 {
    counter-reset: docx-num-13-7;
  }
  p.docx-num-13-7:before {
    content: "\9";
    counter-increment: docx-num-13-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-13-7 {
    counter-reset: docx-num-13-8;
  }
  p.docx-num-13-8:before {
    content: "\9";
    counter-increment: docx-num-13-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-13-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-29-0:before {
    content: ""counter(docx-num-29-0, decimal)".\9";
    counter-increment: docx-num-29-0;
  }
  p.docx-num-29-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-29-0 {
    counter-reset: docx-num-29-1;
  }
  p.docx-num-29-1:before {
    content: ""counter(docx-num-29-1, decimal)".\9";
    counter-increment: docx-num-29-1;
  }
  p.docx-num-29-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-29-1 {
    counter-reset: docx-num-29-2;
  }
  p.docx-num-29-2:before {
    content: ""counter(docx-num-29-2, decimal)".\9";
    counter-increment: docx-num-29-2;
  }
  p.docx-num-29-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-29-2 {
    counter-reset: docx-num-29-3;
  }
  p.docx-num-29-3:before {
    content: ""counter(docx-num-29-3, decimal)".\9";
    counter-increment: docx-num-29-3;
  }
  p.docx-num-29-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-29-3 {
    counter-reset: docx-num-29-4;
  }
  p.docx-num-29-4:before {
    content: ""counter(docx-num-29-4, decimal)".\9";
    counter-increment: docx-num-29-4;
  }
  p.docx-num-29-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-29-4 {
    counter-reset: docx-num-29-5;
  }
  p.docx-num-29-5:before {
    content: ""counter(docx-num-29-5, decimal)".\9";
    counter-increment: docx-num-29-5;
  }
  p.docx-num-29-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-29-5 {
    counter-reset: docx-num-29-6;
  }
  p.docx-num-29-6:before {
    content: ""counter(docx-num-29-6, decimal)".\9";
    counter-increment: docx-num-29-6;
  }
  p.docx-num-29-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-29-6 {
    counter-reset: docx-num-29-7;
  }
  p.docx-num-29-7:before {
    content: ""counter(docx-num-29-7, decimal)".\9";
    counter-increment: docx-num-29-7;
  }
  p.docx-num-29-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-29-7 {
    counter-reset: docx-num-29-8;
  }
  p.docx-num-29-8:before {
    content: ""counter(docx-num-29-8, decimal)".\9";
    counter-increment: docx-num-29-8;
  }
  p.docx-num-29-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-33-0:before {
    content: ""counter(docx-num-33-0, decimal)".\9";
    counter-increment: docx-num-33-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-33-0 {
    counter-reset: docx-num-33-1;
  }
  p.docx-num-33-1:before {
    content: "o\9";
    counter-increment: docx-num-33-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-33-1 {
    counter-reset: docx-num-33-2;
  }
  p.docx-num-33-2:before {
    content: "\9";
    counter-increment: docx-num-33-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-33-2 {
    counter-reset: docx-num-33-3;
  }
  p.docx-num-33-3:before {
    content: "\9";
    counter-increment: docx-num-33-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-33-3 {
    counter-reset: docx-num-33-4;
  }
  p.docx-num-33-4:before {
    content: "\9";
    counter-increment: docx-num-33-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-33-4 {
    counter-reset: docx-num-33-5;
  }
  p.docx-num-33-5:before {
    content: "\9";
    counter-increment: docx-num-33-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-33-5 {
    counter-reset: docx-num-33-6;
  }
  p.docx-num-33-6:before {
    content: "\9";
    counter-increment: docx-num-33-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-33-6 {
    counter-reset: docx-num-33-7;
  }
  p.docx-num-33-7:before {
    content: "\9";
    counter-increment: docx-num-33-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-33-7 {
    counter-reset: docx-num-33-8;
  }
  p.docx-num-33-8:before {
    content: "\9";
    counter-increment: docx-num-33-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-33-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-26-0:before {
    content: "\9";
    counter-increment: docx-num-26-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-26-0 {
    counter-reset: docx-num-26-1;
  }
  p.docx-num-26-1:before {
    content: "o\9";
    counter-increment: docx-num-26-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-26-1 {
    counter-reset: docx-num-26-2;
  }
  p.docx-num-26-2:before {
    content: "\9";
    counter-increment: docx-num-26-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-26-2 {
    counter-reset: docx-num-26-3;
  }
  p.docx-num-26-3:before {
    content: "\9";
    counter-increment: docx-num-26-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-26-3 {
    counter-reset: docx-num-26-4;
  }
  p.docx-num-26-4:before {
    content: "\9";
    counter-increment: docx-num-26-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-26-4 {
    counter-reset: docx-num-26-5;
  }
  p.docx-num-26-5:before {
    content: "\9";
    counter-increment: docx-num-26-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-26-5 {
    counter-reset: docx-num-26-6;
  }
  p.docx-num-26-6:before {
    content: "\9";
    counter-increment: docx-num-26-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-26-6 {
    counter-reset: docx-num-26-7;
  }
  p.docx-num-26-7:before {
    content: "\9";
    counter-increment: docx-num-26-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-26-7 {
    counter-reset: docx-num-26-8;
  }
  p.docx-num-26-8:before {
    content: "\9";
    counter-increment: docx-num-26-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-26-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-35-0:before {
    content: ""counter(docx-num-35-0, decimal)".\9";
    counter-increment: docx-num-35-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-35-0 {
    counter-reset: docx-num-35-1;
  }
  p.docx-num-35-1:before {
    content: "o\9";
    counter-increment: docx-num-35-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-35-1 {
    counter-reset: docx-num-35-2;
  }
  p.docx-num-35-2:before {
    content: "\9";
    counter-increment: docx-num-35-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-35-2 {
    counter-reset: docx-num-35-3;
  }
  p.docx-num-35-3:before {
    content: "\9";
    counter-increment: docx-num-35-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-35-3 {
    counter-reset: docx-num-35-4;
  }
  p.docx-num-35-4:before {
    content: "\9";
    counter-increment: docx-num-35-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-35-4 {
    counter-reset: docx-num-35-5;
  }
  p.docx-num-35-5:before {
    content: "\9";
    counter-increment: docx-num-35-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-35-5 {
    counter-reset: docx-num-35-6;
  }
  p.docx-num-35-6:before {
    content: "\9";
    counter-increment: docx-num-35-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-35-6 {
    counter-reset: docx-num-35-7;
  }
  p.docx-num-35-7:before {
    content: "\9";
    counter-increment: docx-num-35-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-35-7 {
    counter-reset: docx-num-35-8;
  }
  p.docx-num-35-8:before {
    content: "\9";
    counter-increment: docx-num-35-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-35-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-10-0:before {
    content: "\9";
    counter-increment: docx-num-10-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-10-0 {
    counter-reset: docx-num-10-1;
  }
  p.docx-num-10-1:before {
    content: "o\9";
    counter-increment: docx-num-10-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-10-1 {
    counter-reset: docx-num-10-2;
  }
  p.docx-num-10-2:before {
    content: "\9";
    counter-increment: docx-num-10-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-10-2 {
    counter-reset: docx-num-10-3;
  }
  p.docx-num-10-3:before {
    content: "\9";
    counter-increment: docx-num-10-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-10-3 {
    counter-reset: docx-num-10-4;
  }
  p.docx-num-10-4:before {
    content: "\9";
    counter-increment: docx-num-10-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-10-4 {
    counter-reset: docx-num-10-5;
  }
  p.docx-num-10-5:before {
    content: "\9";
    counter-increment: docx-num-10-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-10-5 {
    counter-reset: docx-num-10-6;
  }
  p.docx-num-10-6:before {
    content: "\9";
    counter-increment: docx-num-10-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-10-6 {
    counter-reset: docx-num-10-7;
  }
  p.docx-num-10-7:before {
    content: "\9";
    counter-increment: docx-num-10-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-10-7 {
    counter-reset: docx-num-10-8;
  }
  p.docx-num-10-8:before {
    content: "\9";
    counter-increment: docx-num-10-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-10-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-23-0:before {
    content: ""counter(docx-num-23-0, decimal)".\9";
    counter-increment: docx-num-23-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-23-0 {
    counter-reset: docx-num-23-1;
  }
  p.docx-num-23-1:before {
    content: "o\9";
    counter-increment: docx-num-23-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-23-1 {
    counter-reset: docx-num-23-2;
  }
  p.docx-num-23-2:before {
    content: "\9";
    counter-increment: docx-num-23-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-23-2 {
    counter-reset: docx-num-23-3;
  }
  p.docx-num-23-3:before {
    content: "\9";
    counter-increment: docx-num-23-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-23-3 {
    counter-reset: docx-num-23-4;
  }
  p.docx-num-23-4:before {
    content: "\9";
    counter-increment: docx-num-23-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-23-4 {
    counter-reset: docx-num-23-5;
  }
  p.docx-num-23-5:before {
    content: "\9";
    counter-increment: docx-num-23-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-23-5 {
    counter-reset: docx-num-23-6;
  }
  p.docx-num-23-6:before {
    content: "\9";
    counter-increment: docx-num-23-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-23-6 {
    counter-reset: docx-num-23-7;
  }
  p.docx-num-23-7:before {
    content: "\9";
    counter-increment: docx-num-23-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-23-7 {
    counter-reset: docx-num-23-8;
  }
  p.docx-num-23-8:before {
    content: "\9";
    counter-increment: docx-num-23-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-23-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-24-0:before {
    content: ""counter(docx-num-24-0, decimal)".\9";
    counter-increment: docx-num-24-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-24-0 {
    counter-reset: docx-num-24-1;
  }
  p.docx-num-24-1:before {
    content: "o\9";
    counter-increment: docx-num-24-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-24-1 {
    counter-reset: docx-num-24-2;
  }
  p.docx-num-24-2:before {
    content: "\9";
    counter-increment: docx-num-24-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-24-2 {
    counter-reset: docx-num-24-3;
  }
  p.docx-num-24-3:before {
    content: "\9";
    counter-increment: docx-num-24-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-24-3 {
    counter-reset: docx-num-24-4;
  }
  p.docx-num-24-4:before {
    content: "\9";
    counter-increment: docx-num-24-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-24-4 {
    counter-reset: docx-num-24-5;
  }
  p.docx-num-24-5:before {
    content: "\9";
    counter-increment: docx-num-24-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-24-5 {
    counter-reset: docx-num-24-6;
  }
  p.docx-num-24-6:before {
    content: "\9";
    counter-increment: docx-num-24-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-24-6 {
    counter-reset: docx-num-24-7;
  }
  p.docx-num-24-7:before {
    content: "\9";
    counter-increment: docx-num-24-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-24-7 {
    counter-reset: docx-num-24-8;
  }
  p.docx-num-24-8:before {
    content: "\9";
    counter-increment: docx-num-24-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-24-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-45-0:before {
    content: ""counter(docx-num-45-0, decimal)".\9";
    counter-increment: docx-num-45-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-45-0 {
    counter-reset: docx-num-45-1;
  }
  p.docx-num-45-1:before {
    content: "o\9";
    counter-increment: docx-num-45-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-45-1 {
    counter-reset: docx-num-45-2;
  }
  p.docx-num-45-2:before {
    content: "\9";
    counter-increment: docx-num-45-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-45-2 {
    counter-reset: docx-num-45-3;
  }
  p.docx-num-45-3:before {
    content: "\9";
    counter-increment: docx-num-45-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-45-3 {
    counter-reset: docx-num-45-4;
  }
  p.docx-num-45-4:before {
    content: "\9";
    counter-increment: docx-num-45-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-45-4 {
    counter-reset: docx-num-45-5;
  }
  p.docx-num-45-5:before {
    content: "\9";
    counter-increment: docx-num-45-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-45-5 {
    counter-reset: docx-num-45-6;
  }
  p.docx-num-45-6:before {
    content: "\9";
    counter-increment: docx-num-45-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-45-6 {
    counter-reset: docx-num-45-7;
  }
  p.docx-num-45-7:before {
    content: "\9";
    counter-increment: docx-num-45-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-45-7 {
    counter-reset: docx-num-45-8;
  }
  p.docx-num-45-8:before {
    content: "\9";
    counter-increment: docx-num-45-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-45-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-22-0:before {
    content: "\9";
    counter-increment: docx-num-22-0;
    font-family: Symbol;
  }
  p.docx-num-22-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-22-0 {
    counter-reset: docx-num-22-1;
  }
  p.docx-num-22-1:before {
    content: ""counter(docx-num-22-1, decimal)".\9";
    counter-increment: docx-num-22-1;
  }
  p.docx-num-22-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-22-1 {
    counter-reset: docx-num-22-2;
  }
  p.docx-num-22-2:before {
    content: ""counter(docx-num-22-2, decimal)".\9";
    counter-increment: docx-num-22-2;
  }
  p.docx-num-22-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-22-2 {
    counter-reset: docx-num-22-3;
  }
  p.docx-num-22-3:before {
    content: ""counter(docx-num-22-3, decimal)".\9";
    counter-increment: docx-num-22-3;
  }
  p.docx-num-22-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-22-3 {
    counter-reset: docx-num-22-4;
  }
  p.docx-num-22-4:before {
    content: ""counter(docx-num-22-4, decimal)".\9";
    counter-increment: docx-num-22-4;
  }
  p.docx-num-22-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-22-4 {
    counter-reset: docx-num-22-5;
  }
  p.docx-num-22-5:before {
    content: ""counter(docx-num-22-5, decimal)".\9";
    counter-increment: docx-num-22-5;
  }
  p.docx-num-22-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-22-5 {
    counter-reset: docx-num-22-6;
  }
  p.docx-num-22-6:before {
    content: ""counter(docx-num-22-6, decimal)".\9";
    counter-increment: docx-num-22-6;
  }
  p.docx-num-22-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-22-6 {
    counter-reset: docx-num-22-7;
  }
  p.docx-num-22-7:before {
    content: ""counter(docx-num-22-7, decimal)".\9";
    counter-increment: docx-num-22-7;
  }
  p.docx-num-22-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-22-7 {
    counter-reset: docx-num-22-8;
  }
  p.docx-num-22-8:before {
    content: ""counter(docx-num-22-8, decimal)".\9";
    counter-increment: docx-num-22-8;
  }
  p.docx-num-22-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-40-0:before {
    content: ""counter(docx-num-40-0, decimal)".\9";
    counter-increment: docx-num-40-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-40-0 {
    counter-reset: docx-num-40-1;
  }
  p.docx-num-40-1:before {
    content: "o\9";
    counter-increment: docx-num-40-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-40-1 {
    counter-reset: docx-num-40-2;
  }
  p.docx-num-40-2:before {
    content: "\9";
    counter-increment: docx-num-40-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-40-2 {
    counter-reset: docx-num-40-3;
  }
  p.docx-num-40-3:before {
    content: "\9";
    counter-increment: docx-num-40-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-40-3 {
    counter-reset: docx-num-40-4;
  }
  p.docx-num-40-4:before {
    content: "\9";
    counter-increment: docx-num-40-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-40-4 {
    counter-reset: docx-num-40-5;
  }
  p.docx-num-40-5:before {
    content: "\9";
    counter-increment: docx-num-40-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-40-5 {
    counter-reset: docx-num-40-6;
  }
  p.docx-num-40-6:before {
    content: "\9";
    counter-increment: docx-num-40-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-40-6 {
    counter-reset: docx-num-40-7;
  }
  p.docx-num-40-7:before {
    content: "\9";
    counter-increment: docx-num-40-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-40-7 {
    counter-reset: docx-num-40-8;
  }
  p.docx-num-40-8:before {
    content: "\9";
    counter-increment: docx-num-40-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-40-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-30-0:before {
    content: ""counter(docx-num-30-0, decimal)".\9";
    counter-increment: docx-num-30-0;
  }
  p.docx-num-30-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-30-0 {
    counter-reset: docx-num-30-1;
  }
  p.docx-num-30-1:before {
    content: ""counter(docx-num-30-1, decimal)".\9";
    counter-increment: docx-num-30-1;
  }
  p.docx-num-30-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-30-1 {
    counter-reset: docx-num-30-2;
  }
  p.docx-num-30-2:before {
    content: ""counter(docx-num-30-2, decimal)".\9";
    counter-increment: docx-num-30-2;
  }
  p.docx-num-30-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-30-2 {
    counter-reset: docx-num-30-3;
  }
  p.docx-num-30-3:before {
    content: ""counter(docx-num-30-3, decimal)".\9";
    counter-increment: docx-num-30-3;
  }
  p.docx-num-30-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-30-3 {
    counter-reset: docx-num-30-4;
  }
  p.docx-num-30-4:before {
    content: ""counter(docx-num-30-4, decimal)".\9";
    counter-increment: docx-num-30-4;
  }
  p.docx-num-30-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-30-4 {
    counter-reset: docx-num-30-5;
  }
  p.docx-num-30-5:before {
    content: ""counter(docx-num-30-5, decimal)".\9";
    counter-increment: docx-num-30-5;
  }
  p.docx-num-30-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-30-5 {
    counter-reset: docx-num-30-6;
  }
  p.docx-num-30-6:before {
    content: ""counter(docx-num-30-6, decimal)".\9";
    counter-increment: docx-num-30-6;
  }
  p.docx-num-30-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-30-6 {
    counter-reset: docx-num-30-7;
  }
  p.docx-num-30-7:before {
    content: ""counter(docx-num-30-7, decimal)".\9";
    counter-increment: docx-num-30-7;
  }
  p.docx-num-30-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-30-7 {
    counter-reset: docx-num-30-8;
  }
  p.docx-num-30-8:before {
    content: ""counter(docx-num-30-8, decimal)".\9";
    counter-increment: docx-num-30-8;
  }
  p.docx-num-30-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-19-0:before {
    content: ""counter(docx-num-19-0, decimal)".\9";
    counter-increment: docx-num-19-0;
    font-family: Times New Roman;
    font-weight: bold;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx-num-19-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 18.00pt;
  }
  p.docx-num-19-0 {
    counter-reset: docx-num-19-1;
  }
  p.docx-num-19-1:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)".\9";
    counter-increment: docx-num-19-1;
    font-family: Times New Roman;
    font-weight: bold;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx-num-19-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -21.60pt;
    margin-left: 39.60pt;
  }
  p.docx-num-19-1 {
    counter-reset: docx-num-19-2;
  }
  p.docx-num-19-2:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)".\9";
    counter-increment: docx-num-19-2;
    font-family: Times New Roman;
    font-weight: bold;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx-num-19-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -25.20pt;
    margin-left: 61.20pt;
  }
  p.docx-num-19-2 {
    counter-reset: docx-num-19-3;
  }
  p.docx-num-19-3:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)"."counter(docx-num-19-3, decimal)".\9";
    counter-increment: docx-num-19-3;
  }
  p.docx-num-19-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -32.40pt;
    margin-left: 86.40pt;
  }
  p.docx-num-19-3 {
    counter-reset: docx-num-19-4;
  }
  p.docx-num-19-4:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)"."counter(docx-num-19-3, decimal)"."counter(docx-num-19-4, decimal)".\9";
    counter-increment: docx-num-19-4;
  }
  p.docx-num-19-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -39.60pt;
    margin-left: 111.60pt;
  }
  p.docx-num-19-4 {
    counter-reset: docx-num-19-5;
  }
  p.docx-num-19-5:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)"."counter(docx-num-19-3, decimal)"."counter(docx-num-19-4, decimal)"."counter(docx-num-19-5, decimal)".\9";
    counter-increment: docx-num-19-5;
  }
  p.docx-num-19-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -46.80pt;
    margin-left: 136.80pt;
  }
  p.docx-num-19-5 {
    counter-reset: docx-num-19-6;
  }
  p.docx-num-19-6:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)"."counter(docx-num-19-3, decimal)"."counter(docx-num-19-4, decimal)"."counter(docx-num-19-5, decimal)"."counter(docx-num-19-6, decimal)".\9";
    counter-increment: docx-num-19-6;
  }
  p.docx-num-19-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-19-6 {
    counter-reset: docx-num-19-7;
  }
  p.docx-num-19-7:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)"."counter(docx-num-19-3, decimal)"."counter(docx-num-19-4, decimal)"."counter(docx-num-19-5, decimal)"."counter(docx-num-19-6, decimal)"."counter(docx-num-19-7, decimal)".\9";
    counter-increment: docx-num-19-7;
  }
  p.docx-num-19-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -61.20pt;
    margin-left: 187.20pt;
  }
  p.docx-num-19-7 {
    counter-reset: docx-num-19-8;
  }
  p.docx-num-19-8:before {
    content: ""counter(docx-num-19-0, decimal)"."counter(docx-num-19-1, decimal)"."counter(docx-num-19-2, decimal)"."counter(docx-num-19-3, decimal)"."counter(docx-num-19-4, decimal)"."counter(docx-num-19-5, decimal)"."counter(docx-num-19-6, decimal)"."counter(docx-num-19-7, decimal)"."counter(docx-num-19-8, decimal)".\9";
    counter-increment: docx-num-19-8;
  }
  p.docx-num-19-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-38-0:before {
    content: ""counter(docx-num-38-0, decimal)".\9";
    counter-increment: docx-num-38-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-38-0 {
    counter-reset: docx-num-38-1;
  }
  p.docx-num-38-1:before {
    content: "o\9";
    counter-increment: docx-num-38-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-38-1 {
    counter-reset: docx-num-38-2;
  }
  p.docx-num-38-2:before {
    content: "\9";
    counter-increment: docx-num-38-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-38-2 {
    counter-reset: docx-num-38-3;
  }
  p.docx-num-38-3:before {
    content: "\9";
    counter-increment: docx-num-38-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-38-3 {
    counter-reset: docx-num-38-4;
  }
  p.docx-num-38-4:before {
    content: "\9";
    counter-increment: docx-num-38-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-38-4 {
    counter-reset: docx-num-38-5;
  }
  p.docx-num-38-5:before {
    content: "\9";
    counter-increment: docx-num-38-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-38-5 {
    counter-reset: docx-num-38-6;
  }
  p.docx-num-38-6:before {
    content: "\9";
    counter-increment: docx-num-38-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-38-6 {
    counter-reset: docx-num-38-7;
  }
  p.docx-num-38-7:before {
    content: "\9";
    counter-increment: docx-num-38-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-38-7 {
    counter-reset: docx-num-38-8;
  }
  p.docx-num-38-8:before {
    content: "\9";
    counter-increment: docx-num-38-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-38-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-6-0:before {
    content: "\9";
    counter-increment: docx-num-6-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-6-0 {
    counter-reset: docx-num-6-1;
  }
  p.docx-num-6-1:before {
    content: "o\9";
    counter-increment: docx-num-6-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-6-1 {
    counter-reset: docx-num-6-2;
  }
  p.docx-num-6-2:before {
    content: "\9";
    counter-increment: docx-num-6-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-6-2 {
    counter-reset: docx-num-6-3;
  }
  p.docx-num-6-3:before {
    content: "\9";
    counter-increment: docx-num-6-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-6-3 {
    counter-reset: docx-num-6-4;
  }
  p.docx-num-6-4:before {
    content: "\9";
    counter-increment: docx-num-6-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-6-4 {
    counter-reset: docx-num-6-5;
  }
  p.docx-num-6-5:before {
    content: "\9";
    counter-increment: docx-num-6-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-6-5 {
    counter-reset: docx-num-6-6;
  }
  p.docx-num-6-6:before {
    content: "\9";
    counter-increment: docx-num-6-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-6-6 {
    counter-reset: docx-num-6-7;
  }
  p.docx-num-6-7:before {
    content: "\9";
    counter-increment: docx-num-6-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-6-7 {
    counter-reset: docx-num-6-8;
  }
  p.docx-num-6-8:before {
    content: "\9";
    counter-increment: docx-num-6-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-6-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-32-0:before {
    content: ""counter(docx-num-32-0, decimal)".\9";
    counter-increment: docx-num-32-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-32-0 {
    counter-reset: docx-num-32-1;
  }
  p.docx-num-32-1:before {
    content: "o\9";
    counter-increment: docx-num-32-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-32-1 {
    counter-reset: docx-num-32-2;
  }
  p.docx-num-32-2:before {
    content: "\9";
    counter-increment: docx-num-32-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-32-2 {
    counter-reset: docx-num-32-3;
  }
  p.docx-num-32-3:before {
    content: "\9";
    counter-increment: docx-num-32-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-32-3 {
    counter-reset: docx-num-32-4;
  }
  p.docx-num-32-4:before {
    content: "\9";
    counter-increment: docx-num-32-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-32-4 {
    counter-reset: docx-num-32-5;
  }
  p.docx-num-32-5:before {
    content: "\9";
    counter-increment: docx-num-32-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-32-5 {
    counter-reset: docx-num-32-6;
  }
  p.docx-num-32-6:before {
    content: "\9";
    counter-increment: docx-num-32-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-32-6 {
    counter-reset: docx-num-32-7;
  }
  p.docx-num-32-7:before {
    content: "\9";
    counter-increment: docx-num-32-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-32-7 {
    counter-reset: docx-num-32-8;
  }
  p.docx-num-32-8:before {
    content: "\9";
    counter-increment: docx-num-32-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-32-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-9-0:before {
    content: "\9";
    counter-increment: docx-num-9-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-9-0 {
    counter-reset: docx-num-9-1;
  }
  p.docx-num-9-1:before {
    content: "o\9";
    counter-increment: docx-num-9-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-9-1 {
    counter-reset: docx-num-9-2;
  }
  p.docx-num-9-2:before {
    content: "\9";
    counter-increment: docx-num-9-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-9-2 {
    counter-reset: docx-num-9-3;
  }
  p.docx-num-9-3:before {
    content: "\9";
    counter-increment: docx-num-9-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-9-3 {
    counter-reset: docx-num-9-4;
  }
  p.docx-num-9-4:before {
    content: "\9";
    counter-increment: docx-num-9-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-9-4 {
    counter-reset: docx-num-9-5;
  }
  p.docx-num-9-5:before {
    content: "\9";
    counter-increment: docx-num-9-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-9-5 {
    counter-reset: docx-num-9-6;
  }
  p.docx-num-9-6:before {
    content: "\9";
    counter-increment: docx-num-9-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-9-6 {
    counter-reset: docx-num-9-7;
  }
  p.docx-num-9-7:before {
    content: "\9";
    counter-increment: docx-num-9-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-9-7 {
    counter-reset: docx-num-9-8;
  }
  p.docx-num-9-8:before {
    content: "\9";
    counter-increment: docx-num-9-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-9-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-1-0:before {
    content: "\9";
    counter-increment: docx-num-1-0;
    font-family: Symbol;
  }
  p.docx-num-1-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-1-0 {
    counter-reset: docx-num-1-1;
  }
  p.docx-num-1-1:before {
    content: "o\9";
    counter-increment: docx-num-1-1;
    font-family: Courier New;
  }
  p.docx-num-1-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-1-1 {
    counter-reset: docx-num-1-2;
  }
  p.docx-num-1-2:before {
    content: "\9";
    counter-increment: docx-num-1-2;
    font-family: Wingdings;
  }
  p.docx-num-1-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-1-2 {
    counter-reset: docx-num-1-3;
  }
  p.docx-num-1-3:before {
    content: "\9";
    counter-increment: docx-num-1-3;
    font-family: Symbol;
  }
  p.docx-num-1-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-1-3 {
    counter-reset: docx-num-1-4;
  }
  p.docx-num-1-4:before {
    content: "o\9";
    counter-increment: docx-num-1-4;
    font-family: Courier New;
  }
  p.docx-num-1-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-1-4 {
    counter-reset: docx-num-1-5;
  }
  p.docx-num-1-5:before {
    content: "\9";
    counter-increment: docx-num-1-5;
    font-family: Wingdings;
  }
  p.docx-num-1-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-1-5 {
    counter-reset: docx-num-1-6;
  }
  p.docx-num-1-6:before {
    content: "\9";
    counter-increment: docx-num-1-6;
    font-family: Symbol;
  }
  p.docx-num-1-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-1-6 {
    counter-reset: docx-num-1-7;
  }
  p.docx-num-1-7:before {
    content: "o\9";
    counter-increment: docx-num-1-7;
    font-family: Courier New;
  }
  p.docx-num-1-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-1-7 {
    counter-reset: docx-num-1-8;
  }
  p.docx-num-1-8:before {
    content: "\9";
    counter-increment: docx-num-1-8;
    font-family: Wingdings;
  }
  p.docx-num-1-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-44-0:before {
    content: ""counter(docx-num-44-0, decimal)".\9";
    counter-increment: docx-num-44-0;
  }
  p.docx-num-44-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-44-0 {
    counter-reset: docx-num-44-1;
  }
  p.docx-num-44-1:before {
    content: ""counter(docx-num-44-1, lower-alpha)".\9";
    counter-increment: docx-num-44-1;
  }
  p.docx-num-44-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-44-1 {
    counter-reset: docx-num-44-2;
  }
  p.docx-num-44-2:before {
    content: ""counter(docx-num-44-2, lower-roman)".\9";
    counter-increment: docx-num-44-2;
  }
  p.docx-num-44-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-44-2 {
    counter-reset: docx-num-44-3;
  }
  p.docx-num-44-3:before {
    content: ""counter(docx-num-44-3, decimal)".\9";
    counter-increment: docx-num-44-3;
  }
  p.docx-num-44-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-44-3 {
    counter-reset: docx-num-44-4;
  }
  p.docx-num-44-4:before {
    content: ""counter(docx-num-44-4, lower-alpha)".\9";
    counter-increment: docx-num-44-4;
  }
  p.docx-num-44-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-44-4 {
    counter-reset: docx-num-44-5;
  }
  p.docx-num-44-5:before {
    content: ""counter(docx-num-44-5, lower-roman)".\9";
    counter-increment: docx-num-44-5;
  }
  p.docx-num-44-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-44-5 {
    counter-reset: docx-num-44-6;
  }
  p.docx-num-44-6:before {
    content: ""counter(docx-num-44-6, decimal)".\9";
    counter-increment: docx-num-44-6;
  }
  p.docx-num-44-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-44-6 {
    counter-reset: docx-num-44-7;
  }
  p.docx-num-44-7:before {
    content: ""counter(docx-num-44-7, lower-alpha)".\9";
    counter-increment: docx-num-44-7;
  }
  p.docx-num-44-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-44-7 {
    counter-reset: docx-num-44-8;
  }
  p.docx-num-44-8:before {
    content: ""counter(docx-num-44-8, lower-roman)".\9";
    counter-increment: docx-num-44-8;
  }
  p.docx-num-44-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-37-0:before {
    content: ""counter(docx-num-37-0, decimal)".\9";
    counter-increment: docx-num-37-0;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-37-0 {
    counter-reset: docx-num-37-1;
  }
  p.docx-num-37-1:before {
    content: "o\9";
    counter-increment: docx-num-37-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-37-1 {
    counter-reset: docx-num-37-2;
  }
  p.docx-num-37-2:before {
    content: "\9";
    counter-increment: docx-num-37-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-37-2 {
    counter-reset: docx-num-37-3;
  }
  p.docx-num-37-3:before {
    content: "\9";
    counter-increment: docx-num-37-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-37-3 {
    counter-reset: docx-num-37-4;
  }
  p.docx-num-37-4:before {
    content: "\9";
    counter-increment: docx-num-37-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-37-4 {
    counter-reset: docx-num-37-5;
  }
  p.docx-num-37-5:before {
    content: "\9";
    counter-increment: docx-num-37-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-37-5 {
    counter-reset: docx-num-37-6;
  }
  p.docx-num-37-6:before {
    content: "\9";
    counter-increment: docx-num-37-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-37-6 {
    counter-reset: docx-num-37-7;
  }
  p.docx-num-37-7:before {
    content: "\9";
    counter-increment: docx-num-37-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-37-7 {
    counter-reset: docx-num-37-8;
  }
  p.docx-num-37-8:before {
    content: "\9";
    counter-increment: docx-num-37-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-37-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-43-0:before {
    content: ""counter(docx-num-43-0, decimal)".\9";
    counter-increment: docx-num-43-0;
  }
  p.docx-num-43-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-43-0 {
    counter-reset: docx-num-43-1;
  }
  p.docx-num-43-1:before {
    content: ""counter(docx-num-43-1, decimal)".\9";
    counter-increment: docx-num-43-1;
  }
  p.docx-num-43-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-43-1 {
    counter-reset: docx-num-43-2;
  }
  p.docx-num-43-2:before {
    content: ""counter(docx-num-43-2, decimal)".\9";
    counter-increment: docx-num-43-2;
  }
  p.docx-num-43-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-43-2 {
    counter-reset: docx-num-43-3;
  }
  p.docx-num-43-3:before {
    content: ""counter(docx-num-43-3, decimal)".\9";
    counter-increment: docx-num-43-3;
  }
  p.docx-num-43-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-43-3 {
    counter-reset: docx-num-43-4;
  }
  p.docx-num-43-4:before {
    content: ""counter(docx-num-43-4, decimal)".\9";
    counter-increment: docx-num-43-4;
  }
  p.docx-num-43-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-43-4 {
    counter-reset: docx-num-43-5;
  }
  p.docx-num-43-5:before {
    content: ""counter(docx-num-43-5, decimal)".\9";
    counter-increment: docx-num-43-5;
  }
  p.docx-num-43-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-43-5 {
    counter-reset: docx-num-43-6;
  }
  p.docx-num-43-6:before {
    content: ""counter(docx-num-43-6, decimal)".\9";
    counter-increment: docx-num-43-6;
  }
  p.docx-num-43-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-43-6 {
    counter-reset: docx-num-43-7;
  }
  p.docx-num-43-7:before {
    content: ""counter(docx-num-43-7, decimal)".\9";
    counter-increment: docx-num-43-7;
  }
  p.docx-num-43-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-43-7 {
    counter-reset: docx-num-43-8;
  }
  p.docx-num-43-8:before {
    content: ""counter(docx-num-43-8, decimal)".\9";
    counter-increment: docx-num-43-8;
  }
  p.docx-num-43-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-34-0:before {
    content: "\9";
    counter-increment: docx-num-34-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-34-0 {
    counter-reset: docx-num-34-1;
  }
  p.docx-num-34-1:before {
    content: "o\9";
    counter-increment: docx-num-34-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-34-1 {
    counter-reset: docx-num-34-2;
  }
  p.docx-num-34-2:before {
    content: "\9";
    counter-increment: docx-num-34-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-34-2 {
    counter-reset: docx-num-34-3;
  }
  p.docx-num-34-3:before {
    content: "\9";
    counter-increment: docx-num-34-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-34-3 {
    counter-reset: docx-num-34-4;
  }
  p.docx-num-34-4:before {
    content: "\9";
    counter-increment: docx-num-34-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-34-4 {
    counter-reset: docx-num-34-5;
  }
  p.docx-num-34-5:before {
    content: "\9";
    counter-increment: docx-num-34-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-34-5 {
    counter-reset: docx-num-34-6;
  }
  p.docx-num-34-6:before {
    content: "\9";
    counter-increment: docx-num-34-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-34-6 {
    counter-reset: docx-num-34-7;
  }
  p.docx-num-34-7:before {
    content: "\9";
    counter-increment: docx-num-34-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-34-7 {
    counter-reset: docx-num-34-8;
  }
  p.docx-num-34-8:before {
    content: "\9";
    counter-increment: docx-num-34-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-34-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-17-0:before {
    content: ""counter(docx-num-17-0, decimal)".\9";
    counter-increment: docx-num-17-0;
  }
  p.docx-num-17-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 18.00pt;
  }
  p.docx-num-17-0 {
    counter-reset: docx-num-17-1;
  }
  p.docx-num-17-1:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)".\9";
    counter-increment: docx-num-17-1;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  p.docx-num-17-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -21.60pt;
    margin-left: 39.60pt;
  }
  p.docx-num-17-1 {
    counter-reset: docx-num-17-2;
  }
  p.docx-num-17-2:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)".\9";
    counter-increment: docx-num-17-2;
  }
  p.docx-num-17-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -25.20pt;
    margin-left: 61.20pt;
  }
  p.docx-num-17-2 {
    counter-reset: docx-num-17-3;
  }
  p.docx-num-17-3:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)"."counter(docx-num-17-3, decimal)".\9";
    counter-increment: docx-num-17-3;
  }
  p.docx-num-17-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -32.40pt;
    margin-left: 86.40pt;
  }
  p.docx-num-17-3 {
    counter-reset: docx-num-17-4;
  }
  p.docx-num-17-4:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)"."counter(docx-num-17-3, decimal)"."counter(docx-num-17-4, decimal)".\9";
    counter-increment: docx-num-17-4;
  }
  p.docx-num-17-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -39.60pt;
    margin-left: 111.60pt;
  }
  p.docx-num-17-4 {
    counter-reset: docx-num-17-5;
  }
  p.docx-num-17-5:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)"."counter(docx-num-17-3, decimal)"."counter(docx-num-17-4, decimal)"."counter(docx-num-17-5, decimal)".\9";
    counter-increment: docx-num-17-5;
  }
  p.docx-num-17-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -46.80pt;
    margin-left: 136.80pt;
  }
  p.docx-num-17-5 {
    counter-reset: docx-num-17-6;
  }
  p.docx-num-17-6:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)"."counter(docx-num-17-3, decimal)"."counter(docx-num-17-4, decimal)"."counter(docx-num-17-5, decimal)"."counter(docx-num-17-6, decimal)".\9";
    counter-increment: docx-num-17-6;
  }
  p.docx-num-17-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-17-6 {
    counter-reset: docx-num-17-7;
  }
  p.docx-num-17-7:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)"."counter(docx-num-17-3, decimal)"."counter(docx-num-17-4, decimal)"."counter(docx-num-17-5, decimal)"."counter(docx-num-17-6, decimal)"."counter(docx-num-17-7, decimal)".\9";
    counter-increment: docx-num-17-7;
  }
  p.docx-num-17-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -61.20pt;
    margin-left: 187.20pt;
  }
  p.docx-num-17-7 {
    counter-reset: docx-num-17-8;
  }
  p.docx-num-17-8:before {
    content: ""counter(docx-num-17-0, decimal)"."counter(docx-num-17-1, decimal)"."counter(docx-num-17-2, decimal)"."counter(docx-num-17-3, decimal)"."counter(docx-num-17-4, decimal)"."counter(docx-num-17-5, decimal)"."counter(docx-num-17-6, decimal)"."counter(docx-num-17-7, decimal)"."counter(docx-num-17-8, decimal)".\9";
    counter-increment: docx-num-17-8;
  }
  p.docx-num-17-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-3-0:before {
    content: ""counter(docx-num-3-0, decimal)".\9";
    counter-increment: docx-num-3-0;
    font-weight: bold;
    min-height: 14.00pt;
    font-size: 14.00pt;
    text-decoration: none;
  }
  p.docx-num-3-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 18.00pt;
  }
  p.docx-num-3-0 {
    counter-reset: docx-num-3-1;
  }
  p.docx-num-3-1:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)".\9";
    counter-increment: docx-num-3-1;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx-num-3-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -21.60pt;
    margin-left: 39.60pt;
  }
  p.docx-num-3-1 {
    counter-reset: docx-num-3-2;
  }
  p.docx-num-3-2:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)".\9";
    counter-increment: docx-num-3-2;
  }
  p.docx-num-3-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -25.20pt;
    margin-left: 61.20pt;
  }
  p.docx-num-3-2 {
    counter-reset: docx-num-3-3;
  }
  p.docx-num-3-3:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)"."counter(docx-num-3-3, decimal)".\9";
    counter-increment: docx-num-3-3;
  }
  p.docx-num-3-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -32.40pt;
    margin-left: 86.40pt;
  }
  p.docx-num-3-3 {
    counter-reset: docx-num-3-4;
  }
  p.docx-num-3-4:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)"."counter(docx-num-3-3, decimal)"."counter(docx-num-3-4, decimal)".\9";
    counter-increment: docx-num-3-4;
  }
  p.docx-num-3-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -39.60pt;
    margin-left: 111.60pt;
  }
  p.docx-num-3-4 {
    counter-reset: docx-num-3-5;
  }
  p.docx-num-3-5:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)"."counter(docx-num-3-3, decimal)"."counter(docx-num-3-4, decimal)"."counter(docx-num-3-5, decimal)".\9";
    counter-increment: docx-num-3-5;
  }
  p.docx-num-3-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -46.80pt;
    margin-left: 136.80pt;
  }
  p.docx-num-3-5 {
    counter-reset: docx-num-3-6;
  }
  p.docx-num-3-6:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)"."counter(docx-num-3-3, decimal)"."counter(docx-num-3-4, decimal)"."counter(docx-num-3-5, decimal)"."counter(docx-num-3-6, decimal)".\9";
    counter-increment: docx-num-3-6;
  }
  p.docx-num-3-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-3-6 {
    counter-reset: docx-num-3-7;
  }
  p.docx-num-3-7:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)"."counter(docx-num-3-3, decimal)"."counter(docx-num-3-4, decimal)"."counter(docx-num-3-5, decimal)"."counter(docx-num-3-6, decimal)"."counter(docx-num-3-7, decimal)".\9";
    counter-increment: docx-num-3-7;
  }
  p.docx-num-3-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -61.20pt;
    margin-left: 187.20pt;
  }
  p.docx-num-3-7 {
    counter-reset: docx-num-3-8;
  }
  p.docx-num-3-8:before {
    content: ""counter(docx-num-3-0, decimal)"."counter(docx-num-3-1, decimal)"."counter(docx-num-3-2, decimal)"."counter(docx-num-3-3, decimal)"."counter(docx-num-3-4, decimal)"."counter(docx-num-3-5, decimal)"."counter(docx-num-3-6, decimal)"."counter(docx-num-3-7, decimal)"."counter(docx-num-3-8, decimal)".\9";
    counter-increment: docx-num-3-8;
  }
  p.docx-num-3-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-42-0:before {
    content: ""counter(docx-num-42-0, decimal)".\9";
    counter-increment: docx-num-42-0;
    font-weight: normal;
  }
  p.docx-num-42-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-42-0 {
    counter-reset: docx-num-42-1;
  }
  p.docx-num-42-1:before {
    content: ""counter(docx-num-42-1, lower-alpha)".\9";
    counter-increment: docx-num-42-1;
  }
  p.docx-num-42-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-42-1 {
    counter-reset: docx-num-42-2;
  }
  p.docx-num-42-2:before {
    content: ""counter(docx-num-42-2, lower-roman)".\9";
    counter-increment: docx-num-42-2;
  }
  p.docx-num-42-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-42-2 {
    counter-reset: docx-num-42-3;
  }
  p.docx-num-42-3:before {
    content: ""counter(docx-num-42-3, decimal)".\9";
    counter-increment: docx-num-42-3;
  }
  p.docx-num-42-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-42-3 {
    counter-reset: docx-num-42-4;
  }
  p.docx-num-42-4:before {
    content: ""counter(docx-num-42-4, lower-alpha)".\9";
    counter-increment: docx-num-42-4;
  }
  p.docx-num-42-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-42-4 {
    counter-reset: docx-num-42-5;
  }
  p.docx-num-42-5:before {
    content: ""counter(docx-num-42-5, lower-roman)".\9";
    counter-increment: docx-num-42-5;
  }
  p.docx-num-42-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-42-5 {
    counter-reset: docx-num-42-6;
  }
  p.docx-num-42-6:before {
    content: ""counter(docx-num-42-6, decimal)".\9";
    counter-increment: docx-num-42-6;
  }
  p.docx-num-42-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-42-6 {
    counter-reset: docx-num-42-7;
  }
  p.docx-num-42-7:before {
    content: ""counter(docx-num-42-7, lower-alpha)".\9";
    counter-increment: docx-num-42-7;
  }
  p.docx-num-42-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-42-7 {
    counter-reset: docx-num-42-8;
  }
  p.docx-num-42-8:before {
    content: ""counter(docx-num-42-8, lower-roman)".\9";
    counter-increment: docx-num-42-8;
  }
  p.docx-num-42-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -9.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-8-0:before {
    content: "\9";
    counter-increment: docx-num-8-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-8-0 {
    counter-reset: docx-num-8-1;
  }
  p.docx-num-8-1:before {
    content: "o\9";
    counter-increment: docx-num-8-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-8-1 {
    counter-reset: docx-num-8-2;
  }
  p.docx-num-8-2:before {
    content: "\9";
    counter-increment: docx-num-8-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-8-2 {
    counter-reset: docx-num-8-3;
  }
  p.docx-num-8-3:before {
    content: "\9";
    counter-increment: docx-num-8-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-8-3 {
    counter-reset: docx-num-8-4;
  }
  p.docx-num-8-4:before {
    content: "\9";
    counter-increment: docx-num-8-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-8-4 {
    counter-reset: docx-num-8-5;
  }
  p.docx-num-8-5:before {
    content: "\9";
    counter-increment: docx-num-8-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-8-5 {
    counter-reset: docx-num-8-6;
  }
  p.docx-num-8-6:before {
    content: "\9";
    counter-increment: docx-num-8-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-8-6 {
    counter-reset: docx-num-8-7;
  }
  p.docx-num-8-7:before {
    content: "\9";
    counter-increment: docx-num-8-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-8-7 {
    counter-reset: docx-num-8-8;
  }
  p.docx-num-8-8:before {
    content: "\9";
    counter-increment: docx-num-8-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-8-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-27-0:before {
    content: ""counter(docx-num-27-0, decimal)".\9";
    counter-increment: docx-num-27-0;
  }
  p.docx-num-27-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-27-0 {
    counter-reset: docx-num-27-1;
  }
  p.docx-num-27-1:before {
    content: ""counter(docx-num-27-1, decimal)".\9";
    counter-increment: docx-num-27-1;
  }
  p.docx-num-27-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-27-1 {
    counter-reset: docx-num-27-2;
  }
  p.docx-num-27-2:before {
    content: ""counter(docx-num-27-2, decimal)".\9";
    counter-increment: docx-num-27-2;
  }
  p.docx-num-27-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-27-2 {
    counter-reset: docx-num-27-3;
  }
  p.docx-num-27-3:before {
    content: ""counter(docx-num-27-3, decimal)".\9";
    counter-increment: docx-num-27-3;
  }
  p.docx-num-27-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-27-3 {
    counter-reset: docx-num-27-4;
  }
  p.docx-num-27-4:before {
    content: ""counter(docx-num-27-4, decimal)".\9";
    counter-increment: docx-num-27-4;
  }
  p.docx-num-27-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-27-4 {
    counter-reset: docx-num-27-5;
  }
  p.docx-num-27-5:before {
    content: ""counter(docx-num-27-5, decimal)".\9";
    counter-increment: docx-num-27-5;
  }
  p.docx-num-27-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-27-5 {
    counter-reset: docx-num-27-6;
  }
  p.docx-num-27-6:before {
    content: ""counter(docx-num-27-6, decimal)".\9";
    counter-increment: docx-num-27-6;
  }
  p.docx-num-27-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-27-6 {
    counter-reset: docx-num-27-7;
  }
  p.docx-num-27-7:before {
    content: ""counter(docx-num-27-7, decimal)".\9";
    counter-increment: docx-num-27-7;
  }
  p.docx-num-27-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-27-7 {
    counter-reset: docx-num-27-8;
  }
  p.docx-num-27-8:before {
    content: ""counter(docx-num-27-8, decimal)".\9";
    counter-increment: docx-num-27-8;
  }
  p.docx-num-27-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  p.docx-num-15-0:before {
    content: ""counter(docx-num-15-0, decimal)".\9";
    counter-increment: docx-num-15-0;
    min-height: 14.00pt;
    font-size: 14.00pt;
  }
  p.docx-num-15-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 18.00pt;
  }
  p.docx-num-15-0 {
    counter-reset: docx-num-15-1;
  }
  p.docx-num-15-1:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)".\9";
    counter-increment: docx-num-15-1;
    min-height: 12.00pt;
    font-size: 12.00pt;
  }
  p.docx-num-15-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -21.60pt;
    margin-left: 39.60pt;
  }
  p.docx-num-15-1 {
    counter-reset: docx-num-15-2;
  }
  p.docx-num-15-2:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)".\9";
    counter-increment: docx-num-15-2;
  }
  p.docx-num-15-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -25.20pt;
    margin-left: 61.20pt;
  }
  p.docx-num-15-2 {
    counter-reset: docx-num-15-3;
  }
  p.docx-num-15-3:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)"."counter(docx-num-15-3, decimal)".\9";
    counter-increment: docx-num-15-3;
  }
  p.docx-num-15-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -32.40pt;
    margin-left: 86.40pt;
  }
  p.docx-num-15-3 {
    counter-reset: docx-num-15-4;
  }
  p.docx-num-15-4:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)"."counter(docx-num-15-3, decimal)"."counter(docx-num-15-4, decimal)".\9";
    counter-increment: docx-num-15-4;
  }
  p.docx-num-15-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -39.60pt;
    margin-left: 111.60pt;
  }
  p.docx-num-15-4 {
    counter-reset: docx-num-15-5;
  }
  p.docx-num-15-5:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)"."counter(docx-num-15-3, decimal)"."counter(docx-num-15-4, decimal)"."counter(docx-num-15-5, decimal)".\9";
    counter-increment: docx-num-15-5;
  }
  p.docx-num-15-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -46.80pt;
    margin-left: 136.80pt;
  }
  p.docx-num-15-5 {
    counter-reset: docx-num-15-6;
  }
  p.docx-num-15-6:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)"."counter(docx-num-15-3, decimal)"."counter(docx-num-15-4, decimal)"."counter(docx-num-15-5, decimal)"."counter(docx-num-15-6, decimal)".\9";
    counter-increment: docx-num-15-6;
  }
  p.docx-num-15-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -54.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-15-6 {
    counter-reset: docx-num-15-7;
  }
  p.docx-num-15-7:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)"."counter(docx-num-15-3, decimal)"."counter(docx-num-15-4, decimal)"."counter(docx-num-15-5, decimal)"."counter(docx-num-15-6, decimal)"."counter(docx-num-15-7, decimal)".\9";
    counter-increment: docx-num-15-7;
  }
  p.docx-num-15-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -61.20pt;
    margin-left: 187.20pt;
  }
  p.docx-num-15-7 {
    counter-reset: docx-num-15-8;
  }
  p.docx-num-15-8:before {
    content: ""counter(docx-num-15-0, decimal)"."counter(docx-num-15-1, decimal)"."counter(docx-num-15-2, decimal)"."counter(docx-num-15-3, decimal)"."counter(docx-num-15-4, decimal)"."counter(docx-num-15-5, decimal)"."counter(docx-num-15-6, decimal)"."counter(docx-num-15-7, decimal)"."counter(docx-num-15-8, decimal)".\9";
    counter-increment: docx-num-15-8;
  }
  p.docx-num-15-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -72.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-7-0:before {
    content: "\9";
    counter-increment: docx-num-7-0;
    font-family: Symbol;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 54.00pt;
  }
  p.docx-num-7-0 {
    counter-reset: docx-num-7-1;
  }
  p.docx-num-7-1:before {
    content: "o\9";
    counter-increment: docx-num-7-1;
    font-family: Courier New;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 90.00pt;
  }
  p.docx-num-7-1 {
    counter-reset: docx-num-7-2;
  }
  p.docx-num-7-2:before {
    content: "\9";
    counter-increment: docx-num-7-2;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 126.00pt;
  }
  p.docx-num-7-2 {
    counter-reset: docx-num-7-3;
  }
  p.docx-num-7-3:before {
    content: "\9";
    counter-increment: docx-num-7-3;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 162.00pt;
  }
  p.docx-num-7-3 {
    counter-reset: docx-num-7-4;
  }
  p.docx-num-7-4:before {
    content: "\9";
    counter-increment: docx-num-7-4;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 198.00pt;
  }
  p.docx-num-7-4 {
    counter-reset: docx-num-7-5;
  }
  p.docx-num-7-5:before {
    content: "\9";
    counter-increment: docx-num-7-5;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 234.00pt;
  }
  p.docx-num-7-5 {
    counter-reset: docx-num-7-6;
  }
  p.docx-num-7-6:before {
    content: "\9";
    counter-increment: docx-num-7-6;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 270.00pt;
  }
  p.docx-num-7-6 {
    counter-reset: docx-num-7-7;
  }
  p.docx-num-7-7:before {
    content: "\9";
    counter-increment: docx-num-7-7;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 306.00pt;
  }
  p.docx-num-7-7 {
    counter-reset: docx-num-7-8;
  }
  p.docx-num-7-8:before {
    content: "\9";
    counter-increment: docx-num-7-8;
    font-family: Wingdings;
    min-height: 10.00pt;
    font-size: 10.00pt;
  }
  p.docx-num-7-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 342.00pt;
  }
  p.docx-num-28-0:before {
    content: ""counter(docx-num-28-0, decimal)".\9";
    counter-increment: docx-num-28-0;
  }
  p.docx-num-28-0 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 36.00pt;
  }
  p.docx-num-28-0 {
    counter-reset: docx-num-28-1;
  }
  p.docx-num-28-1:before {
    content: ""counter(docx-num-28-1, decimal)".\9";
    counter-increment: docx-num-28-1;
  }
  p.docx-num-28-1 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 72.00pt;
  }
  p.docx-num-28-1 {
    counter-reset: docx-num-28-2;
  }
  p.docx-num-28-2:before {
    content: ""counter(docx-num-28-2, decimal)".\9";
    counter-increment: docx-num-28-2;
  }
  p.docx-num-28-2 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 108.00pt;
  }
  p.docx-num-28-2 {
    counter-reset: docx-num-28-3;
  }
  p.docx-num-28-3:before {
    content: ""counter(docx-num-28-3, decimal)".\9";
    counter-increment: docx-num-28-3;
  }
  p.docx-num-28-3 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 144.00pt;
  }
  p.docx-num-28-3 {
    counter-reset: docx-num-28-4;
  }
  p.docx-num-28-4:before {
    content: ""counter(docx-num-28-4, decimal)".\9";
    counter-increment: docx-num-28-4;
  }
  p.docx-num-28-4 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 180.00pt;
  }
  p.docx-num-28-4 {
    counter-reset: docx-num-28-5;
  }
  p.docx-num-28-5:before {
    content: ""counter(docx-num-28-5, decimal)".\9";
    counter-increment: docx-num-28-5;
  }
  p.docx-num-28-5 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 216.00pt;
  }
  p.docx-num-28-5 {
    counter-reset: docx-num-28-6;
  }
  p.docx-num-28-6:before {
    content: ""counter(docx-num-28-6, decimal)".\9";
    counter-increment: docx-num-28-6;
  }
  p.docx-num-28-6 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 252.00pt;
  }
  p.docx-num-28-6 {
    counter-reset: docx-num-28-7;
  }
  p.docx-num-28-7:before {
    content: ""counter(docx-num-28-7, decimal)".\9";
    counter-increment: docx-num-28-7;
  }
  p.docx-num-28-7 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 288.00pt;
  }
  p.docx-num-28-7 {
    counter-reset: docx-num-28-8;
  }
  p.docx-num-28-8:before {
    content: ""counter(docx-num-28-8, decimal)".\9";
    counter-increment: docx-num-28-8;
  }
  p.docx-num-28-8 {
    display: list-item;
    list-style-position: inside;
    list-style-type: none;
    text-indent: -18.00pt;
    margin-left: 324.00pt;
  }
  .docx-wrapper {
    counter-reset: docx-num-25-0 docx-num-21-0 docx-num-20-0 docx-num-18-0 docx-num-39-0 docx-num-14-0 docx-num-41-0 docx-num-12-0 docx-num-11-0 docx-num-16-0 docx-num-36-0 docx-num-31-0 docx-num-4-0 docx-num-5-0 docx-num-2-0 docx-num-13-0 docx-num-29-0 docx-num-33-0 docx-num-26-0 docx-num-35-0 docx-num-10-0 docx-num-23-0 docx-num-24-0 docx-num-45-0 docx-num-22-0 docx-num-40-0 docx-num-30-0 docx-num-19-0 docx-num-38-0 docx-num-6-0 docx-num-32-0 docx-num-9-0 docx-num-1-0 docx-num-44-0 docx-num-37-0 docx-num-43-0 docx-num-34-0 docx-num-17-0 docx-num-3-0 docx-num-42-0 docx-num-8-0 docx-num-27-0 docx-num-15-0 docx-num-7-0 docx-num-28-0;
  }
</style>
<div class="docx-wrapper">
  <section class="docx" style="padding: 72pt; width: 595.25pt; min-height: 842pt;">
    <article>
      <p style="margin-bottom: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"><span style="font-family: Aptos; font-weight: bold; min-height: 12pt; font-size: 12pt;"> </span><span style="font-family: Aptos; font-weight: bold; min-height: 12pt; font-size: 12pt;"><span> </span> </span></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 14pt; font-size: 14pt;">Index</span></p>
      <p style="margin-bottom: 5.65pt; margin-right: 30.75pt; text-align: justify;"><span style="font-family: Aptos; font-weight: bold; min-height: 12pt; font-size: 12pt;"> </span></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"><span style="font-family: Aptos; font-weight: bold; min-height: 12pt; font-size: 12pt;"> </span></p>
      <table class="first-row first-col no-vband docx_tablegrid" style="width: auto;">
        <colgroup>
          <col style="width: 146.95pt;">
          <col style="width: 148.25pt;">
          <col style="width: 147.05pt;">
        </colgroup>
        <tr>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">S.NO</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">TOPIC</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">PAGE NO</span></p>
          </td>
        </tr>
        <tr>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">1.</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Introduction</span></p>
            <p class="docx_listparagraph docx-num-31-1" style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Motivation</span></p>
            <p class="docx_listparagraph docx-num-31-1" style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Objective</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">7-9</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">8</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">9</span></p>
          </td>
        </tr>
        <tr>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">2.</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Existing Work</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">10-12</span></p>
          </td>
        </tr>
        <tr>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">3.</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Topic of the work</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">3.1 Introduction</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">3.2 All About Data</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">3.3 Mapping to ML/DL</span></p>
            <p style="text-align: justify;"></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> 3.3.1 Type of Machine Learning Problem</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> 3.3.2 Metrices</span></p>
            <p style="text-align: justify;"></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">3.4 Exploratory Data Analysis</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">13-28</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">13</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">13</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">15</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">15</span></p>
            <p style="text-align: justify;"></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">15</span></p>
            <p style="text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">15</span></p>
          </td>
        </tr>
        <tr>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">4.</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Conclusion </span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">&amp; Future Work</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">28-30</span></p>
          </td>
        </tr>
        <tr>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">5.</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">References</span></p>
          </td>
          <td style="width: 150.25pt;">
            <p style="text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">30-31</span></p>
          </td>
        </tr>
      </table>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: center;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; margin-left: 8.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 0pt; line-height: 1; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-3-0" style="margin-bottom: 0pt; line-height: 1;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">INTRODUCTION</span></p>
      <p class="docx_listparagraph" style="margin-bottom: 0pt; line-height: 1; margin-left: 26.5pt; text-align: justify;"></p>
      <p class="docx_listparagraph" style="margin-bottom: 0pt; line-height: 1; margin-left: 26.5pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Efficient water management is a critical aspect of sustainable urban development, particularly as global populations rise and climatic patterns shift. Accurate forecasting of water demand plays a pivotal role in ensuring the optimised distribution of this essential resource. By predicting future consumption patterns, utilities and policymakers can mitigate the risks of water shortages, reduce operational costs, and enhance service reliability.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">This report explores the methodologies and tools employed in forecasting water demand, emphasizing their application in optimizing water distribution systems. It highlights the importance of integrating advanced technologies, such as machine learning algorithms and real-time data analytics, to enhance prediction accuracy. Additionally, the report examines case studies and best practices from various regions to provide actionable insights for water utility managers and planners.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">The discussion underscores the interdependence of demand forecasting and distribution network efficiency, illustrating how precise projections can lead to significant resource conservation, energy savings, and improved water access for communities. Ultimately, this analysis aims to contribute to the broader objective of achieving sustainable water resource management in the face of evolving challenges.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-3-1" style="margin-bottom: 5.2pt; line-height: 1.81; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Motivation</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Water is a vital resource that supports life, sustains ecosystems, and drives economic and social development. However, the increasing global population, rapid urbanization, and the unpredictable impacts of climate change are placing immense pressure on water resources. These challenges necessitate the efficient management of water supply systems to ensure equitable access, minimize waste, and support sustainable development.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">The process of forecasting water demand allows utility providers, policymakers, and engineers to anticipate future water needs and plan accordingly. This is crucial in minimizing the risks of over-supply, which leads to resource wastage and increased operational costs, as well as under-supply, which can disrupt daily life, hamper economic activities, and harm public health.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Moreover, the increasing adoption of smart water technologies and Internet of Things (IoT)-based solutions has created opportunities for more precise and dynamic demand forecasting. These innovations allow real-time monitoring of water consumption patterns and integration of diverse datasets, such as weather forecasts, population growth rates, and urban development plans.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">The motivation for focusing on optimized water distribution through demand forecasting also stems from its environmental and economic benefits. Efficient distribution reduces energy consumption associated with water treatment and pumping, thereby lowering greenhouse gas emissions.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">From an economic perspective, accurate demand forecasting minimizes financial losses by reducing costs associated with emergency responses, infrastructure overhauls, and water scarcity penalties</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">In conclusion, forecasting water demand for optimized distribution is not merely a technical challenge; it is a critical component of sustainable water resource management. By addressing this need, we can contribute to the broader goals of environmental conservation, economic efficiency, and societal well-being, while ensuring that future generations have access to this indispensable resource.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 6.35pt; text-align: justify;"></p>
      <p style="margin-bottom: 6.35pt; text-align: justify;"></p>
      <p style="margin-bottom: 6.35pt; text-align: justify;"></p>
      <p style="margin-bottom: 6.35pt; text-align: justify;"></p>
      <p style="margin-bottom: 6.35pt; text-align: justify;"></p>
      <p style="margin-bottom: 6.35pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-3-1" style="margin-bottom: 11.1pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Objective </span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">The primary objective of this report is to explore and outline methodologies for forecasting water demand to achieve optimized distribution, ensuring the efficient, equitable, and sustainable management of water resources.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> The focus is to develop a framework that integrates advanced predictive tools, innovative technologies, and actionable insights for addressing the challenges posed by growing water demand and constrained supply systems.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">This report aims to identify and evaluate various forecasting models that cater to both short-term operational needs and long-term strategic planning. </span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">The project aims to:</span></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Anticipate Future Water Needs:</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> Develop accurate models to predict short-term and long-term water demand based on various influencing factors.</span></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Optimize Resource Allocation: </span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Enhance the efficiency of water distribution systems by aligning supply with demand forecasts.</span></p>
      <p class="docx_listparagraph" style="text-align: justify;"></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Support Sustainable Development:</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> Minimize water wastage and ensure equitable distribution to address the needs of growing populations and urban areas.</span></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Enhance System Resilience</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">: Prepare for potential disruptions, such as climate change impacts, through dynamic and adaptable forecasting approaches.</span></p>
      <p class="docx_listparagraph" style="text-align: justify;"></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Promote Environmental Conservation:</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> Reduce the over-extraction of natural water sources and lower energy consumption related to water distribution.</span></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Ensure Economic Efficiency:</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> Decrease operational costs and mitigate financial risks associated with water scarcity or infrastructure inefficiencies.</span></p>
      <p class="docx_listparagraph" style="text-align: justify;"></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-20-0" style="margin-bottom: 5.2pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">Foster Public Trust:</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> Provide consistent and reliable water supply, building confidence in water management systems and authorities.</span></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; line-height: 1; margin-left: 54pt; text-align: justify;"></p>
      <p class="docx_listparagraph" style="text-align: justify;"></p>
      <p class="docx_listparagraph" style="line-height: 1; margin-left: 54pt; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Furthermore, the objective includes identifying strategies to implement these forecasting tools within water management frameworks to achieve sustainable and efficient resource allocation.</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> </span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-3-0" style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">EXI</span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">S</span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">TING WORK</span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;"> </span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Numerous studies and technological advancements have focused on forecasting water demand for optimized distribution. These efforts span statistical, machine learning, and hybrid </span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">modelling</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;"> approaches, as well as the integration of innovative tools like IoT and GIS-based systems. </span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">1. Dataset Preprocessing</span></p>
      <p class="docx-num-35-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Dataset Source: Groundwater consumption and rainfall data.</span></p>
      <p class="docx-num-35-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Feature Selection: Chose Water_Consumption as the target variable and Rainfall as an influencing factor.</span></p>
      <p class="docx-num-35-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Data Cleaning:</span></p>
      <p class="docx-num-35-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Renamed columns (Water_Consumption, Rainfall).</span></p>
      <p class="docx-num-35-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Handled missing values using fillna() and dropna().</span></p>
      <p class="docx-num-35-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Normalized data using MinMaxScaler() to scale values between 0 and 1.</span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">2. Time-Series Data Preparation</span></p>
      <p class="docx-num-36-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Converted dataset into sequences with a window size of 10 time steps.</span></p>
      <p class="docx-num-36-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Splitting Data: 80% for training, 20% for testing.</span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">3. LSTM Model Architecture</span></p>
      <p class="docx-num-37-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Why LSTM? Designed for sequential data and time-series forecasting.</span></p>
      <p class="docx-num-37-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Layers Used:</span></p>
      <p class="docx-num-37-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Two LSTM layers (each with 100 neurons).</span></p>
      <p class="docx-num-37-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Dense layers for output prediction.</span></p>
      <p class="docx-num-37-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Hyperparameters:</span></p>
      <p class="docx-num-37-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Optimizer: Adam</span></p>
      <p class="docx-num-37-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Loss Function: Mean Squared Error (MSE)</span></p>
      <p class="docx-num-37-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Epochs: 100</span></p>
      <p class="docx-num-37-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Batch Size: 16</span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">4. Model Training &amp; Evaluation</span></p>
      <p class="docx-num-38-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Model Training: The LSTM model was trained using model.fit() for 100 epochs.</span></p>
      <p class="docx-num-38-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Performance Metrics:</span></p>
      <p class="docx-num-38-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Training Loss vs. Validation Loss curve was analyzed.</span></p>
      <p class="docx-num-38-1" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Actual vs. Predicted values were plotted for comparison.</span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">5. Web Dashboard Deployment</span></p>
      <p class="docx-num-39-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Flask + Plotly used to create an interactive dashboard.</span></p>
      <p class="docx-num-39-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Predictions stored in predictions.csv and displayed dynamically.</span></p>
      <p class="docx-num-39-0" style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Users can view real-time forecasts via a web interface.</span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"></p>
      <p class="docx_listparagraph" style="margin-bottom: 5.2pt; line-height: 1; margin-left: 18pt; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 14pt; font-size: 14pt;">3. Proposed Work</span></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"><span>
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 451.25pt; height: 258.99pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 452.53pt; height: 259.72pt;" src="blob:https://4html.net/0f230f10-9f4a-477a-a552-59a7cfa37461"></div>
        </span></p>
      <p style="margin-top: 5pt; margin-bottom: 5pt; line-height: 1; text-align: justify;"><span>Figure </span><span> </span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">BLOCK DIAGRAM OF EXISTING PROJECTS</span></p>
      <p class="docx_caption" style="text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="margin-bottom: 5.2pt; line-height: 1; text-align: justify;"></p>
      <p style="text-align: justify;"></p>
      <p style="text-align: justify;"></p>
      <p style="text-align: justify;"></p>
    </article>
    <footer>
      <p class="docx_footer" style="text-align: center;"><span>33</span></p>
      <p class="docx_footer"></p>
    </footer>
  </section>
  <section class="docx" style="padding: 72pt; width: 595.3pt; min-height: 841.9pt;">
    <article>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Topic of the Work</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.1 Introduction</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Water management in rural areas has long faced challenges due to inefficiencies, limited resources, and a lack of data-driven decision-making tools. This project introduces a Predictive Analytics System for Water Demand and Distribution, which leverages historical data, artificial intelligence (AI), and machine learning (ML) to forecast water demand and optimize water distribution. By addressing issues such as unpredictable water consumption patterns and seasonal demand fluctuations, the proposed system ensures equitable and efficient water resource allocation.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The predictive system focuses on analyzing real-time and historical data, including population trends, agricultural usage, and weather conditions. Using advanced machine learning models, the project aims to minimize wastage, reduce shortages, and improve overall water management outcomes for rural regions.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.2 All About Data</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The success of any machine learning model depends on the quality and diversity of data. This section discusses the sources, nature, and preprocessing techniques applied to the data used in the project.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.2.1 Data Sources The project utilizes a variety of data sources to ensure accurate predictions:</span></p>
      <p class="docx-num-23-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Historical Water Consumption Data: Data on past water usage patterns for domestic, agricultural, and industrial purposes in rural areas.</span></p>
      <p class="docx-num-23-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Weather Data: Temperature, humidity, rainfall, and other climatic variables influencing water demand.</span></p>
      <p class="docx-num-23-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Population and Socio-Economic Data: Population growth, agricultural needs, and socio-economic trends impacting water requirements.</span></p>
      <p class="docx-num-23-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Seasonal Trends: Analysis of demand variations caused by seasonal changes.</span></p>
      <p class="docx-num-23-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">IoT and Sensor Data: Real-time data collected from water meters and sensors for dynamic adjustments.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.2.2 Data Preprocessing </span><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Data preprocessing is a critical step to prepare raw data for model training and analysis. The following techniques are applied:</span></p>
      <p class="docx-num-24-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Handling Missing Values: Imputation methods like mean/median replacement for missing records.</span></p>
      <p class="docx-num-24-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Normalization: Scaling data to ensure uniformity in units and magnitude.</span></p>
      <p class="docx-num-24-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Outlier Detection and Treatment: Identifying anomalies using statistical methods and ensuring data consistency.</span></p>
      <p class="docx-num-24-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Feature Engineering: Creating meaningful features such as water demand per capita, seasonal demand ratios, and weather-based indicators.</span></p>
      <p class="docx-num-24-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Time Series Formatting: Organizing data into time series format for accurate trend analysis and predictions.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.3 Mapping to ML/DL</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The system maps the problem of water demand forecasting and distribution optimization to machine learning and deep learning techniques.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.3.1 Type of Machine Learning Problem</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The water demand prediction problem is framed as a Supervised Learning Regression Problem. Given historical and real-time data inputs, the model predicts continuous values, such as daily or weekly water demand.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Key characteristics of the problem:</span></p>
      <p class="docx-num-25-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Input Features: Population size, weather parameters, historical water usage, seasonal trends, and real-time sensor readings.</span></p>
      <p class="docx-num-25-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Target Variable: Predicted water demand (measured in liters/day or equivalent).</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.3.2 Metrics</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">To evaluate the performance of the predictive models, the following metrics are used:</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">For Artificial Neural Networks (ANN):</span></p>
      <p class="docx-num-28-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Root Mean Squared Error (RMSE): Measures the standard deviation of the residuals (errors) between predicted and actual values. A lower RMSE indicates better model performance.</span></p>
      <p class="docx-num-28-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Mean Absolute Error (MAE): Computes the average absolute difference between predicted and actual values, providing a direct measure of prediction accuracy.</span></p>
      <p class="docx-num-28-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">R-Squared (R²): Evaluates how well the model explains the variance in the target variable.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">For Regression Models:</span></p>
      <p class="docx-num-29-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Mean Squared Error (MSE): Measures the average squared differences between predicted and actual values, penalizing larger errors more heavily.</span></p>
      <p class="docx-num-29-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Adjusted R-Squared: Similar to R² but adjusted for the number of predictors in the model, ensuring no overfitting occurs.</span></p>
      <p class="docx-num-29-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Mean Absolute Percentage Error (MAPE): Provides error as a percentage, useful for understanding relative prediction accuracy.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">For Support Vector Regression (SVR):</span></p>
      <p class="docx-num-30-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Epsilon-Insensitive Loss: Measures how predictions fall within a margin of tolerance (epsilon), ignoring small deviations.</span></p>
      <p class="docx-num-30-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">RMSE: Evaluates prediction accuracy by measuring error magnitude.</span></p>
      <p class="docx-num-30-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Correlation Coefficient (r): Assesses the strength and direction of the relationship between predicted and actual values.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">These metrics ensure that the system delivers reliable and precise forecasts, which are critical for optimizing water distribution.</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">3.4 Exploratory Data Analysis (EDA)</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Water Consumption Data</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt; background-color: red;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 206.2pt; height: 123.7pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 206.2pt; height: 123.7pt;" src="blob:https://4html.net/5db450dc-d8ca-4a84-bfc2-cf348fabfb8c"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:-60pt;margin-top:98.4pt;width:57.75pt;height:31.5pt;z-index:251659264;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="0" height="0">
              <g fill="#4472c4 [3204]"></g>
            </svg></div>
        </span><span>Figure </span><span> </span><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Inland Water resources in the country</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:-121.25pt;margin-top:48.8pt;width:8.55pt;height:17.05pt;z-index:251668480;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text" width="12" height="23">
              <image width="100%" height="100%" href="blob:https://4html.net/bb81968e-d90e-4a37-9c3f-8bf2d11da4ec"></image>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 429.05pt; height: 163.5pt; float: left;"><img style="position: relative; left: 0pt; top: 0pt; width: 429.05pt; height: 163.5pt;" src="blob:https://4html.net/414f6b35-133b-4c1d-904e-a11ebb4790e5"></div>
        </span><span>Figure </span><span> Madhya</span><span> </span><span>Pradesh Individual Data</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 162.42pt; height: 141.82pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 163.17pt; height: 142.47pt;" src="blob:https://4html.net/4397129a-e75b-49e9-86b4-19dc447cb5d5"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> States by total length of rivers and canals</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Madhya Pradesh total length of river and canal </span><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">is 16000 with 2.79 reservoirs 0.59 Tanks, and Pond, 0.1 Brackish Water with total of 8.11.</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 429pt; height: 168.54pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 429.06pt; height: 168.56pt;" src="blob:https://4html.net/80f4ca60-a290-43a9-86d9-8cd0fd7fb302"></div>
        </span><span>Figure </span><span> Estimated per capita availability of water in Different River Basins during 2010</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 401.25pt; height: 201.64pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 401.31pt; height: 201.67pt;" src="blob:https://4html.net/bc57809c-753f-4f2b-bf6c-3f4146e43bd9"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> Basin Wise flow and storage potential in India</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:555.25pt;margin-top:54.85pt;width:8.8pt;height:17.05pt;z-index:251664384;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text" width="12" height="23">
              <image width="100%" height="100%" href="blob:https://4html.net/ed5cdba4-85f9-403a-9d22-3d06006abb15"></image>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The States of Andhra Pradesh, Gujarat, Karnataka, Madhya Pradesh, Maharashtra, Orissa and Uttar Pradesh together account for about 72 % of total live storage capacity in the country.</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:0;margin-top:135.65pt;width:207.2pt;height:22.45pt;z-index:251670528;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:center;mso-position-horizontal-relative:margin;mso-position-vertical:absolute;mso-position-vertical-relative:text" width="277" height="30">
              <image width="100%" height="100%" href="blob:https://4html.net/d9af4c30-9b32-4dd3-bda5-45a3b3d713f5"></image>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:28.7pt;margin-top:130.45pt;width:57.75pt;height:31.5pt;z-index:251673600;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="0" height="0">
              <g fill="#4472c4 [3204]"></g>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 216pt; height: 237.75pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 216.03pt; height: 237.78pt;" src="blob:https://4html.net/9a3c05e1-8081-4e00-b7e9-754926afaa8f"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> Annual Replenishable Ground Water Resources</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">It shows 14 States comprise 91% of ground water potential. Among the States, in terms of share of replenishable ground water resources Madhya Pradesh (7.9%)</span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">.</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt; background-color: red;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 407.25pt; height: 179.59pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 407.31pt; height: 179.61pt;" src="blob:https://4html.net/1d493428-f4d1-4e16-b12a-42f8f9469308"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> </span><span> Annual Replenishable Ground Water Resources</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:22.85pt;margin-top:0;width:15.95pt;height:17.05pt;z-index:251674624;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text" width="22" height="23">
              <image width="100%" height="100%" href="blob:https://4html.net/71339da1-60df-439e-8918-c38d4dbbb1f0"></image>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:525.2pt;margin-top:86.2pt;width:8.55pt;height:17.05pt;z-index:251682816;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text" width="12" height="23">
              <image width="100%" height="100%" href="blob:https://4html.net/9c5d8e28-5f3c-49d8-b80d-c973a75d6e1a"></image>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;"> Orange Denotes For Annual Replenishable Ground Water Resources of Madhya Pradesh</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 413.31pt; height: 225.03pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 413.31pt; height: 225.03pt;" src="blob:https://4html.net/56561301-83b7-43d3-b3f4-472f5c96a3cf"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> Number of Dams By state</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">The maximum number of dams completed in the country in Madhya Pradesh are 899 finished with 7 Under Construction.</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:-37.5pt;margin-top:213.25pt;width:57.75pt;height:31.5pt;z-index:251681792;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:margin;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="0" height="0">
              <g fill="#4472c4 [3204]"></g>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 392.3pt; height: 282.79pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 392.3pt; height: 282.79pt;" src="blob:https://4html.net/fb0d3ddd-506e-4f34-bca6-35644b3602fa"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> Total Live Storage Capacity</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Water Availability</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 451.3pt; height: 37.75pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 451.3pt; height: 37.75pt;" src="blob:https://4html.net/a4916781-7c45-4c26-bbef-761a2418032c"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 215.86pt; height: 218.25pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 216.18pt; height: 218.58pt;" src="blob:https://4html.net/ed2b405e-a953-4321-9600-eaba3c43ac1a"></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 220.45pt; height: 219pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 221.38pt; height: 219.92pt;" src="blob:https://4html.net/c4c09c21-22ff-40fa-990b-ecc4b24f1c4f"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:171.75pt;margin-top:19.95pt;width:21.75pt;height:14.25pt;z-index:251687936;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="29" height="19">
              <rect width="100%" height="100%" fill="#70ad47 [3209]"></rect>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Per Capita Water availability for Sehore, Madhya Pradesh in the Year 2050 lies Under Stress category of 1000-1700m3</span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:174pt;margin-top:19.25pt;width:24.75pt;height:16.5pt;z-index:251689984;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="33" height="22">
              <rect width="100%" height="100%" fill="#70ad47 [3209]"></rect>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Per Capita Water availability for Sehore, Madhya Pradesh in the Year 2025 lies Under Stress category of 1000-1700m3</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Pre and Post Monsoon Water Levels</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 483.85pt; height: 21pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 489.87pt; height: 21.26pt;" src="blob:https://4html.net/cdf1e2e9-7217-4614-a1f4-797bc109a428"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 208.71pt; height: 222.62pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 210.02pt; height: 224.02pt;" src="blob:https://4html.net/30a96d10-37c2-406e-adf6-fac378ccd308"></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 219.75pt; height: 224.93pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 220.73pt; height: 225.93pt;" src="blob:https://4html.net/920c2236-adb6-46f7-b81f-a214474532f4"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:237pt;margin-top:18.25pt;width:26.25pt;height:16.5pt;z-index:251692032;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="35" height="22">
              <rect width="100%" height="100%" fill="#ed7d31 [3205]"></rect>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Pre-Monsoon</span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;"> Water availability for Sehore, Madhya Pradesh in the Year 2022-23 lies Under Moderately Deep Water level (10 to 20) </span></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div><svg style="position:absolute;margin-left:222.75pt;margin-top:17.55pt;width:27.75pt;height:18pt;z-index:251694080;visibility:visible;mso-wrap-style:square;mso-wrap-distance-left:9pt;mso-wrap-distance-top:0;mso-wrap-distance-right:9pt;mso-wrap-distance-bottom:0;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;mso-position-vertical:absolute;mso-position-vertical-relative:text;v-text-anchor:middle" width="37" height="24">
              <rect width="100%" height="100%" fill="#ffc000"></rect>
            </svg></div>
        </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Post Monsoon Water availability for Sehore, Madhya Pradesh in the Year 2022-23 lies Under Moderate </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Deep-Water</span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;"> level (5 to 10) </span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 451.3pt; height: 258.76pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 451.3pt; height: 258.76pt;" src="blob:https://4html.net/6f1a5a59-9636-43cc-8138-a0bc93998931"></div>
        </span><span>Figure </span><span> </span><span>District Wise Station Count in Sehore, Madhya Pradesh</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 451.3pt; height: 220.12pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 451.3pt; height: 220.12pt;" src="blob:https://4html.net/bd800fad-f55c-4819-9ccd-aaf9f5c5a5b0"></div>
        </span><span>Figure </span><span> </span><span>Monthly Ground Water Level Information</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 451.3pt; height: 336.5pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 451.3pt; height: 336.5pt;" src="blob:https://4html.net/86ef4b66-18fd-4d02-8feb-0b273fb3c30a"></div>
        </span><span>Figure </span><span> Ground Water Level in MP</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 153.77pt; height: 237.78pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 153.77pt; height: 237.78pt;" src="blob:https://4html.net/62b5067a-fe6a-4ce9-bc22-2793370edb03"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 417.06pt; height: 385.5pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 417.28pt; height: 385.7pt;" src="blob:https://4html.net/4dccfd33-7179-4168-a468-561822977146"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"><span>Figure </span><span> </span><span>Reservoir Fill Percentage in Sehore, Madhya Pradesh lie Between 50-70%</span></p>
      <p style="line-height: 1.16; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 242.55pt; height: 212.11pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 243pt; height: 212.51pt;" src="blob:https://4html.net/baa52821-6790-4a52-a5c9-a0ff81c9c7f5"></div>
        </span></p>
      <p style="line-height: 1.16; text-align: center;"></p>
      <p style="line-height: 1.16; text-align: center;"></p>
      <p style="line-height: 1.16;"></p>
      <p style="line-height: 1.16;"><br></p>
      <p style="line-height: 1.16;"></p>
      <p style="line-height: 1.16;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p class="docx_listparagraph docx-num-30-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 14pt; font-size: 14pt;">Conclusion &amp; Future Work</span></p>
      <p class="docx_listparagraph" style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">4.1 </span><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">Conclusion</span></p>
      <p class="docx_listparagraph docx-num-40-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The LSTM-based forecasting model effectively predicts water demand, allowing for optimized resource distribution.</span></p>
      <p class="docx_listparagraph docx-num-40-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">The Flask dashboard enables real-time visualization, making predictions accessible to decision-makers.</span></p>
      <p style="line-height: 1.16; margin-left: 18pt; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 380.36pt; height: 204.18pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 381.51pt; height: 204.79pt;" src="blob:https://4html.net/33816623-e67d-4a5b-8f67-f1c98862574c"></div>
        </span></p>
      <p style="line-height: 1.16; margin-left: 18pt; text-align: center;"><span>Figure </span><span> Water Demanding Forecasting</span></p>
      <p style="line-height: 1.16; margin-left: 18pt; text-align: center;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">
          <div style="display: inline-block; position: relative; text-indent: 0px; width: 393.27pt; height: 226.39pt;"><img style="position: relative; left: 0pt; top: 0pt; width: 394.09pt; height: 226.87pt;" src="blob:https://4html.net/16fa247f-b91d-4c3e-8885-f67dcfaffd75"></div>
        </span></p>
      <p style="line-height: 1.16; margin-left: 18pt; text-align: center;"><span>Figure </span><span> Loss Curve</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 12pt; font-size: 12pt;">4.2 Future Improvements</span></p>
      <p class="docx-num-33-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Enhance dataset: Include temperature, humidity, and population growth for more accurate predictions.</span></p>
      <p class="docx-num-33-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Optimize hyperparameters for improved model performance.</span></p>
      <p class="docx-num-33-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Deploy on a cloud platform like AWS/GCP for large-scale real-time forecasting.</span></p>
      <p class="docx-num-33-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;">Compare with other models like GRU, Transformer networks, or hybrid approaches.</span></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; font-weight: bold; color: black; min-height: 14pt; font-size: 14pt;">5.Reference</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">H</span><span style="font-family: &quot;Times New Roman&quot;; color: black; min-height: 12pt; font-size: 12pt;"> </span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Neural Computation</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 9, no. 8, pp. 1735–1780, 1997.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">J. Brownlee, </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Deep Learning for Time Series Forecasting</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, Machine Learning Mastery, 2018.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">F. Chollet, </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Deep Learning with Python</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, Manning Publications, 2017.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">G. Zhang, B. Eddy Patuwo, and M. Y. Hu, “Forecasting with artificial neural networks: The state of the art,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Int. J. Forecasting</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 14, no. 1, pp. 35–62, 1998.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Y. S. Abu-Mostafa, M. Magdon-Ismail, and H. T. Lin, </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Learning from Data</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, AMLBook, 2012.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">T. Asefa, et al., “Multivariate short-term water demand forecasting using artificial neural networks,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">J. Water Resour. Plann. Manage.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 132, no. 1, pp. 10–20, 2006.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">M. Herrera, et al., “Short-term water demand forecasting using artificial neural networks,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">J. Hydrol.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 387, no. 1–2, pp. 28–38, 2010.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">J. Adamowski and C. Karapataki, “Comparison of MLR and ANN models for urban water demand forecasting,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">J. Hydrol.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 408, no. 1, pp. 28–34, 2011.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">S. Mohan and S. Ahilan, “Water Demand Forecasting using Deep Learning,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Int. J. Sci. Res. Sci. Technol.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 5, no. 6, pp. 456–461, 2019.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">S. Pande and M. Sivapalan, “Data and modeling innovations for water management,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Hydrol. Earth Syst. Sci.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 20, pp. 3541–3556, 2016.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">A. Graves, </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Supervised Sequence Labelling with Recurrent Neural Networks</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, Springer, 2012.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">F. A. Gers, J. Schmidhuber, and F. Cummins, “Learning to forget: Continual prediction with LSTM,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Neural Comput.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 12, no. 10, pp. 2451–2471, 2000.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">J. Bergstra and Y. Bengio, “Random search for hyper-parameter optimization,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">J. Mach. Learn. Res.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, vol. 13, pp. 281–305, 2012.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">I. Goodfellow, Y. Bengio, and A. Courville, </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Deep Learning</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, MIT Press, 2016.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">S. Ioffe and C. Szegedy, “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift,” </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Proc. 32nd Int. Conf. Mach. Learn.</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, 2015.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Central Ground Water Board (CGWB), India, “Annual Ground Water Report,” 2020.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">India Meteorological Department (IMD), “Rainfall Statistics of India,” Govt. of India, 2021.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Ministry of Jal Shakti, “National Compilation on Dynamic Ground Water Resources,” Govt. of India, 2022.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Kaggle, “Water Demand Forecasting Dataset,” [Online]. Available: </span><a href="https://www.kaggle.com"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://www.kaggle.com</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">WHO/UNICEF JMP, “Progress on Drinking Water, Sanitation and Hygiene,” 2021.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">TensorFlow, “TensorFlow Official Documentation,” [Online]. Available: </span><a href="https://www.tensorflow.org"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://www.tensorflow.org</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Keras, “Keras Documentation,” [Online]. Available: </span><a href="https://keras.io"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://keras.io</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Wes McKinney, </span><span style="font-family: &quot;Times New Roman&quot;; font-style: italic; min-height: 12pt; font-size: 12pt;">Python for Data Analysis</span><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">, O’Reilly Media, 2017.</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">NumPy Developers, “NumPy Documentation,” [Online]. Available: </span><a href="https://numpy.org"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://numpy.org</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Matplotlib Developers, “Matplotlib Documentation,” [Online]. Available: </span><a href="https://matplotlib.org"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://matplotlib.org</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Scikit-learn Developers, “Scikit-learn Documentation,” [Online]. Available: </span><a href="https://scikit-learn.org"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://scikit-learn.org</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Plotly, “Plotly for Python,” [Online]. Available: https://plotly.com/python/</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Flask, “Flask Documentation,” [Online]. Available: https://flask.palletsprojects.com</span></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">GitHub, “Open-Source Water Forecasting Repositories,” [Online]. Available: </span><a href="https://github.com"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://github.com</span></a></p>
      <p class="docx-num-43-0" style="line-height: 1.16; text-align: justify;"><span style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">Python Software Foundation, “Python 3 Documentation,” [Online]. Available: </span><a href="https://docs.python.org/3/"><span class="docx_hyperlink" style="font-family: &quot;Times New Roman&quot;; min-height: 12pt; font-size: 12pt;">https://docs.python.org/3/</span></a></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16;"></p>
      <p style="line-height: 1.16;"><br></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16; text-align: justify;"></p>
      <p style="line-height: 1.16;"></p>
    </article>
    <footer>
      <p></p>
    </footer>
  </section>
</div>
