!function(e){var t={};function r(n){if(t[n])return t[n].exports;var o=t[n]={i:n,l:!1,exports:{}};return e[n].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=e,r.c=t,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)r.d(n,o,function(t){return e[t]}.bind(null,o));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="",r(r.s=3)}([function(e,t,r){"use strict";e.exports=r(1)},function(e,t,r){"use strict";
/** @license React v16.13.1
 * react.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var n=r(2),o="function"==typeof Symbol&&Symbol.for,l=o?Symbol.for("react.element"):60103,s=o?Symbol.for("react.portal"):60106,i=o?Symbol.for("react.fragment"):60107,a=o?Symbol.for("react.strict_mode"):60108,c=o?Symbol.for("react.profiler"):60114,u=o?Symbol.for("react.provider"):60109,p=o?Symbol.for("react.context"):60110,f=o?Symbol.for("react.forward_ref"):60112,d=o?Symbol.for("react.suspense"):60113,h=o?Symbol.for("react.memo"):60115,m=o?Symbol.for("react.lazy"):60116,v="function"==typeof Symbol&&Symbol.iterator;function y(e){for(var t="https://reactjs.org/docs/error-decoder.html?invariant="+e,r=1;r<arguments.length;r++)t+="&args[]="+encodeURIComponent(arguments[r]);return"Minified React error #"+e+"; visit "+t+" for the full message or use the non-minified dev environment for full errors and additional helpful warnings."}var g={isMounted:function(){return!1},enqueueForceUpdate:function(){},enqueueReplaceState:function(){},enqueueSetState:function(){}},b={};function E(e,t,r){this.props=e,this.context=t,this.refs=b,this.updater=r||g}function w(){}function S(e,t,r){this.props=e,this.context=t,this.refs=b,this.updater=r||g}E.prototype.isReactComponent={},E.prototype.setState=function(e,t){if("object"!=typeof e&&"function"!=typeof e&&null!=e)throw Error(y(85));this.updater.enqueueSetState(this,e,t,"setState")},E.prototype.forceUpdate=function(e){this.updater.enqueueForceUpdate(this,e,"forceUpdate")},w.prototype=E.prototype;var _=S.prototype=new w;_.constructor=S,n(_,E.prototype),_.isPureReactComponent=!0;var T={current:null},x=Object.prototype.hasOwnProperty,C={key:!0,ref:!0,__self:!0,__source:!0};function O(e,t,r){var n,o={},s=null,i=null;if(null!=t)for(n in void 0!==t.ref&&(i=t.ref),void 0!==t.key&&(s=""+t.key),t)x.call(t,n)&&!C.hasOwnProperty(n)&&(o[n]=t[n]);var a=arguments.length-2;if(1===a)o.children=r;else if(1<a){for(var c=Array(a),u=0;u<a;u++)c[u]=arguments[u+2];o.children=c}if(e&&e.defaultProps)for(n in a=e.defaultProps)void 0===o[n]&&(o[n]=a[n]);return{$$typeof:l,type:e,key:s,ref:i,props:o,_owner:T.current}}function k(e){return"object"==typeof e&&null!==e&&e.$$typeof===l}var j=/\/+/g,D=[];function P(e,t,r,n){if(D.length){var o=D.pop();return o.result=e,o.keyPrefix=t,o.func=r,o.context=n,o.count=0,o}return{result:e,keyPrefix:t,func:r,context:n,count:0}}function L(e){e.result=null,e.keyPrefix=null,e.func=null,e.context=null,e.count=0,10>D.length&&D.push(e)}function R(e,t,r){return null==e?0:function e(t,r,n,o){var i=typeof t;"undefined"!==i&&"boolean"!==i||(t=null);var a=!1;if(null===t)a=!0;else switch(i){case"string":case"number":a=!0;break;case"object":switch(t.$$typeof){case l:case s:a=!0}}if(a)return n(o,t,""===r?"."+M(t,0):r),1;if(a=0,r=""===r?".":r+":",Array.isArray(t))for(var c=0;c<t.length;c++){var u=r+M(i=t[c],c);a+=e(i,u,n,o)}else if(null===t||"object"!=typeof t?u=null:u="function"==typeof(u=v&&t[v]||t["@@iterator"])?u:null,"function"==typeof u)for(t=u.call(t),c=0;!(i=t.next()).done;)a+=e(i=i.value,u=r+M(i,c++),n,o);else if("object"===i)throw n=""+t,Error(y(31,"[object Object]"===n?"object with keys {"+Object.keys(t).join(", ")+"}":n,""));return a}(e,"",t,r)}function M(e,t){return"object"==typeof e&&null!==e&&null!=e.key?function(e){var t={"=":"=0",":":"=2"};return"$"+(""+e).replace(/[=:]/g,(function(e){return t[e]}))}(e.key):t.toString(36)}function N(e,t){e.func.call(e.context,t,e.count++)}function Y(e,t,r){var n=e.result,o=e.keyPrefix;e=e.func.call(e.context,t,e.count++),Array.isArray(e)?$(e,n,r,(function(e){return e})):null!=e&&(k(e)&&(e=function(e,t){return{$$typeof:l,type:e.type,key:t,ref:e.ref,props:e.props,_owner:e._owner}}(e,o+(!e.key||t&&t.key===e.key?"":(""+e.key).replace(j,"$&/")+"/")+r)),n.push(e))}function $(e,t,r,n,o){var l="";null!=r&&(l=(""+r).replace(j,"$&/")+"/"),R(e,Y,t=P(t,l,n,o)),L(t)}var A={current:null};function H(){var e=A.current;if(null===e)throw Error(y(321));return e}var B={ReactCurrentDispatcher:A,ReactCurrentBatchConfig:{suspense:null},ReactCurrentOwner:T,IsSomeRendererActing:{current:!1},assign:n};t.Children={map:function(e,t,r){if(null==e)return e;var n=[];return $(e,n,null,t,r),n},forEach:function(e,t,r){if(null==e)return e;R(e,N,t=P(null,null,t,r)),L(t)},count:function(e){return R(e,(function(){return null}),null)},toArray:function(e){var t=[];return $(e,t,null,(function(e){return e})),t},only:function(e){if(!k(e))throw Error(y(143));return e}},t.Component=E,t.Fragment=i,t.Profiler=c,t.PureComponent=S,t.StrictMode=a,t.Suspense=d,t.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED=B,t.cloneElement=function(e,t,r){if(null==e)throw Error(y(267,e));var o=n({},e.props),s=e.key,i=e.ref,a=e._owner;if(null!=t){if(void 0!==t.ref&&(i=t.ref,a=T.current),void 0!==t.key&&(s=""+t.key),e.type&&e.type.defaultProps)var c=e.type.defaultProps;for(u in t)x.call(t,u)&&!C.hasOwnProperty(u)&&(o[u]=void 0===t[u]&&void 0!==c?c[u]:t[u])}var u=arguments.length-2;if(1===u)o.children=r;else if(1<u){c=Array(u);for(var p=0;p<u;p++)c[p]=arguments[p+2];o.children=c}return{$$typeof:l,type:e.type,key:s,ref:i,props:o,_owner:a}},t.createContext=function(e,t){return void 0===t&&(t=null),(e={$$typeof:p,_calculateChangedBits:t,_currentValue:e,_currentValue2:e,_threadCount:0,Provider:null,Consumer:null}).Provider={$$typeof:u,_context:e},e.Consumer=e},t.createElement=O,t.createFactory=function(e){var t=O.bind(null,e);return t.type=e,t},t.createRef=function(){return{current:null}},t.forwardRef=function(e){return{$$typeof:f,render:e}},t.isValidElement=k,t.lazy=function(e){return{$$typeof:m,_ctor:e,_status:-1,_result:null}},t.memo=function(e,t){return{$$typeof:h,type:e,compare:void 0===t?null:t}},t.useCallback=function(e,t){return H().useCallback(e,t)},t.useContext=function(e,t){return H().useContext(e,t)},t.useDebugValue=function(){},t.useEffect=function(e,t){return H().useEffect(e,t)},t.useImperativeHandle=function(e,t,r){return H().useImperativeHandle(e,t,r)},t.useLayoutEffect=function(e,t){return H().useLayoutEffect(e,t)},t.useMemo=function(e,t){return H().useMemo(e,t)},t.useReducer=function(e,t,r){return H().useReducer(e,t,r)},t.useRef=function(e){return H().useRef(e)},t.useState=function(e){return H().useState(e)},t.version="16.13.1"},function(e,t,r){"use strict";
/*
object-assign
(c) Sindre Sorhus
@license MIT
*/var n=Object.getOwnPropertySymbols,o=Object.prototype.hasOwnProperty,l=Object.prototype.propertyIsEnumerable;function s(e){if(null==e)throw new TypeError("Object.assign cannot be called with null or undefined");return Object(e)}e.exports=function(){try{if(!Object.assign)return!1;var e=new String("abc");if(e[5]="de","5"===Object.getOwnPropertyNames(e)[0])return!1;for(var t={},r=0;r<10;r++)t["_"+String.fromCharCode(r)]=r;if("0123456789"!==Object.getOwnPropertyNames(t).map((function(e){return t[e]})).join(""))return!1;var n={};return"abcdefghijklmnopqrst".split("").forEach((function(e){n[e]=e})),"abcdefghijklmnopqrst"===Object.keys(Object.assign({},n)).join("")}catch(e){return!1}}()?Object.assign:function(e,t){for(var r,i,a=s(e),c=1;c<arguments.length;c++){for(var u in r=Object(arguments[c]))o.call(r,u)&&(a[u]=r[u]);if(n){i=n(r);for(var p=0;p<i.length;p++)l.call(r,i[p])&&(a[i[p]]=r[i[p]])}}return a}},function(e,t,r){"use strict";r.r(t);var n=r(0),o=r.n(n);class l extends n.Component{render(){return o.a.createElement("button",{type:"button",className:this.props.buttonClass,onClick:this.props.clickHandler},this.props.buttonText)}}class s extends n.Component{clickHandler(){console.log("You clicked! How can you click!")}render(){return o.a.createElement(l,{buttonText:"Complete",clickHandler:this.clickHandler,buttonClass:"btn btn-outline-success btn-sm align-self-end"})}}class i extends n.Component{clickHandler(){console.log("You tried to comment")}render(){return o.a.createElement(l,{buttonText:"Comment",clickHandler:this.clickHandler,buttonClass:"btn btn-outline-info btn-sm align-self-end"})}}class a extends n.Component{render(){return o.a.createElement("div",{className:"row"},o.a.createElement("div",{className:"col-md-12 text-right"},o.a.createElement(i,null),o.a.createElement(s,null)))}}var c=a;class u extends n.Component{render(){return o.a.createElement("img",{className:"prof-pic-small",src:this.props.profPic,alt:"prof-pic"})}}var p=u;class f extends n.Component{render(){return o.a.createElement("b",null,"User Name")}}var d=f;class h extends n.Component{render(){return o.a.createElement("div",{className:"time-info"},"12:30 PM Jun 15th")}}var m=h;class v extends n.Component{render(){return o.a.createElement("div",{className:"row"},o.a.createElement("div",{className:"col-sm-1"},o.a.createElement(p,{profPic:"/static/img/profile_pics/default.png"})),o.a.createElement("div",{className:"col-sm-11"},o.a.createElement(d,null),o.a.createElement(m,null)))}}var y=v;class g extends n.Component{render(){return o.a.createElement("div",{className:"row "},o.a.createElement("div",{className:"card-info"},"Day Name - ",o.a.createElement("b",null,"Project Name")," Day X"))}}var b=g;class E extends n.Component{render(){return o.a.createElement("div",{className:"row "},o.a.createElement("div",{className:"day-details"},"Day Details - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."))}}var w=E;class S extends n.Component{render(){return o.a.createElement("div",{className:"row"},o.a.createElement("div",{className:"user-comment"},"User Comment: this was super fun"))}}var _=S;class T extends n.Component{render(){return o.a.createElement("div",{className:"feed-card"},o.a.createElement(y,null),o.a.createElement(b,null),o.a.createElement(w,null),o.a.createElement(_,null),o.a.createElement(c,null))}}var x=T,C=function(e,t){return(C=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var r in t)t.hasOwnProperty(r)&&(e[r]=t[r])})(e,t)};
/*! *****************************************************************************
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0

THIS CODE IS PROVIDED ON AN *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
MERCHANTABLITY OR NON-INFRINGEMENT.

See the Apache Version 2.0 License for specific language governing permissions
and limitations under the License.
***************************************************************************** */var O=function(){return(O=Object.assign||function(e){for(var t,r=1,n=arguments.length;r<n;r++)for(var o in t=arguments[r])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e}).apply(this,arguments)};var k="Pixel",j="Percent",D={unit:j,value:.8};var P=function(e){function t(t){var r=e.call(this,t)||this;return r.lastScrollTop=0,r.actionTriggered=!1,r.startY=0,r.currentY=0,r.dragging=!1,r.maxPullDownDistance=0,r.getScrollableTarget=function(){return r.props.scrollableTarget instanceof HTMLElement?r.props.scrollableTarget:"string"==typeof r.props.scrollableTarget?document.getElementById(r.props.scrollableTarget):(null===r.props.scrollableTarget&&console.warn("You are trying to pass scrollableTarget but it is null. This might\n        happen because the element may not have been added to DOM yet.\n        See https://github.com/ankeetmaini/react-infinite-scroll-component/issues/59 for more info.\n      "),null)},r.onStart=function(e){r.lastScrollTop||(r.dragging=!0,e instanceof MouseEvent?r.startY=e.pageY:e instanceof TouchEvent&&(r.startY=e.touches[0].pageY),r.currentY=r.startY,r._infScroll&&(r._infScroll.style.willChange="transform",r._infScroll.style.transition="transform 0.2s cubic-bezier(0,0,0.31,1)"))},r.onMove=function(e){r.dragging&&(e instanceof MouseEvent?r.currentY=e.pageY:e instanceof TouchEvent&&(r.currentY=e.touches[0].pageY),r.currentY<r.startY||(r.currentY-r.startY>=Number(r.props.pullDownToRefreshThreshold)&&r.setState({pullToRefreshThresholdBreached:!0}),r.currentY-r.startY>1.5*r.maxPullDownDistance||r._infScroll&&(r._infScroll.style.overflow="visible",r._infScroll.style.transform="translate3d(0px, "+(r.currentY-r.startY)+"px, 0px)")))},r.onEnd=function(){r.startY=0,r.currentY=0,r.dragging=!1,r.state.pullToRefreshThresholdBreached&&r.props.refreshFunction&&r.props.refreshFunction(),requestAnimationFrame((function(){r._infScroll&&(r._infScroll.style.overflow="auto",r._infScroll.style.transform="none",r._infScroll.style.willChange="none")}))},r.onScrollListener=function(e){"function"==typeof r.props.onScroll&&setTimeout((function(){return r.props.onScroll&&r.props.onScroll(e)}),0);var t=r.props.height||r._scrollableNode?e.target:document.documentElement.scrollTop?document.documentElement:document.body;r.actionTriggered||(r.isElementAtBottom(t,r.props.scrollThreshold)&&r.props.hasMore&&(r.actionTriggered=!0,r.setState({showLoader:!0}),r.props.next&&r.props.next()),r.lastScrollTop=t.scrollTop)},r.state={showLoader:!1,pullToRefreshThresholdBreached:!1},r.throttledOnScrollListener=function(e,t,r,n){var o,l=!1,s=0;function i(){o&&clearTimeout(o)}function a(){var a=this,c=Date.now()-s,u=arguments;function p(){s=Date.now(),r.apply(a,u)}function f(){o=void 0}l||(n&&!o&&p(),i(),void 0===n&&c>e?p():!0!==t&&(o=setTimeout(n?f:p,void 0===n?e-c:e)))}return"boolean"!=typeof t&&(n=r,r=t,t=void 0),a.cancel=function(){i(),l=!0},a}(150,r.onScrollListener).bind(r),r.onStart=r.onStart.bind(r),r.onMove=r.onMove.bind(r),r.onEnd=r.onEnd.bind(r),r}return function(e,t){function r(){this.constructor=e}C(e,t),e.prototype=null===t?Object.create(t):(r.prototype=t.prototype,new r)}(t,e),t.prototype.componentDidMount=function(){if(void 0===this.props.dataLength)throw new Error('mandatory prop "dataLength" is missing. The prop is needed when loading more content. Check README.md for usage');if(this._scrollableNode=this.getScrollableTarget(),this.el=this.props.height?this._infScroll:this._scrollableNode||window,this.el&&this.el.addEventListener("scroll",this.throttledOnScrollListener),"number"==typeof this.props.initialScrollY&&this.el&&this.el instanceof HTMLElement&&this.el.scrollHeight>this.props.initialScrollY&&this.el.scrollTo(0,this.props.initialScrollY),this.props.pullDownToRefresh&&this.el&&(this.el.addEventListener("touchstart",this.onStart),this.el.addEventListener("touchmove",this.onMove),this.el.addEventListener("touchend",this.onEnd),this.el.addEventListener("mousedown",this.onStart),this.el.addEventListener("mousemove",this.onMove),this.el.addEventListener("mouseup",this.onEnd),this.maxPullDownDistance=this._pullDown&&this._pullDown.firstChild&&this._pullDown.firstChild.getBoundingClientRect().height||0,this.forceUpdate(),"function"!=typeof this.props.refreshFunction))throw new Error('Mandatory prop "refreshFunction" missing.\n          Pull Down To Refresh functionality will not work\n          as expected. Check README.md for usage\'')},t.prototype.componentWillUnmount=function(){this.el&&(this.el.removeEventListener("scroll",this.throttledOnScrollListener),this.props.pullDownToRefresh&&(this.el.removeEventListener("touchstart",this.onStart),this.el.removeEventListener("touchmove",this.onMove),this.el.removeEventListener("touchend",this.onEnd),this.el.removeEventListener("mousedown",this.onStart),this.el.removeEventListener("mousemove",this.onMove),this.el.removeEventListener("mouseup",this.onEnd)))},t.prototype.UNSAFE_componentWillReceiveProps=function(e){this.props.key===e.key&&this.props.dataLength===e.dataLength||(this.actionTriggered=!1,this.setState({showLoader:!1,pullToRefreshThresholdBreached:!1}))},t.prototype.isElementAtBottom=function(e,t){void 0===t&&(t=.8);var r=e===document.body||e===document.documentElement?window.screen.availHeight:e.clientHeight,n=function(e){return"number"==typeof e?{unit:j,value:100*e}:"string"==typeof e?e.match(/^(\d*(\.\d+)?)px$/)?{unit:k,value:parseFloat(e)}:e.match(/^(\d*(\.\d+)?)%$/)?{unit:j,value:parseFloat(e)}:(console.warn('scrollThreshold format is invalid. Valid formats: "120px", "50%"...'),D):(console.warn("scrollThreshold should be string or number"),D)}(t);return n.unit===k?e.scrollTop+r>=e.scrollHeight-n.value:e.scrollTop+r>=n.value/100*e.scrollHeight},t.prototype.render=function(){var e=this,t=O({height:this.props.height||"auto",overflow:"auto",WebkitOverflowScrolling:"touch"},this.props.style),r=this.props.hasChildren||!!(this.props.children&&this.props.children instanceof Array&&this.props.children.length),n=this.props.pullDownToRefresh&&this.props.height?{overflow:"auto"}:{};return o.a.createElement("div",{style:n,className:"infinite-scroll-component__outerdiv"},o.a.createElement("div",{className:"infinite-scroll-component "+(this.props.className||""),ref:function(t){return e._infScroll=t},style:t},this.props.pullDownToRefresh&&o.a.createElement("div",{style:{position:"relative"},ref:function(t){return e._pullDown=t}},o.a.createElement("div",{style:{position:"absolute",left:0,right:0,top:-1*this.maxPullDownDistance}},this.state.pullToRefreshThresholdBreached?this.props.releaseToRefreshContent:this.props.pullDownToRefreshContent)),this.props.children,!this.state.showLoader&&!r&&this.props.hasMore&&this.props.loader,this.state.showLoader&&this.props.hasMore&&this.props.loader,!this.props.hasMore&&this.props.endMessage))},t}(n.Component);class L extends n.Component{constructor(...e){var t;return t=super(...e),this.state={cards:[],initialCount:20,moreCount:10},this.fetchMoreData=()=>{this.fetchData(this.state.moreCount)},this.fetchData=e=>{for(var t=[],r=0;r<e;r++)t.push(r);this.setState({cards:this.state.cards.concat(t)})},t}componentDidMount(){this.fetchData(this.state.initialCount)}render(){return o.a.createElement("div",null,o.a.createElement("hr",null),o.a.createElement("div",{className:"main-feed"},o.a.createElement(P,{dataLength:this.state.cards.length,next:this.fetchMoreData,hasMore:!0,loader:o.a.createElement("h4",null,"Loading...")},this.state.cards.map((e,t)=>o.a.createElement(x,null)))))}}ReactDOM.render(o.a.createElement(L,null),document.getElementById("feed"))}]);