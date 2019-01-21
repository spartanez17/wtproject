import React from "react";
import { AvForm, AvField } from "availity-reactstrap-validation";
import { Button, Alert } from "reactstrap";
import { connect } from "react-redux";
import { NavLink } from "react-router-dom";

import * as actions from "store/actions/auth";
import { routes } from "assets";

const formatMessage =
  "Your name must be composed only with letters and numbers";

const lengthMessage = (min, max) =>
  `Your name must be between ${min} and ${max} characters`;

class LoginForm extends React.Component {
  handleValidSubmit = (event, values) => {
    this.props.onAuth(values.username, values.password);
    this.props.history.push("/");
  };

  render() {
    const { error } = this.props;

    return (
      <div className="w-50" style={{ marginLeft: "25vw" }}>
        <AvForm onValidSubmit={this.handleValidSubmit}>
          {error ? (
            <Alert color="danger">
              Unable to log in with provided credentials.
            </Alert>
          ) : null}
          <AvField
            name="username"
            label=" Username"
            type="text"
            validate={{
              required: {
                value: true,
                errorMessage: "Please enter a username"
              },
              pattern: {
                value: "^[A-Za-z0-9]+$",
                errorMessage: formatMessage
              },
              minLength: {
                value: 4,
                errorMessage: lengthMessage(4, 12)
              },
              maxLength: {
                value: 12,
                errorMessage: lengthMessage(4, 12)
              }
            }}
          />
          <AvField
            name="password"
            label="Password"
            type="password"
            validate={{
              required: {
                value: true,
                errorMessage: "Please enter a password"
              },
              pattern: {
                value: "^[A-Za-z0-9]+$",
                errorMessage: formatMessage
              },
              minLength: {
                value: 4,
                errorMessage: lengthMessage(4, 20)
              },
              maxLength: {
                value: 20,
                errorMessage: lengthMessage(4, 20)
              }
            }}
          />
          <Button type="submit" color="primary">
            Sign in
          </Button>
          {" or "}
          <NavLink to={routes.SIGN_UP}>Sign up</NavLink>
        </AvForm>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    loading: state.loading,
    error: state.error
  };
};

const mapDispatchToProps = dispatch => {
  return {
    onAuth: (username, password) =>
      dispatch(actions.authLogin(username, password))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginForm);
