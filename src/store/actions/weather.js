import axios from "axios";
import * as actionTypes from "./actionTypes";
import { urls } from "assets";

export const requestStart = () => {
  return {
    type: actionTypes.REQUEST_START
  };
};

export const requestSuccess = subStore => {
  return {
    type: actionTypes.REQUEST_SUCCESS,
    subStore
  };
};

export const requestFail = error => {
  return {
    type: actionTypes.REQUEST_FAIL,
    requestError: error
  };
};

export const fetchCurrentWeather = (query, units) => {
  return dispatch => {
    dispatch(requestStart());
    let params = {
      query,
      units: units.query
    };
    axios
      .get(urls.WEATHER, {
        params
      })
      .then(res => {
        let weather = res.data;
        weather.units = units;
        dispatch(requestSuccess({ currWeather: weather }));
      })
      .catch(err => {
        dispatch(requestFail(err));
      });
  };
};
