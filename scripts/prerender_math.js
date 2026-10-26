// Pre-render TeX in an answer-*.html into inline SVG (no MathJax at view time).
// Usage: node scripts/prerender_math.js in.html out.html   (needs mathjax-full in NODE_PATH)
const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages, inlineMath: [['$','$'],['\\(','\\)']], displayMath: [['$$','$$'],['\\[','\\]']]});
const svg = new SVG({fontCache: 'none'});
const [, , inp, outp] = process.argv;
let html = fs.readFileSync(inp, 'utf8');
html = html.replace(/<script>\s*window\.MathJax[\s\S]*?<\/script>\s*/,'')
           .replace(/<script async src="https:\/\/cdn\.jsdelivr\.net\/npm\/mathjax[^"]*"><\/script>\s*/,'');
const doc = mathjax.document(html, {InputJax: tex, OutputJax: svg});
doc.render();
let out = adaptor.outerHTML(adaptor.root(doc.document));
out = out.replace('</head>', `<style>${adaptor.textContent(svg.styleSheet(doc))}</style></head>`);
fs.writeFileSync(outp, '<!DOCTYPE html>\n' + out);
