import React from "react";
import { Container } from "reactstrap";
import { connect } from "react-redux";

import CustomForm from "components/Form";
import WeatherWidget from "components/WeatherWidget";
import * as actions from "store/actions/weather";

class Main extends React.Component {
  fetchWeather = (query, units) => {
    this.props.fetchWeather(query, units);
  };

  render() {
    const {weather} = this.props || null;
    return (
      <div className="w-75" style={{ margin: "0 auto" }}>
        <CustomForm handleSubmit={this.fetchWeather} />
        {weather ? (
          <WeatherWidget weather={weather} />
        ) : (
          <Container
            className="d-flex align-items-center justify-content-center"
            style={{ height: "30vh", color: "gray" }}
          >
            <h3> Nothing to geoloc. </h3>
          </Container>
        )}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    weather: state.currWeather,
    requestLoading: state.requestLoading,
    requestError: state.requestError
  };
};

const mapDispatchToProps = dispatch => {
  return {
    fetchWeather: (query, units) =>
      dispatch(actions.fetchCurrentWeather(query, units))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Main);
