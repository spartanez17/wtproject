import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import PropTypes from 'prop-types';

import {routes} from 'assets';

const AuthRoute = props => {
  // const token = localStorage.getItem("token");
  const { token, noAuthRequired, userAuthRequired } = props;
  let { redirectTo } = props;

  if (userAuthRequired && !token) {
    redirectTo = redirectTo || routes.LOGIN;
    return <Redirect to={redirectTo} push />;
  }

  if (noAuthRequired && token) {
    redirectTo = redirectTo || routes.WEATHER;
    return <Redirect to={redirectTo} push />;
  }

  return <Route {...props} />;
};

AuthRoute.propTypes = {
  token: PropTypes.string,
  noAuthRequired: PropTypes.bool,
  userAuthRequired: PropTypes.bool,
  ...Route.propTypes,
};

export default AuthRoute;