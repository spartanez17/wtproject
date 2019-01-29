import React from "react";
import { Container, Row, Col } from "reactstrap";

class WeatherWidget extends React.Component {
  render() {
    const {
      desc,
      icon,
      temp,
      humidity,
      windSpeed,
      date,
      country,
      city,
      units
    } = this.props.weather;
    let dateObj = new Date(date*1000);

    var options = {
      hour12: false,
      year: "numeric",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      month: "long"
    };
    console.log(date);
    let dateFormat = dateObj.toLocaleTimeString("en-UN", options);
    let day = dateObj.getDate();
    let hour = dateObj.getHours()
    let mounth = dateObj.getMonth();
    let year = dateObj.getFullYear();
    console.log(hour, day, mounth, year)
    console.log(dateObj.getDate());

    return (
      <Container className="rounded mw-100" style={{ height: "50vh" }}>
        <Row>
          <Col md={{ size: 6, offset: 3 }}>
            <p className="h3 font-weight-bold">{`Weather in ${city}, ${country}`}</p>
          </Col>
        </Row>
        <Row>
          <Col
            className="d-flex flex-column w-100 justify-content-center align-items-center"
            md={{ size: 5, offset: 2 }}
          >
            <h1>
              <img src={`http://openweathermap.org/img/w/${icon}.png`} alt="" />
              <span>{`${temp} ${units.symb}`} </span>
            </h1>
            <p className="text-secondary">{desc}</p>
            <p className="text-secondary">{dateFormat}</p>
          </Col>
          <Col className="d-flex flex-column w-100 justify-content-center align-items-start">
            <p className="h5 text-secondary">{`Humidity: ${humidity}%`}</p>
            <p className="h5 text-secondary">{`Wind: ${windSpeed} ${
              units.speed
            }`}</p>
          </Col>
        </Row>
      </Container>
    );
  }
}
export default WeatherWidget;
