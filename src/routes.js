import React from "react";
import { Switch } from "react-router-dom";

import Main from "./containers/Main";
import Login from "./containers/Login";
import Signup from "./containers/Signup";
import AuthRoute from "components/AuthRoute/container";

import { routes } from "assets";

const BaseRouter = () => (
  <div>
    <Switch>
      <AuthRoute
        exact
        path={routes.WEATHER}
        component={Main}
        userAuthRequired
      />
      <AuthRoute exact path={routes.SIGN_UP} component={Signup} noAuthRequired />
      <AuthRoute exact path={routes.SIGN_IN} component={Login} noAuthRequired />
    </Switch>
  </div>
);

export default BaseRouter;
