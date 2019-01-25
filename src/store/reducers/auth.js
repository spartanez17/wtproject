const initialState = {
  token: null,
  error: null,
  loading: false
};

const authStart = (state, action) => {
  return {
    ...state,
    error: null,
    loading: true
  }
};

const authSuccess = (state, action) => {
  return {
    ...state,
    token: action.token,
    username: action.username,
    error: null,
    loading: false
  }
};

const authFail = (state, action) => {
  return {
    ...state,
    error: action.error,
    loading: false
  }
};

const authLogout = (state, action) => {
  return  {
    ...state,
    token: null,
    username: null
  }
};

export { authStart, authSuccess, authFail, authLogout, initialState };
