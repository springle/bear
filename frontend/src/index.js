import React from 'react';
import ReactDOM from 'react-dom';
import { handleEvent } from './utils';
import { lowerCase } from 'lodash';
import registerServiceWorker from './registerServiceWorker';
import Home from './App/Home';
import 'typeface-roboto';

const debug = false;
var ReactGA = require('react-ga');
ReactGA.initialize('UA-105377090-1');

function logPageView() {
  if (debug || window.location.hostname !== "localhost") {
    const path = window.location.pathname + window.location.search;
    ReactGA.set({ path });
    ReactGA.pageview(path);
  }
}

window.addEventListener('scroll', function(e) {
  if (debug || window.location.hostname !== "localhost") {
    const path = window.location.pathname + window.location.search;
    if (!debug) {
      handleEvent('Scroll', path);
    }
  }
});

window.addEventListener('mousemove', function(e) {
  if (debug || window.location.hostname !== "localhost") {
    const path = window.location.pathname + window.location.search;
    if (!debug) {
      handleEvent('Mouse', lowerCase(path));
    }
  }
});

window.addEventListener('click', function(e) {
  if (debug || window.location.hostname !== "localhost") {
    const path = window.location.pathname + window.location.search;
    if (!debug) {
      handleEvent('Click', lowerCase(path));
    }
  }
});

window.addEventListener('keypress', function(e) {
  if (debug || window.location.hostname !== "localhost") {
    const path = window.location.pathname + window.location.search;
    if (!debug) {
      handleEvent('KeyPress', lowerCase(path));
    }
  }
});

// eslint-disable-next-line
{/*
	react-GA requires react-router as an npm package, where we have:

	var app = document.getElementById('root');
	ReactDOM.render(<Router routes={routes} onUpdate={logPageView} />, app);
	registerServiceWorker();

	replace everything below this comment
*/}
ReactDOM.render(<Home onUpdate={logPageView} />, document.getElementById('root'));
registerServiceWorker();
