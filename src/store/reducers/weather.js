const initialState = {
  weather: null,
  requestError: null,
  requestLoading: false
};

const requestStart = (state, action) => {
  return {
    ...state,
    requestError: null,
    requestLoading: true
  };
};

const requestSuccess = (state, action) => {
  return {
    ...state,
    requestError: null,
    requestLoading: false,
    ...action.subStore
  };
};

const requestFail = (state, action) => {
  return {
    ...state,
    requestError: action.error,
    requestLoading: false
  };
};

export { requestStart, requestSuccess, requestFail, initialState };
