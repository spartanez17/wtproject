import * as actionTypes from "../actions/actionTypes";
import {
  initialState as initAuth,
  authStart,
  authSuccess,
  authFail,
  authLogout
} from "./auth";
import {
  initialState as initWeather,
  requestStart,
  requestSuccess,
  requestFail
} from "./weather";

const initialState = {
  ...initAuth,
  ...initWeather
}

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.AUTH_START:
      return authStart(state, action);
    case actionTypes.AUTH_SUCCESS:
      return authSuccess(state, action);
    case actionTypes.AUTH_FAIL:
      return authFail(state, action);
    case actionTypes.AUTH_LOGOUT:
      return authLogout(state, action);

    case actionTypes.REQUEST_START:
      return requestStart(state, action);
    case actionTypes.REQUEST_SUCCESS:
      return requestSuccess(state, action);
    case actionTypes.REQUEST_FAIL:
      return requestFail(state, action);

    default:
      return state;
  }
};

export default reducer;
