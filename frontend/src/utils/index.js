import ReactGA from 'react-ga';
// eslint-disable-next-line
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
