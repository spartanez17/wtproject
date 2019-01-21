import React from "react";
import { AvForm, AvField } from "availity-reactstrap-validation";
import { Button } from "reactstrap";
import { connect } from "react-redux";
import { NavLink } from "react-router-dom";

import * as actions from "store/actions/auth";
import { routes } from "assets";

const formatMessage =
  "Your name must be composed only with letters and numbers";

const lengthMessage = (min, max) =>
  `Your name must be between ${min} and ${max} characters`;

class SignupForm extends React.Component {
  handleValidSubmit = (event, values) => {
    this.props.onAuth(
      values.username,
      values.email,
      values.password,
      values.confpassword
    );
    this.props.history.push("/");
  };

  render() {
    return (
      <div className="w-50" style={{ marginLeft: "25vw" }}>
        <AvForm onValidSubmit={this.handleValidSubmit}>
          <AvField
            name="username"
            label="Username"
            type="text"
            errorMessage="Invalid field"
            validate={{
              required: { value: true, errorMessage: "Please enter a username" },
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

          <AvField name="email" label="Email" type="email" />
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
          <AvField
            name="confpassword"
            label="Confirm password"
            type="password"
            validate={{ match: { value: "password" } }}
          />
          <Button type="submit" color="primary">
            Sign up
          </Button>
          {" or "}
          <NavLink to={routes.SIGN_IN}>Sign in</NavLink>
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
    onAuth: (username, email, password1, password2) =>
      dispatch(actions.authSignup(username, email, password1, password2))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(SignupForm);
