import ReactGA from 'react-ga';
const _ = require('lodash');

function handleEvent(category, action, label="") {
  ReactGA.event({
    category,
    action,
    label,
  });
}

export {
  handleEvent
};
