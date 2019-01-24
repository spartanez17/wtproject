import React from "react";
import axios from "axios";
import CustomForm from "components/Form";
import WeatherWidget from "components/WeatherWidget";
import { Container, Row, Col } from "reactstrap";
import { urls } from "assets";

class Main extends React.Component {
  state = {
    weather: {
      desc: "descriptoin",
      icon: "10d",
      temp: 12,
      humidity: "88",
      windSpeed: 5,
      date: 764289168,
      country: "BY",
      city: "Minsk",
      units: "celsius"
    }
  };

  fetchWeather = ({ query, units }) => {
    console.log(query);
    let params = {
      query,
      units
    };
    axios
      .get(urls.WEATHER, {
        params
      })
      .then(res => {
        let weather = res.data;
        weather.units = units;

        this.setState({
          weather
        });
      })
      .catch(rej => {
        console.log("ERROR\n", rej);
      });
  };

  render() {
    return (
      <div className="w-75" style={{ margin: "0 auto" }}>
        <CustomForm handleSubmit={this.fetchWeather} />
        {this.state.weather ? (
          <WeatherWidget weather={this.state.weather} />
        ) : (
          <Container
            className="d-flex align-items-center justify-content-center"
            style={{ height: "50vh", color: "gray" }}
          >
            <h3> Nothing to geoloc </h3>
          </Container>
        )}
      </div>
    );
  }
}

export default Main;
