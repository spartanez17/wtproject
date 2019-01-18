import React from "react";
import { Switch, Route } from "react-router-dom";
import AuthRoute from "components/AuthRoute/container";
import ArticleList from "./containers/ArticleListView";
import ArticleDetail from "./containers/ArticleDetailView";
import Login from "./containers/Login";
import Signup from "./containers/Signup";
import { routes } from "assets";

const BaseRouter = () => (
  <div>
    <Switch>
      <AuthRoute
        exact
        path={routes.WEATHER}
        component={ArticleList}
        userAuthRequired
      />
      <AuthRoute exact path="/login/" component={Login} noAuthRequired />
      <AuthRoute exact path="/signup/" component={Signup} noAuthRequired />
    </Switch>
  </div>
);

export default BaseRouter;
