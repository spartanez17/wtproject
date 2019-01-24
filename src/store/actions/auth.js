import axios from "axios";
import * as actionTypes from "./actionTypes";
import { urls } from "assets";

export const authStart = () => {
  return {
    type: actionTypes.AUTH_START
  };
};

export const authSuccess = (token, username) => {
  return {
    type: actionTypes.AUTH_SUCCESS,
    token: token,
    username: username
  };
};

export const authFail = error => {
  return {
    type: actionTypes.AUTH_FAIL,
    error: error
  };
};

export const logout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("username");
  return {
    type: actionTypes.AUTH_LOGOUT
  };
};

export const authLogin = (username, password) => {
  return dispatch => {
    dispatch(authStart());
    axios
      .post(urls.SIGN_IN, {
        username: username,
        password: password
      })
      .then(res => {
        console.log('response')
        const token = res.data.key;
        localStorage.setItem("token", token);
        localStorage.setItem("username", username);
        dispatch(authSuccess(token, username));
      })
      .catch(err => {
        console.log('response')
        dispatch(authFail(err));
      });
  };
};

export const authSignup = (username, email, password1, password2) => {
  return dispatch => {
    dispatch(authStart());
    axios
      .post(urls.SIGN_UP, {
        username: username,
        email: email,
        password1: password1,
        password2: password2
      })
      .then(res => {
        const token = res.data.key;
        localStorage.setItem("token", token);
        localStorage.setItem("username", username);
        dispatch(authSuccess(token, username));
      })
      .catch(err => {
        dispatch(authFail(err));
      });
  };
};

export const authCheckState = () => {
  return dispatch => {
    const token = localStorage.getItem("token");
    const username = localStorage.getItem("username");

    if (token === undefined) {
      dispatch(logout());
    } else {
      dispatch(authSuccess(token, username));
    }
  };
};
