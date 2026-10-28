const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync((process.argv[2] || require('node:path').join(__dirname,'../assets/template/index.html')),'utf8');
const listeners={},scrollListeners={},dialog={open:false};
class Element{
 constructor(kind='article',parent=null){this.kind=kind;this.parent=parent;this.attrs={};this.handlers={};this.classes=new Set();this.dataset={cardTitle:'Example'};this.inert=false;this.bounds={top:100,bottom:350};this.classList={add:x=>this.classes.add(x),remove:x=>this.classes.delete(x),contains:x=>this.classes.has(x),toggle:(x,on)=>{if(on===undefined)on=!this.classes.has(x);on?this.classes.add(x):this.classes.delete(x);return on;}};}
 setAttribute(k,v){this.attrs[k]=String(v);}hasAttribute(k){return k in this.attrs;}getAttribute(k){return this.attrs[k];}
 matches(selector){return selector.split(',').some(x=>{x=x.trim();return x==='[data-flip-card]'?this.kind==='flip':x.startsWith('[')?this.hasAttribute(x.slice(1,-1)):x===this.kind;});}
 closest(selector){return this.matches(selector)?this:this.parent?.closest(selector)||null;}
 querySelector(selector){return this.parts?.[selector]||null;}
 addEventListener(type,fn){(this.handlers[type]??=[]).push(fn);}getBoundingClientRect(){return this.bounds;}focus(){}
 click(){const e={target:this,preventDefault(){}};(listeners.click||[]).filter(x=>x.capture).forEach(x=>x.fn(e));for(let n=this;n;n=n.parent)(n.handlers.click||[]).forEach(fn=>fn(e));(listeners.click||[]).filter(x=>!x.capture).forEach(x=>x.fn(e));}
}
const flip=new Element('flip');flip.parts={'.flip-card__front':new Element('div',flip),'.flip-card__back':new Element('div',flip),'.flip-card__toggle':new Element('button',flip)};flip.parts['.flip-card__toggle'].parts={'.flip-card__toggle-label':new Element('span')};
const stat=new Element(),second=new Element(),native=new Element('details'),toggle=new Element('button');
const cards=[flip,stat,second,native];
const doc={querySelectorAll:selector=>selector==='[data-flip-card]'?[flip]:cards,addEventListener(type,fn,capture){(listeners[type]??=[]).push({fn,capture});},getElementById:()=>dialog};
const context=vm.createContext({document:doc,toggle,editing:false,innerHeight:900,addEventListener(type,fn){scrollListeners[type]=fn;}});
const flipCode=html.slice(html.indexOf(' const flipCards='),html.indexOf(" toggle.addEventListener('click',()=>{editing=!editing"));
vm.runInContext(flipCode,context);
vm.runInContext(html.split(' // Presenter spotlight:')[1].split(' // End presenter spotlight.')[0].replace(/^ capture selection before native flip\/expand handlers run\.\n/,''),context);
flip.parts['.flip-card__front'].click();assert(flip.classes.has('is-flipped'));assert(flip.classes.has('is-spotlit'));
stat.click();assert(stat.classes.has('is-spotlit'));assert.equal(stat.attrs['aria-pressed'],'true');assert(!flip.classes.has('is-spotlit'));assert(flip.classes.has('is-flipped'));
second.click();assert(!stat.classes.has('is-spotlit'));assert.equal(stat.attrs['aria-pressed'],'false');assert(second.classes.has('is-spotlit'));
const key=(target,key)=>listeners.keydown.forEach(x=>x.fn({target,key,preventDefault(){}}));
key(second,'Escape');assert(!second.classes.has('is-spotlit'));
key(stat,'Enter');assert(stat.classes.has('is-spotlit'));key(second,' ');assert(second.classes.has('is-spotlit'));
vm.runInContext('editing=true',context);stat.click();assert(!stat.classes.has('is-spotlit'));vm.runInContext('editing=false',context);
second.bounds={top:-400,bottom:40};scrollListeners.scroll();assert(!second.classes.has('is-spotlit'));
assert(!native.hasAttribute('data-spotlight-button'));native.click();assert(native.classes.has('is-spotlit'));
dialog.open=true;key(native,'Escape');assert(native.classes.has('is-spotlit'));dialog.open=false;key(native,'Escape');assert(!native.classes.has('is-spotlit'));
for(const m of html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g))new vm.Script(m[1]);
console.log('Passed: flip + spotlight, static selection, exclusive spotlight, keyboard selection, Escape, edit guard, scroll cleanup, native details, modal guard, and script syntax');
