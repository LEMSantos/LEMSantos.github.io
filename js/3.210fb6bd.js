(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[3],{"0c5d":function(t,e,a){},"11b1":function(t,e,a){},1467:function(t,e,a){t.exports=a.p+"img/home-image.1c53d476.webp"},"182b":function(t,e,a){},"33e8":function(t,e,a){t.exports=a.p+"img/quasar-logo.f4cb2b69.webp"},4042:function(t,e,a){"use strict";var s=a("0c5d"),o=a.n(s);o.a},"443f":function(t,e,a){"use strict";var s=a("182b"),o=a.n(s);o.a},5210:function(t,e,a){t.exports=a.p+"img/flask-icon.e9419c41.webp"},"52aa":function(t,e,a){"use strict";var s=a("11b1"),o=a.n(s);o.a},"950c":function(t,e,a){t.exports=a.p+"img/octocat.20d1cda6.webp"},"9d63":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("q-img",{staticClass:"full-width q-mb-lg",attrs:{src:t.image}}),a("p",{staticClass:"ellipsis-2-lines text-h6 display-block max-title-height",class:{"text-center":t.centerText}},[t._v("\n    "+t._s(t.title)+"\n  ")]),a("p",{staticClass:"text-justify"},[t._v("\n    "+t._s(t.abstract)+"\n  ")]),a("div",{staticClass:"row justify-between"},[a("q-btn",{attrs:{label:"Ler mais",color:"primary",flat:"","no-caps":"",padding:"none",to:"/blog/"+t.id+"/"+t.formatTitle(t.title),exact:""}}),a("span",{staticClass:"op-50"},[t._v("\n      Publicado em "+t._s(t._f("moment")(t.publishDate,"DD/MM/YYYY"))+"\n    ")])],1)],1)},o=[],n={props:{id:{type:Number,required:!0},title:{type:String,default:""},image:{type:String,default:""},abstract:{type:String,default:""},publishDate:{type:String,default:""},centerText:{type:Boolean,default:!1}},methods:{formatTitle(t){return t.split(" ").map(t=>t.toLowerCase()).join("-")}}},i=n,l=(a("52aa"),a("2877")),c=a("068f"),r=a("9c40"),m=a("eebe"),d=a.n(m),u=Object(l["a"])(i,s,o,!1,null,"4c8a5ee3",null);e["a"]=u.exports;d()(u,"components",{QImg:c["a"],QBtn:r["a"]})},bc13:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("q-page",[s("page-section",{staticClass:"row",class:{"q-gutter-x-lg":t.$q.screen.gt.sm},attrs:{"hide-header":""}},[s("div",{staticClass:"col-md col-xs-12"},[s("p",{staticClass:"text-weight-bold",class:{"text-h3 q-mb-lg":t.$q.screen.gt.sm,"text-h4 q-mb-xs text-center":!t.$q.screen.gt.sm}},[t._v("\n        Lucas Eliaquim\n      ")]),s("p",{class:t.$q.screen.gt.sm?"text-h5 q-mb-xl":"text-subtitle1 q-mb-lg text-center"},[t._v("\n        Cientista de Dados\n      ")]),s("div",{staticClass:"flex flex-center"},[t.$q.screen.gt.sm?t._e():s("q-img",{staticClass:"home-image-size",attrs:{src:a("1467"),"spinner-color":"white",alt:"ainda não há nenhum post"}})],1),t.$q.screen.gt.sm?s("p",{staticClass:"text-justify q-mb-xl text-subtitle1"},[t._v("\n        Sou estudante de Engenharia da Computação na UNIVASF, fascinado pelas áreas de Data\n        Science e Data Engineering, além de gostar de qualquer coisa relacionada com Inteligência\n        Artificial. Almejo alcançar altas posições na área que gosto e viajar pelo mundo inteiro.\n        Tento ser bem humorado e as vezes enérgico, mas gosto de discutir quando o assunto é R\n        vs Python ou como a Inteligência Artificial vai dominar o mundo.\n      ")]):s("p",{staticClass:"text-center text-subtitle1"},[t._v("\n        Estudante de Engenharia da Computação na UNIVASF, fascinado pelas áreas de Data Science\n        e Data Engineering, além de gostar de qualquer coisa relacionada com\n        Inteligência Artificial.\n      ")]),t.$q.screen.gt.sm?s("div",[s("q-btn",{staticClass:"q-py-xs q-mr-md",attrs:{color:"primary",label:"Ver o Portfólio",icon:"fas fa-code","text-color":"white",to:"/portfolio",unelevated:"","no-caps":""}}),s("q-btn",{staticClass:"q-py-xs",attrs:{color:"secondary",label:"Ver o Currículo",icon:"fas fa-file-alt","text-color":"white",to:"/resume",unelevated:"","no-caps":""}})],1):s("div",{staticClass:"row justify-center"},t._l(t.socialMedias,(function(t,e){return s("q-btn",{key:e,staticClass:"q-mr-md",attrs:{type:"a",target:"_blank",href:t.link,"aria-label":t.name,rel:"noopener",color:"primary",outline:"",round:""}},[s("q-icon",{attrs:{name:t.icon,color:"black"}})],1)})),1)]),t.$q.screen.gt.sm?s("div",{staticClass:"col-auto"},[s("q-img",{staticClass:"home-image-size",attrs:{src:a("1467"),"spinner-color":"white"}})],1):t._e()]),s("page-section",{attrs:{title:"O que eu faço","center-title":!t.$q.screen.gt.sm}},[s("div",{staticClass:"row q-col-gutter-x-lg q-col-gutter-y-xl q-mt-xs"},[s("what-i-do-section",{staticClass:"col-md-3 col-sm-6 col-xs-12",attrs:{title:"Python & Flask",icons:[{name:"fab fa-python",color:"#456E9C"},{name:"img:"+a("5210"),color:"#64B687"}]}},[t._v("\n        Utilizando Python, construo aplicações relacionadas à inteligência artificial, em áreas\n        como, Machine Learning, Processamento de Linguagem Natural e Business Intelligence, com\n        pipelines que vão desde os estudos iniciais até o deploy utilizando Flask.\n      ")]),s("what-i-do-section",{staticClass:"col-md-3 col-sm-6 col-xs-12",attrs:{title:"JavaScript, Html & Css",icons:[{name:"fab fa-js-square",color:"#F1DE4F"},{name:"fab fa-html5",color:"#DE6E3C"},{name:"fab fa-css3-alt",color:"#53A7DC"}]}},[t._v("\n        Com a stack básica do desenvolvimento web, posso construir aplicações simples, porém\n        robustas e leves para oferecer uma melhor experiência para o usuário final.\n      ")]),s("what-i-do-section",{staticClass:"col-md-3 col-sm-6 col-xs-12",attrs:{title:"Docker",icons:[{name:"fab fa-docker",color:"#1488C6"}]}},[t._v("\n        Com o Docker, construo ambientes personalizados para desenvolvimento e deploy em produção,\n        além de trabalhar com CI no Gitlab, e o uso de containers para facilitar atividades\n        rotineiras e que podem ser automatizadas.\n      ")]),s("what-i-do-section",{staticClass:"col-md-3 col-sm-6 col-xs-12",attrs:{title:"Vue & Quasar",icons:[{name:"fab fa-vuejs",color:"#64B687"},{name:"img:"+a("33e8"),color:"#64B687"}]}},[t._v("\n        Com Vue e Quasar, construo aplicações escaláveis e de fácil manutenção, que podem variar\n        entre os tipos: SPA, SSR, PWA, Aplicações Mobile, Aplicações de Desktop e Extensões de\n        Browser. Além disso, posso desenvolver apenas com o Vue sem o uso de frameworks, como\n        também, junto com a maioria dos frameworks disponíveis no mercado.\n      ")])],1)]),s("page-section",{attrs:{title:"Últimos Posts do Blog","center-title":!t.$q.screen.gt.sm}},[t.loadingBlogPosts?s("div",{staticClass:"relative-position flex flex-center q-py-xl"},[s("q-spinner-grid",{staticClass:"q-my-xl",attrs:{color:"primary",size:"50px"}})],1):t.errorFetchLatestBlogPosts?s("div",{staticClass:"q-mt-md"},[s("q-banner",{staticClass:"text-white bg-negative rounded-borders",attrs:{"inline-actions":""}},[t._v("\n        Houve um erro ao recuperar os últimos posts do blog.\n      ")])],1):t.latestBlogPosts.length?s("div",{staticClass:"row q-col-gutter-xl q-mt-xs q-mb-xl"},[t._l(t.latestBlogPosts,(function(e,a){return s("blog-post",t._b({key:a,staticClass:"col-md-4 col-sm-6 col-xs-12",attrs:{"publish-date":e.created_at,"center-text":t.$q.screen.lt.sm}},"blog-post",e,!1))})),t.$q.screen.lt.md?t._e():s("div",{staticClass:"col-12"},[s("q-btn",{staticClass:"q-py-xs q-mr-md",attrs:{color:"primary",label:"Ver o Blog",icon:"fas fa-blog","text-color":"white",to:"/blog",unelevated:"","no-caps":""}})],1)],2):s("div",{staticClass:"column items-center q-gutter-y-md q-pt-xl"},[s("q-icon",{attrs:{name:"img:"+a("950c"),size:"250px"}}),s("span",{staticClass:"text-h5 text-weight-bold op-80 q-mb-xl"},[t._v("\n        Não há nenhum post ainda.\n      ")])],1)])],1)},o=[],n=(a("e6cf"),a("a79d"),a("ded3")),i=a.n(n),l=a("fd2d"),c=a("9d63"),r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"column",class:t.$q.screen.gt.sm?"text-justify":"text-center"},[a("div",t._l(t.icons,(function(e,s){return a("q-icon",{key:s,staticClass:"icon-height",class:s<t.icons.length-1?"q-mr-md":"",style:e.color?"color: "+e.color:"",attrs:{name:e.name,size:"30px"}})})),1),a("p",{staticClass:"text-weight-bold text-subtitle1"},[t._v("\n    "+t._s(t.title)+"\n  ")]),a("p",[t._t("default")],2)])},m=[],d={props:{title:{type:String,default:""},icons:{type:Array,default:()=>[]}}},u=d,p=(a("443f"),a("2877")),g=a("0016"),f=a("eebe"),b=a.n(f),h=Object(p["a"])(u,r,m,!1,null,"24d55af7",null),x=h.exports;b()(h,"components",{QIcon:g["a"]});var q=a("dde5f"),v={name:"HomePage",components:{PageSection:l["a"],BlogPost:c["a"],WhatIDoSection:x},data(){return{latestBlogPosts:[],errorFetchLatestBlogPosts:!1,socialMedias:[{name:"link do github",icon:"fab fa-github-alt",link:"https://github.com/LEMSantos"},{name:"link do linkedin",icon:"fab fa-linkedin-in",link:"https://www.linkedin.com/in/lucas-eliaquim-1a7675181/"},{name:"link do email",icon:"fas fa-envelope",link:"mailto:lucas_m-santos@hotmail.com"}],loadingBlogPosts:!1}},mounted(){this.loadingBlogPosts=!0,this.getLatestBlogPosts().then(({data:t})=>{this.latestBlogPosts=t}).catch(()=>{this.errorFetchLatestBlogPosts=!0}).finally(()=>{this.loadingBlogPosts=!1})},methods:i()({},q["a"])},C=v,y=(a("4042"),a("9989")),_=a("068f"),w=a("9c40"),k=a("981c"),B=a("54e1"),P=Object(p["a"])(C,s,o,!1,null,null,null);e["default"]=P.exports;b()(P,"components",{QPage:y["a"],QImg:_["a"],QBtn:w["a"],QIcon:g["a"],QSpinnerGrid:k["a"],QBanner:B["a"]})},dde5f:function(t,e,a){"use strict";a("5319");var s=a("bc3a"),o=a.n(s);const n=()=>{const t='"https://personal-web-page-api.herokuapp.com"'.replace(/"/g,"");return o.a.get(t+"/latest-posts")};var i=n;const l=t=>{const e='"https://personal-web-page-api.herokuapp.com"'.replace(/"/g,"");return o.a.get(`${e}/posts?p=${t}`)};var c=l;e["a"]={getLatestBlogPosts:i,getBlogPosts:c}},fd2d:function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"q-my-xl"},[t.hideHeader?t._e():[a("div",{staticClass:"text-h4 q-mb-xs text-weight-bold",class:{"text-center":t.centerTitle,"text-h4":t.$q.screen.gt.sm,"text-h6":!t.$q.screen.gt.sm}},[t._v("\n      "+t._s(t.title)+"\n    ")]),a("q-separator",{staticClass:"op-30",attrs:{color:"black"}})],t._t("default")],2)},o=[],n={props:{title:{type:String,default:""},hideHeader:{type:Boolean,default:!1},centerTitle:{type:Boolean,default:!1}}},i=n,l=a("2877"),c=a("eb85"),r=a("eebe"),m=a.n(r),d=Object(l["a"])(i,s,o,!1,null,"b61a10c0",null);e["a"]=d.exports;m()(d,"components",{QSeparator:c["a"]})}}]);