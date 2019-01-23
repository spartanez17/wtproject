import React from "react";
import axios from "axios";
import CustomForm from "components/Form";
import WeatherWidget from "components/WeatherWidget";

class Main extends React.Component {
  state = {
    weather: {},
  };
  //celsius
  //kelvin
  //fahrenheit

  fetchWeather = (query, units) => {
    console.log(query)
    let params = {
      q: query,
      units
    };
    axios
      .get("http://127.0.0.1:8000/api/weather", {
        params
      })
      .then(res => {
        this.setState({
          weather: res.data
        });
      })
      .catch(rej => {
        console.log("ERROR\n", rej);
      });
  };

  render() {
    return (
      <React.Fragment>
        <CustomForm handleSubmit={this.fetchWeather} />
        <WeatherWidget weather={this.state.weather} />
      </React.Fragment>
    );
  }
}

export default Main;
